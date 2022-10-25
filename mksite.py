'''
Some demonstrator code.
'''

import os
from configobj import ConfigObj
import jinja2


def scandir(dir_name):
    subfolders= [f.path for f in os.scandir(dir_name) if f.is_dir()]
    for dir_name in list(subfolders):
        subfolders.extend(scandir(dir_name))
    return subfolders

def get_uniques(dir_list, prefix):
	uniques = [p for p in dir_list if prefix in p]
	return uniques


def main():
	conf = ConfigObj('config.ini')
	data_dir = conf['General']['data_dir']
	print(f"Searching path: {data_dir}")
	
	dirs = scandir(data_dir)
	print(dirs)
	unique_m = get_uniques(dirs, 'm_iv')
	print(unique_m)


	subs = jinja2.Environment(loader=jinja2.FileSystemLoader('./')
	        ).get_template('template.html').render(title='Example Site', para='All folders measured with IV:', dirs=unique_m)# lets write the substitution to a file
	
	with open('index.html','w') as f: 
		f.write(subs)


if __name__ == '__main__':
	main()