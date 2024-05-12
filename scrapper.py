# -*- coding: utf-8 -*-
"""
Created on Mon May  6 11:34:07 2024

@author: noodl
"""

from bs4 import BeautifulSoup
import requests
import re
#import pandas as pd
#import numpy as np
#from PyInquirer import prompt
#import os
#import signal
#import sys



def get_year_stats():
    #url = 'https://www.iplt20.com/stats/'
    url = 'https://www.nfl.com/stats/player-stats/'
    years = []
    stats_url = []
    stats_title = []
    try:
        page = requests.get(url)
        if page.status_code == 200:
            soup = BeautifulSoup(page.content, 'html.parser')
            years = get_years(soup)
            stats_url, stats_title = get_stats(soup)
            stats_url.append('team-ranking')
            stats_title.append('Team Ranking')
    except requests.exceptions.ConnectionError:
        print('Please check network connection')
        return
    return years, stats_url, stats_title

def get_years(soup):
    divs = soup.find('select', class_='d3-o-dropdown')
    years = []
    
    for div in divs:
        if div != '\n':
            years.append(div.get_text())
    #years[-1] = 'all-time'
    return years

def get_stats(soup):
    stats = soup.find_all('ul', class_='d3-o-tabs d3-o-tabs__nowrap')
    stats_url = []#[re.search(r'\d/(.*)', stat['href']).group(1) for stat in stats]
    stats_raw = [stat.get_text().strip() for stat in stats]
    stats_title = stats_raw[0].split('\n')
    stats_title.remove('')
    print()
    return stats_url, [stat for stat in stats_title if stat != '']

try:
    def main():
        year, stats_url, stats_title = get_year_stats()
except Exception:
    pass

if __name__ == "__main__":
    main()