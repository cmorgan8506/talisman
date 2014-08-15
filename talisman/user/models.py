from datetime import datetime

from flask import Blueprint, render_template
from werkzeug.security import generate_password_hash, check_password_hash

from .. import db


# An association table to create a many-to-many relationship
# between User UserGroup
user_groups = db.Table('user_group_lookup',
    db.Column('id', db.Integer, db.ForeignKey('users.id')),
    db.Column('name', db.String(40), db.ForeignKey('user_groups.name'))
)


class User(db.Model):
    """
    Basic User object to represent website users.
    """
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    created = db.Column(db.DateTime, default=datetime.now())
    password = db.Column(db.String(80), nullable=False)

    groups = db.relationship('UserGroup', secondary=user_groups,
                             backref=db.backref('users', lazy='dynamic'))

    addresses = db.relationship('UserAddress',
        backref=db.backref('user', lazy='joined'), lazy='dynamic')

    # Authentication Methods
    def set_password(self, password_str):
        self.password = generate_password_hash(password_str)

    def check_password(self, password_hash):
        return check_password_hash(self.password, password_hash)


class UserGroup(db.Model):
    """
    UserGroup is used to represent the various types
    of User permissions that are available. A UserGroup
    can have any number of Users, which is handled through
    an associative table.
    """
    __tablename__ = "user_groups"

    name = db.Column(db.String(40), primary_key=True)


class UserProfile(db.Model):
    """
    Provides a basic user profile, to collect common information
    that all users will be required to include.
    """
    __tablename__ = 'user_profiles'

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(40), nullable=False)
    phone_primary = db.Column(db.String(11), nullable=False)
    phone_secondary = db.Column(db.String(11), nullable=True)


class UserAddress(db.Model):
    """
    Represents a user address, that can be used for either
    shipping, or billing.
    """
    __tablename__ = 'user_addresses'

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    address_1 = db.Column(db.String(80), nullable=False)
    address_2 = db.Column(db.String(80), nullable=True)
    code = db.Column(db.String(10), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    province = db.Column(db.String(100), nullable=False)
