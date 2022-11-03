## Readme

This is the front-end of our APS-internal framework to:

1. Scan the data directories given in config.ini variable `data_dir` and all their subdirectories. If a directory contains files or is empty it will be listed here. Hidden files etc can be excluded with the `exclude` variable in the config file.
2. Build a website based on the scan results that allows to do a keyword search based on the path. In order for this to work well all parameters such as
	* **device name**
	* **student / staff name**
	* **measurement type** should be included in the path!
3. Obtain the paths of the directories in which the data resides and a download link to pull the data onto your local machine for further analysis.


### Naming Conventions

In order to successfully identify your measurement data it has to include keywords - similar to hastags on twitter or instagram.

Please try to include these keywords into the path to your data:

* **person** please stick to using your ETH username as it is unique
* **sample** use the manufacturer's device number e.g. C2M0080120D or another unique identifier
* **measurement technique** dlts, iv, cv, ccd, cl, pl, mcts, microscope, ..
* **detail** or **Readme.txt** a detail might be 'source-drain' for an IV-measurement. Of course best would be to include a Readme.txt in which you describe in a few sentences what was done.

Example paths:

* data/smith/C2M0080120D/iv/drain-source
* data/doe/dlts/Ascatron-150µm-EPI-41
* data/roe/optical-microscope/power2power-s1


### Deployment and Code
For development the server is run in a tmux-session. In order to start it

* Open a tmux session on the server with: `tmux new -s webserver`
* Start the webserver: 
	* local development: `python -m flask --debug --app server run --host=0.0.0.0`
	* on server: `python -m flask --app server run --host=0.0.0.0 --port=80`


The website should then be available at: http:127.0.0.1:5000
You can re-connect to the tmux session using: `tmux attach -t webserver` e.g. if the webserver has crashed to see what has happened.

For the future the code should be deployed through a dedicated webserver such as nginx using uwsgi emperor or similar.


#### Files

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