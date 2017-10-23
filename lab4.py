# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 13:17:49 2017

@author: ap9g17
"""

import urllib
import re


# Provided
def noaa_string():
    url = "http://tgftp.nws.noaa.gov/data/observations/metar/decoded/EGHI.TXT"
    noaa_data_string = urllib.request.urlopen(url).read()
    return noaa_data_string.decode("utf-8")


def line_averages(filename):
    """compute the average value for every line, and
    return the average values in a list"""
    with open(filename, 'rt') as f:
        avgs = []
        for line in f:
            numbers = line.split(',')
            numbers = list(map(int, numbers))
            avg = 0
            for n in numbers:
                avg += n
            avg = avg/len(numbers)
            avgs.append(avg)
        return avgs


def noaa_temperature(s):
    """extract the temperature in degree Celsius from the string, 
    and return this temperature as an integer number"""
    temp_str = re.findall('((\d){2}(?= C))', s)[0]
    return int(temp_str[0])


def seq_sqrt(xs):
    pass


def mean(xs):
    pass


def wc(filename):
    pass
