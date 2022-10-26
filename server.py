#python -m flask --debug --app server run (--host=0.0.0.0)
import os
from configobj import ConfigObj
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask import render_template, redirect

conf = ConfigObj('config.ini')


class DataScraping():
	def __init__(self, conf):
		self.conf = conf
		self.ddir = self.conf['Data']['data_dir']


	def scandir(self, dir_name):
		subfolders = [f.path for f in os.scandir(dir_name) if f.is_dir()]
		for dir_name in list(subfolders):
			subfolders.extend(self.scandir(dir_name))
		return subfolders


	def search_results(self, sstrings):
		dirs = self.scandir(self.ddir) #get all folders and subfolders
		print(dirs)

		if len(sstrings) == 0: #no search term - return all data
			return dirs

		dirs = [d for d in dirs if all(s in d for s in sstrings)]
		return dirs

ds = DataScraping(conf)




class Config():
	EXPLAIN_TEMPLATE_LOADING = True
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'vRbPDgZP6rHpjCSQWByy'

app = Flask(__name__)
app.config.from_object(Config)

class SearchForm(FlaskForm):
	search_terms = StringField("search_terms")
	submit = SubmitField("Submit")



@app.route("/",methods =['POST','GET'])
def main():
	form = SearchForm()
	if form.validate_on_submit():
		sstring = form.search_terms.data
		print('Search strings: ', sstring)
		if sstring == '':
			dirs = ds.search_results(sstrings=[])
		else:
			sstrings = sstring.split(',')
			sstrings = [s.strip() for s in sstrings]
			dirs = ds.search_results(sstrings=sstrings)
			
		return render_template("index.html", form=form, dirs=dirs)
	return render_template("index.html", form=form)


if __name__ == "__main__":
	app.run(debug=True)
