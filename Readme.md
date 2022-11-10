## Readme

This is the front-end of our APS-internal framework to:

1. Scan the data directories given in config.ini variable `data_dir` and all their subdirectories. If a directory contains files or is empty it will be listed, else not. Selected files etc can be excluded with the `exclude` variable in the config file.
2. Generate a website based on the content of the data directory that allows to do a keyword-based search. In order for this to work well all parameters such as
	* **device name**
	* **student / staff name**
	* **measurement type** should encoded in the path of the file (i.e. give your folder/file a useful name (see naming conventions below)
3. Obtain the paths of the directories in which the data resides and a download link to pull the data onto your local machine for further analysis.


### Naming conventions

In order to successfully identify your measurement data it has to include keywords - similar to hastags on twitter or instagram.

Please try to include these keywords into the path to your data:

* **person** please stick to using your ETH username as it is unique
* **sample** use the manufacturer's device number e.g. C2M0080120D or another unique identifier
* **measurement technique** dlts, iv, cv, ccd, cl, pl, mcts, microscope, ..
* **detail** or **Readme.txt** a detail might be 'source-drain' for an IV-measurement. Of course best would be to include a Readme.txt in which you describe in a few sentences what was done and even put your analysis code there, so that other people can reproduce the results.

Example paths:

* data/smith/C2M0080120D/iv/drain-source
* data/doe/dlts/Ascatron-150µm-EPI-41
* data/roe/optical-microscope/power2power-s1


### How to locally run the development version of the webserver
A development version of the webserver can be run on your local machine.

* First, install the necessary python packages with:

`pip install -r requirements.txt`

* Start the webserver for local development:

`python -m flask --debug --app server run --host=0.0.0.0`

The website should then be available at: http:127.0.0.1:5000

On the APS webserver reachable at data.aps.ee.ethz.ch the code is deployed through a dedicated webserver (nginx) in combination with uwsgi.

### Understand the deployment on the webserver
If you have never done this you might struggle a bit, but the learning curve is steep.
For easier reproducability I have followed [this article](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uswgi-and-nginx-on-ubuntu-18-04) on how to employ our flask application with uWSGI and Nginx.

The corresponding config files can be found in the folder server_config.

In addition the website is secured with a basic http authentication. Details on how this was setup here [here](https://docs.nginx.com/nginx/admin-guide/security-controls/configuring-http-basic-authentication/). You can find the user/PW in our Wiki (Guide to the APS servers).

#### The flask webserver python files

The (small) framework consists of several files and folders:

* *config.ini*: The configuration file in which the data directory as well as keywords to exclude are listed.
* *data_scraping.py*: Holds the code to scan the given data directory and to return a list of files that comply with the requirements we have set.
* *server.py*: Renders the website with flask.
* *static*-folder: Stores static files such as logos.
* *templates*-folder: Stores the html templates for rendering the website.
* *data*-folder: This is where the data resides.

Upon pressing the search button the data-folder is searched for all files that match the search terms. If no search terms were given all files are returned.

#### Contact Persons

<medeiros@aps.ee.ethz.ch>,
<dorfer@aps.ee.ethz.ch>


apsdatabase!