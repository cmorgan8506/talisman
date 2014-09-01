from flask import Blueprint, make_response, render_template, redirect, url_for, g, request
from .. import db
from ..tools.response import static_response
from .forms import RegisterForm, LoginForm
from .models import User


users = Blueprint('users', __name__)


@users.route('/', methods=['GET'])
def index():
    return render_template('users/index.html')


@users.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.form and form.validate():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('.index'))
    return render_template('users/register.html', form=form)
