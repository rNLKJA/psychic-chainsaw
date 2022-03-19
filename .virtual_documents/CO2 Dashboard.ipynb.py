# import required libraries
import pandas as pd
import numpy as np

import hvplot


import imp
imp.find_module('pandas')


import panel as pn
pn.extension()


get_ipython().getoutput("jupyter kernelspec list --json")


import matplotlib.pyplot as plt


get_ipython().getoutput("/usr/local/opt/python@3.9/bin/python3.9 -m pip install --upgrade pip")


# request the data
data = pd.read_csv('https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv')


# inspect the data
data.tail(5)


# display summary information
data.describe()



