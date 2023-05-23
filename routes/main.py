from flask import Blueprint, render_template
from extensions import db  # Importing from extensions module
from flask import Flask, render_template, flash, redirect, url_for, request, Blueprint
from flask_login import login_required, current_user
from .forms import CreateCourseForm
from .forms import CreateCategoryForm
from models.course import Course
from models.category import Category


main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')


@main.route('/create_course', methods=['GET', 'POST'])
@login_required
def create_course():
    form = CreateCourseForm()
    if form.validate_on_submit():
        category = Category.query.filter_by(name=form.category.data).first()
        if not category:
            category = Category(name=form.category.data)
            db.session.add(category)
            db.session.commit()

        course = Course(name=form.title.data, description=form.description.data, 
                        price=form.price.data, category_id=category.id,
                        teacher_id=current_user.id)
        db.session.add(course)
        db.session.commit()
        flash('Your course has been created!', 'success')
        return redirect(url_for('main.dashboard'))
    return render_template('createCourse.html', title='Create Course', form=form)

@main.route('/create-category', methods=['GET', 'POST'])
@login_required
def create_category():
    if current_user.role != 'Teacher':
        flash('You are not authorized to access this page.')
        return redirect(url_for('main.index'))

    form = CreateCategoryForm()

    if form.validate_on_submit():
        new_category = Category(name=form.name.data)
        db.session.add(new_category)
        db.session.commit()

        flash('Category successfully created.')
        return redirect(url_for('main.dashboard'))

    return render_template('createCategory.html', form=form)


@main.route('/dashboard')
@login_required
def dashboard():
    if current_user.role != 'Teacher':
        flash('You are not authorized to access this page.')
        return redirect(url_for('main.index'))

    courses = Course.query.filter_by(teacher_id=current_user.id).all()
    return render_template('dashboard.html', courses=courses)

@main.route('/course/<int:course_id>')
@login_required
def display_course(course_id):
    course = Course.query.get_or_404(course_id)
    if current_user.id != course.teacher_id:
        flash('You are not authorized to access this page.')
        return redirect(url_for('main.index'))
    return render_template('course.html', course=course)


