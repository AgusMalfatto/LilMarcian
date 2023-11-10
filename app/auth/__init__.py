import functools
from flask import(
    Blueprint, flash, g, redirect, render_template, request, url_for, session, redirect
)

# Creacion de Blueprint
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

from . import views
