# Expense Tracker

## 📌 Project Overview
The **Expense Tracker** is a Django-based web application that allows users to manage their personal expenses.  
It provides functionality to add, edit, delete, and view expenses, along with CSV import/export support for better data management.

---

## 🚀 Features
- Add new expenses with details (amount, category, description, date).
- Edit or delete existing expenses.
- Import expenses from a CSV file.
- Export expenses to a CSV file.
- Prevent duplicate entries with confirmation.
- Simple and clean user interface using Django Templates.
- Built-in SQLite database for quick setup.

---

## 🛠️ Technologies Used
- **Python 3**
- **Django Web Framework**
- **SQLite** (default database)
- **Django Forms & Templates**
- **Bootstrap (via CDN)** for styling (if linked in templates)
- **CSV Import/Export utilities**

---

## 📂 Project Structure
```
ExpenseTracker/
│── ExpenseTracker/           # Main Django project
│   ├── settings.py           # Project settings
│   ├── urls.py               # URL routing
│   ├── wsgi.py / asgi.py     # Deployment entry points
│
│── expenses/                 # Main app for expense management
│   ├── models.py             # Database models
│   ├── views.py              # Core business logic
│   ├── forms.py              # Django forms
│   ├── urls.py               # App-specific routes
│   ├── api_views.py          # API endpoints (if enabled)
│   ├── import_export.py      # CSV import/export logic
│   ├── templates/expenses/   # HTML templates
│       ├── home.html
│       ├── add_expense.html
│       ├── edit_expense.html
│       ├── delete_expense.html
│       ├── import_csv.html
│       └── duplicate_confirm.html
│
│── db.sqlite3                # SQLite database
│── manage.py                 # Django management script
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/akhilesh-yadav680/ExpenseTracker.git
cd ExpenseTracker
```

### 2️⃣ Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate    # On Windows
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Start the development server
```bash
python manage.py runserver
```

Then open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

---

## 📊 Future Enhancements
- User authentication (login/signup).
- Expense categorization with charts & analytics.
- Multi-user support with personalized dashboards.
- REST API for mobile or external integrations.
- Docker support for deployment.

---

## 🤝 Contributing
Contributions are welcome!  
Feel free to fork this repository, create a branch, and submit a pull request.

---

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
