# MkSite Documentation

**MkSite** is our APS-internal framework to:

1. Scan the data directories given in config.ini variable `data` and all their subdirectories
2. Build a website based on the scan results that allows to do a keyword search based on:
	* device name
	* student / staff name
	* measurement type
3. Obtain the paths of the directories in which the data resides


## How it works
The python code in `mksite.py` recursively scans all directories given in `data` in the config file. Information about the device, the person that measured it and the measurement type is encoded in the path and extracted from there.

Example paths:

* `data`/p\_smith/s\_C2M0080120D/m\_iv/d\_drain-source
* `data`/p\_doe/m\_dlts/s\_Ascatron-150µm-EPI-41
* `data`/p\_roe/m\_optical-microscope/s\_power2power-s1

As it can be guessed from the examples above the convention is:

* **p\_**\<person\> to denote who did the measurement
* **s\_**\<sample\> to specify the sample
* **m\_**\<measurement technique\> to describe how the sample was measured
* **d\_**\<details\> to add some details that might be interesting - however, ideally a Readme.txt is placed in the directory containing the data that better describes the measurements or points to a place where this is described.

Because people often remember who has worked on something but not what it was precisely it is often helpful to have the person specified who did the measurements with the **p\_** keyword - however this is not absolutely necessary.


### Standardized Keywords

* **m\_**\<measurement technique\> : dlts, iv, cv, ccd, cl, pl, mcts, .. (add further)
* **s\_**\<sample\> : Use the manufacturer's device number e.g. C2M0080120D


## Server-Side

**Work to do:** 

Possible solutions:


