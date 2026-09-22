# Library-App

A data-driven Flask web application that connects a MySQL library database with Python and displays employee and library reports through HTML pages.

## Features

- Displays fiction books from the library database
- Shows employees with salary greater than 40,000, sorted by salary in descending order
- Identifies book categories containing more than two books
- Calculates total issues for each book title
- Displays books with a rental price greater than 3
- Uses Flask routes, SQLAlchemy ORM queries, Jinja HTML templates, and MySQL

## Technologies Used

- Python
- Flask
- Flask-SQLAlchemy
- SQLAlchemy
- MySQL
- PyMySQL
- HTML
- CSS
- Jinja Templates

## Project Structure

```text
library-db/
├── app.py
├── models.py
├── routes.py
├── requirements.txt
├── .env.example
├── .gitignore
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── books.html
│   ├── high_salary.html
│   ├── categories.html
│   ├── sum_of_data.html
│   └── price.html
└── static/
    └── style.css
```

## Database Tables

The project uses the following MySQL tables:

- `books`
- `employees`
- `branch`
- `members`
- `issued_status`
- `return_status`
- `book_issued_cnt`

## Reports

| Report | Route | Description |
|---|---|---|
| Fiction Books | `/books/fiction` | Displays books whose category is Fiction |
| High Salary Employees | `/employees/high-salary` | Displays employee positions with salary greater than 40,000 |
| Popular Categories | `/books/popular-categories` | Displays categories that have more than two books |
| Total Book Issues | `/book_issued_cnt/sum-of-books` | Calculates total book issues by title |
| Rental Price Analysis | `/books/pricing` | Displays books with rental price greater than 3 |

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/tobysta/library-app
cd library-app
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

Windows Command Prompt:

```bat
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

```bash
pip install Flask Flask-SQLAlchemy PyMySQL
```

## Configure the Database

```text
DATABASE_URL=mysql+pymysql://YOUR_USERNAME:YOUR_PASSWORD@localhost/library-app
```

```python
import os
from flask import Flask
from models import db
from routes import main

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    app.register_blueprint(main)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
```

## Run the Application

Move to the project folder:

```bat
cd C:\Users\manas\library-app
```

Start the Flask application:

```bash
python app.py
```

Flask will display a local URL similar to:

```text
http://127.0.0.1:5000
```

Open that URL in your browser.

## Example Queries Implemented

### Fiction books

```python
Book.query.filter_by(category="Fiction").all()
```

### Employees with salary above 40,000

```python
db.session.query(Employee.position, Employee.salary) \
    .filter(Employee.salary > 40000) \
    .order_by(desc(Employee.salary)) \
    .all()
```

### Categories with more than two books

```python
db.session.query(
    Book.category,
    func.count(Book.category).label("counting")
).group_by(
    Book.category
).having(
    func.count(Book.category) > 2
).all()
```

### Total issue count by book

```python
db.session.query(
    BookIssuedCnt.book_title,
    func.sum(BookIssuedCnt.issues_count).label("total_issues")
).group_by(
    BookIssuedCnt.book_title
).all()
```

## Learning Outcomes

Through this project, I practiced:

- Connecting Python Flask to a MySQL database
- Creating SQLAlchemy models for existing SQL tables
- Converting SQL analysis queries into SQLAlchemy ORM queries
- Building Flask routes with `Blueprint`
- Rendering SQL data dynamically using Jinja HTML templates
- Creating database-driven reports for a simple web UI
- Structuring a Python web application into models, routes, templates, and static files

## Author

Manas Khedkar
