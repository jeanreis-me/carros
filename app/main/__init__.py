from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('routes', __name__, template_folder='templates')

from . import routes