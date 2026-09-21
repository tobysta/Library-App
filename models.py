# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# 1. Book Issued Count Table (Often used for analytics/counters)
class BookIssuedCnt(db.Model):
    __tablename__ = 'book_issued_cnt'
    isbn = db.Column(db.String(50), primary_key=True)
    book_title = db.Column(db.String(255), nullable=False)
    issues_count = db.Column(db.Integer, default=0)

# 2. Books Table
class Book(db.Model):
    __tablename__ = 'books'
    isbn = db.Column(db.String(50), primary_key=True)  # change to your primary key
    book_title = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(100))
    rental_price = db.Column(db.Float)
    status = db.Column(db.String(10))  # e.g., 'yes' or 'no' for availability
    author = db.Column(db.String(100))
    publisher = db.Column(db.String(100))

# 3. Branch Table
class Branch(db.Model):
    __tablename__ = 'branch'
    branch_id = db.Column(db.String(50), primary_key=True)
    manager_id = db.Column(db.String(50))
    branch_address = db.Column(db.String(255))
    contact_no = db.Column(db.String(20))

# 4. Employees Table
class Employee(db.Model):
    __tablename__ = 'employees'
    emp_id = db.Column(db.String(50), primary_key=True)
    emp_name = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(50))
    salary = db.Column(db.Float)
    branch_id = db.Column(db.String(50))  # Links to Branch

# 5. Issued Status Table (Tracks when a book is checked out)
class IssuedStatus(db.Model):
    __tablename__ = 'issued_status'
    issued_id = db.Column(db.String(50), primary_key=True)
    issued_member_id = db.Column(db.String(50))  # Links to Member
    issued_book_name = db.Column(db.String(255))
    issued_date = db.Column(db.Date)
    issued_book_isbn = db.Column(db.String(50))  # Links to Book
    issued_emp_id = db.Column(db.String(50))     # Links to Employee

# 6. Members Table
class Member(db.Model):
    __tablename__ = 'members'
    member_id = db.Column(db.String(50), primary_key=True)
    member_name = db.Column(db.String(100), nullable=False)
    member_address = db.Column(db.String(255))
    reg_date = db.Column(db.Date)


# 7. Return Status Table (Tracks when a book is brought back)
class ReturnStatus(db.Model):
    __tablename__ = 'return_status'
    return_id = db.Column(db.String(50), primary_key=True)
    issued_id = db.Column(db.String(50))          # Links to IssuedStatus
    return_date = db.Column(db.Date)
    


	