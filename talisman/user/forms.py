from wtforms import Form, validators, PasswordField, TextField, ValidationError
from .models import User


class LoginForm(Form):
    email = TextField('Email Address', [validators.Length(min=6, max=50),
                                        validators.Email(),
                                        validators.Required()])
    password = PasswordField('Password', [validators.Length(min=6, max=30),
                                          validators.Required()])


class RegisterForm(Form):
    email = TextField('Email Address', [validators.Length(min=6, max=50),
                                        validators.Email(),
                                        validators.Required()])
    password = PasswordField('Password', [validators.Length(min=6, max=30),
                                          validators.Required()])
    confirm = PasswordField('Confirm Password', [validators.Length(min=6, max=30),
                                                 validators.Required()])
    username = TextField('Confirm Password', [validators.Length(min=4, max=35),
                                              validators.Required()])

    def validate_email(form, field):
        user = User.query.filter_by(email=field.data).first()
        if user:
            raise ValidationError('Email is already in use')

    def validate_username(form, field):
        user = User.query.filter_by(username=field.data).first()
        if user:
            raise ValidationError('Username is already in use')

    def validate_confirm(form, field):
        if field.data != form.password.data:
            raise ValidationError("Passwords do not match")
