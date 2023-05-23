from . import main
from extensions import db  # Importing from extensions module
from flask import Flask, render_template, flash, redirect, url_for, request, Blueprint
from flask_login import login_required, current_user
from models.course import Course
from models.category import Category
from .forms import CreateCourseForm
from .forms import CreateCategoryForm



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

        course = Course(title=form.title.data, description=form.description.data, 
                        price=form.price.data, category_id=category.id,
                        teacher_id=current_user.id)
        db.session.add(course)
        db.session.commit()
        flash('Your course has been created!', 'success')
        return redirect(url_for('main.index'))
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
        return redirect(url_for('main.create_course'))

    return render_template('createCategory.html', form=form)