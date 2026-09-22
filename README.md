# Library-db

A data-driven Flask web application that connects a MySQL library database with Python and displays employee and library reports through HTML pages. The application also provides REST API endpoints that return the report data in JSON format.

## Features

- Displays fiction books from the library database
- Shows employees with salary greater than 40,000, sorted by salary in descending order
- Identifies book categories containing more than two books
- Calculates total issues for each book title
- Displays books with a rental price greater than 3
- Uses Flask routes, SQLAlchemy ORM queries, Jinja HTML templates, and MySQL
- Provides REST API endpoints for report data in JSON format
- Demonstrates both server-rendered HTML pages and API-based data access

## Technologies Used

- Python
- Flask
- Flask-SQLAlchemy
- SQLAlchemy
- MySQL
- PyMySQL
- HTML
- Jinja Templates
- REST API
- JSON

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
    ├── base.html
    ├── index.html
    ├── books.html
    ├── high_salary.html
    ├── categories.html
    ├── sum_of_data.html
    └── price.html

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

## HTML Reports

| Report | Route | Description |
|---|---|---|
| Fiction Books | `/books/fiction` | Displays books whose category is Fiction |
| High Salary Employees | `/employees/high-salary` | Displays employee positions with salary greater than 40,000 |
| Popular Categories | `/books/popular-categories` | Displays categories that have more than two books |
| Total Book Issues | `/book_issued_cnt/sum-of-books` | Calculates total book issues by title |
| Rental Price Analysis | `/books/pricing` | Displays books with rental price greater than 3 |

## REST API Endpoints
The application also exposes the same database reports through REST API endpoints. 
The API routes reuse the SQLAlchemy query logic and return the results in JSON format.

All endpoints use the `GET` method.

| API Endpoint | Method | JSON Fields Returned | Description |
|---|---|---|---|
| `/api/books/fiction` | `GET` | `book_title`, `category`, `author` | Returns fiction books |
| `/api/employees/high-salary` | `GET` | `position`, `salary` | Returns employee positions with salary greater than 40,000 |
| `/api/books/popular-categories` | `GET` | `category`, `book_count` | Returns categories with more than two books |
| `/api/book-issued-count/sum-of-books` | `GET` | `book_title`, `total_issues` | Returns total issued count by book title |
| `/api/books/pricing` | `GET` | `book_title`, `rental_price` | Returns books with rental price greater than 3 |

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/tobysta/library-db
cd library-db
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

## Configure the Database

```text
DATABASE_URL=mysql+pymysql://YOUR_USERNAME:YOUR_PASSWORD@localhost/library-db
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

## Run the Application(HTML)

Move to the project folder:

```bat
cd C:\Users\manas\library-db
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

## Run the Application(RestApi)

Move to the project folder:

```bat
cd C:\Users\manas\library_db_2
```

Start the Flask application:

```bash
python app.py
```

Flask will display a local URL similar to:

```text
http://127.0.0.1:5000/api/books/fiction
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
- Structuring a Python web application into models, routes, templates, and API endpoints

## Author

Manas Khedkar
