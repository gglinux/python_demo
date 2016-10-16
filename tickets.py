#! /usr/bin/env python3
#coding=utf-8


""" 火车票

Usage:
	tickets [-gdtkz] <from> <to> <date>

Option:
	-h,--help 现实帮助菜单
	－g		  高铁 
	-d  	  动车
	-t        特快
	-k        普快
	-z        直达
Example:
	tickets beijing shanghai 2016-10-01
"""

from docopt import docopt
from stations import stations

def cli():
	arguments = docopt(__doc__)
	from_station = stations.get(arguments['<from>'])
	to_station = stations.get(arguments['<to>'])
	date = arguments['<date>']
	# 构建URL
	url = 'https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate={}&from_station={}&to_station={}'.format(
        date, from_station, to_station
    )
	# print(__doc__)
	print(arguments)

if __name__ == '__main__':
	cli()