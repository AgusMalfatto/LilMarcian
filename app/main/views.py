from flask import (
    flash, g, redirect, render_template, request, url_for
)
from . import main_bp
from werkzeug.exceptions import abort
from app.auth.views import login_required
from app.db import get_db

@main_bp.route('/')
@login_required
def index():
    return render_template('index.html')