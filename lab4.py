# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 13:17:49 2017

@author: ap9g17
"""

import re
import urllib


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
            numbers = line.strip().split(',')
            numbers = list(map(float, numbers))
            avg = 0
            for n in numbers:
                avg += n
            avg = avg / len(numbers)
            avgs.append(avg)
        f.close()
        return avgs


def noaa_temperature(s):
    """extract the temperature in degree Celsius from the string,
    and return this temperature as an integer number"""
    temp_strs = re.findall(
        r'(?<=Temperature:\s[0-9]{2}\s\w\s\()((-)?[0-9]+)', s.strip())[0]
    if (len(temp_strs) > 0 and len(temp_strs[0]) > 0):
        return int(temp_strs[0])
    else:
        return []


def seq_sqrt(xs):
    """ takes a list of non-negative numbers xs with elements
    [x0, x1, x2, ..., xn], and returns the list
    [sqrt(x0), sqrt(x1), sqrt(x2), ..., sqrt(xn)]"""
    return [x ** 0.5 for x in xs]


def mean(xs):
    """takes a sequence xs of numbers, and returns the (arithmetic) mean """
    return sum(xs) / len(xs)


def wc(filename):
    """returns the number of words in file filename"""
    with open(filename, 'rt') as f:
        words = re.findall('(\w+)', f.read())
        f.close()
        return len(words)
