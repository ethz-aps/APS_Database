##########################################################
##					APS Database Server     			##
##														##
## Authors: dorfer@aps.ethz.ch, 						##
## Date: November 3, 2022								##
## Version: 1											##
##########################################################
#python -m flask --debug --app server run (--host=0.0.0.0)

import os
from pathlib import Path
from configobj import ConfigObj
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask import render_template, redirect
from flaskext.markdown import Markdown


from data_scraping import DataScraping


#load configuration file
conf = ConfigObj('config.ini')

#get DataScraping class object
ds = DataScraping(conf)

#simple class to hold all configuration parameters for the flask server
class Config():
	EXPLAIN_TEMPLATE_LOADING = True
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'vRbPDgZP6rHpjCSQWByy'

app = Flask(__name__)
Markdown(app)
app.config.from_object(Config)

#class for defining search form
class SearchForm(FlaskForm):
	search_terms = StringField("search_terms")
	submit = SubmitField("Submit")



#define the URLs routes for the Website
@app.route("/",methods =['POST','GET'])
def index():
	form = SearchForm()
	if form.validate_on_submit():
		sstring = form.search_terms.data
		if sstring == '':
			dirs = ds.search_results(sterms=[])
			dlink = f"rsync -a --progress <your_username>@{conf['Server']['url']}:/{conf['Data']['data_dir']} ."
		else:
			sterms = sstring.split(',')
			sterms = [s.strip() for s in sterms]
			dirs = ds.search_results(sterms=sterms)

			#generate download link:
			dlink = f"rsync -a --progress <your_username>@{conf['Server']['url']}:"
			for d in dirs:
				dlink += f" :{d}"
			dlink += " ."

		return render_template("index.html", form=form, dirs=dirs, dlink=dlink)
	return render_template("index.html", form=form)


@app.route("/readme")
def readme():
	md_text = Path('Readme.md').read_text()
	return render_template("readme.html", md_text=md_text)


if __name__ == "__main__":
	app.run(debug=True)

