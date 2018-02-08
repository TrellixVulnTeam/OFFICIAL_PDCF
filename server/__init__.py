from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

migrate = Migrate(app,db)
manager = Manager(app)
manager.add_command('db',MigrateCommand)

mail = Mail(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'general.login_get'


@app.errorhandler(400)
def error400(error):
	print('400 error')
	return render_template('errors/400.html'), 400

@app.errorhandler(404)
def error404(error):
	print('404 error')
	return render_template('errors/404.html'), 404

@app.errorhandler(403)
def error403(error):
	print('403 error')
	return render_template('errors/403.html'), 403


from server.views import general
app.register_blueprint(general.mod)

from server import models
from server.models.users import Users

@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))


