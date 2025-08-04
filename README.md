# 📚 LMS (Learning Management System)

A simple **Flask-based Learning Management System** for managing students, subjects, and timetables.

## 🚀 Features
- User Registration & Login
- View Subjects
- View Timetable
- SQLite Database for storing information
- HTML Templates for UI

## 🛠️ Tech Stack
- **Backend:** Python (Flask)
- **Database:** SQLite
- **Frontend:** HTML, CSS (Bootstrap)
- **Others:** Jinja2 Templates

## 📂 Project Structure
```
lms_flask/
│── app.py              # Main Flask app
│── models.py           # Database models
│── config.py           # Configuration settings
│── instance/lms.db     # SQLite database file
│── templates/          # HTML templates
│   ├── register.html
│   ├── subjects.html
│   ├── timetable.html
│── static/             # Static files (CSS, JS, images)
│── README.md           # Project documentation
```

## ⚙️ Installation & Setup

1. **Clone the repository**
```bash
git clone https://github.com/Chandananl15/LMS.git
cd LMS
```

2. **Create a virtual environment**
```bash
python -m venv venv
```

3. **Activate the virtual environment**
- **Windows**
```bash
venv\Scripts\activate
```
- **Mac/Linux**
```bash
source venv/bin/activate
```

4. **Install dependencies**
```bash
pip install -r requirements.txt
```

5. **Run the application**
```bash
python app.py
```

6. **Open in browser**
```
http://127.0.0.1:5000
```

## 👩‍💻 Author
**Chandana N L**  
GitHub: [Chandananl15](https://github.com/Chandananl15)

---

⭐ If you like this project, consider giving it a star!
