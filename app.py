from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, Subject, Enrollment
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Create database tables & add default subjects
def create_tables():
    with app.app_context():
        db.create_all()
        if not Subject.query.first():
            subjects = [
                Subject(name="Mathematics", faculty="Dr. Suresh Kumar", timetable="Mon 10:00-11:00"),
                Subject(name="Physics", faculty="Prof. Meera Sharma", timetable="Tue 09:00-10:00"),
                Subject(name="Chemistry", faculty="Dr. Ramesh Gupta", timetable="Wed 11:00-12:00"),
                Subject(name="Computer Science", faculty="Dr. Priya Nair", timetable="Thu 10:00-11:00")
            ]
            db.session.bulk_save_objects(subjects)
            db.session.commit()

create_tables()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = generate_password_hash(request.form['password'])

        if User.query.filter_by(email=email).first():
            flash("Email already registered.")
            return redirect(url_for('register'))

        new_user = User(name=name, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash("Registration successful. Please log in.")
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash("Invalid email or password.")
    return render_template('login.html')

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/subjects', methods=['GET','POST'])
@login_required
def subjects():
    subjects = Subject.query.all()
    if request.method == 'POST':
        selected_subjects = request.form.getlist('subjects')
        for subject_id in selected_subjects:
            if not Enrollment.query.filter_by(user_id=current_user.id, subject_id=subject_id).first():
                db.session.add(Enrollment(user_id=current_user.id, subject_id=subject_id))
        db.session.commit()
        flash("Subjects enrolled successfully.")
        return redirect(url_for('timetable'))
    return render_template('subjects.html', subjects=subjects)

@app.route('/timetable')
@login_required
def timetable():
    enrollments = Enrollment.query.filter_by(user_id=current_user.id).all()
    subjects = [Subject.query.get(e.subject_id) for e in enrollments]
    return render_template('timetable.html', subjects=subjects)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
