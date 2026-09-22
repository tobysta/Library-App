from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from sqlalchemy import desc, func 
from models import db, Employee, Book, BookIssuedCnt

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html', title="Home")

@main.route('/books/fiction')
def view_fiction_books():
    fiction_books = Book.query.filter_by(category='Fiction').all()
    return render_template('books.html', books=fiction_books, title="Fiction Books")

@main.route('/employees/high-salary')
def high_salary_employees():
    high_earners = (
        db.session.query(Employee.position ,Employee.salary)
        .filter(Employee.salary > 40000)
        .order_by(desc(Employee.salary))
        .all()
    )
    
    
    return render_template('high_salary.html', employees=high_earners)

@main.route('/books/popular-categories')
def popular_categories():
    categories_data = (
        db.session.query(
            Book.category, 
            func.count(Book.category).label('counting')
        )
        .group_by(Book.category)
        .having(func.count(Book.category) > 2)
        .all()
    )
    return render_template('categories.html', categories=categories_data)

@main.route('/book_issued_cnt/sum-of-books')
def sum_of_books():
    sum_data = (
        db.session.query(
            BookIssuedCnt.book_title,
            func.sum(BookIssuedCnt.issues_count).label('sum')
        )
        .group_by(BookIssuedCnt.book_title)
        .all()
    )
    return render_template('sum_of_data.html', sum_of_data=sum_data)

@main.route('/books/pricing')
def pricing():
    pricing_books = (
        db.session.query(Book.book_title, Book.rental_price)
        .filter(Book.rental_price > 3)
        .all()
    )
    return render_template('price.html', price=pricing_books)
