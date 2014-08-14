from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug.contrib.fixers import ProxyFix


# Boostrap Flask App
app = Flask(__name__)
db = SQLAlchemy(app)
app.config.from_object('talisman.config')
app.wsgi_app = ProxyFix(app.wsgi_app)

# Register blueprints
from talisman.user.views import users
app.register_blueprint(users)



@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')

if __name__ == '__main__':
    app.run()
