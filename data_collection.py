# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 03:30:58 2020

@author: tahmeed
"""

import glassdoor_scraper as gs
import pandas as pd

path = "C:/Users/tahme/OneDrive/Desktop/ML Projects/Data Science Salary Prediction/chromedriver"

df = gs.get_jobs('data scientist' ,1000, False, path, 15)

df.to_csv('glassdoor_jobs.csv', index = False)