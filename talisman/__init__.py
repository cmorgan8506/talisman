from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug.contrib.fixers import ProxyFix


def create_app(config_filename, db):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    app.wsgi_app = ProxyFix(app.wsgi_app)
    db.init_app(app)
    # Register blueprints
    #from talisman.user.views import users
    #app.register_blueprint(users)
    return app


# Boostrap Flask App
db = SQLAlchemy()
app = create_app('talisman.config', db)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')

if __name__ == '__main__':
    app.run()
