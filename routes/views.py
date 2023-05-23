from . import main
from extensions import db  # Importing from extensions module
from flask import Flask, render_template, flash, redirect, url_for, request, Blueprint
from flask_login import login_required, current_user
from models.course import Course
from models.category import Category
from .forms import CreateCourseForm
from .forms import CreateCategoryForm








