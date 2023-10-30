import functools
from flask import(
    Blueprint, flash, g, redirect, render_template, request, url_for, session, redirect
)

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

from . import views
