#!/usr/bin/python
# coding: utf8
import urllib
from zipfile import *
from subprocess import call
import csv
import sys
import unicodecsv
import os

suffixes = ['US']
csv.field_size_limit(10000000000)

def geonames2SHP():
    for suffixe in suffixes:
        url = 'http://download.geonames.org/export/dump/'+suffixe+'.zip'
        urllib.urlretrieve(url, '/Users/juanlozano/Documents/geonames'+suffixe+'.zip')
        f = '/Users/juanlozano/Documents/geonames'+suffixe+'.zip'
        zipfile = ZipFile(f)
        zipfile.extractall('/Users/juanlozano/Documents/geonames')
        f = '/Users/juanlozano/Documents/geonames/'+suffixe+'.txt'
        call(['geonames', f])
geonames2SHP()
