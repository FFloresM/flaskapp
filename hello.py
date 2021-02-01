from flask import Flask, render_template, url_for, json
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from forms.forms import NameForm
from datetime import datetime
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = 'afobklsgsheknfrljnengliejbvnlirsbgvirhgbdr'
bootstrap = Bootstrap(app)
moment = Moment(app)


@app.route('/')
def index():
	SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
	json_url = os.path.join(SITE_ROOT, 'static/data', 'data.json')
	data = json.load(open(json_url))
	return render_template(
				'index.html',
				data=data
				)

@app.route('/user/<name>')
def user(name):
	return render_template('user.html', name=name)


		


#errors handlers
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'), 500

if __name__ == '__main__':
	app.run(debug=True)