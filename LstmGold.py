# -*- coding: utf-8 -*-
"""
Created on Wed May 10 10:49:06 2017

@author: thera_000
"""

import pandas
import matplotlib.pyplot as plt
dataset = pandas.read_csv('WGC-GOLD_DAILY_INR.csv', usecols=[1], engine='python', skipfooter=3)
plt.plot(dataset)
plt.show()