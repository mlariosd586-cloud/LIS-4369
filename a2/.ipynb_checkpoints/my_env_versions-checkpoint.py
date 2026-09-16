import sys
import jupyterlab
import pandas as pd
import pandas_datareader
import numpy as np
import matplotlib
import sklearn
import django
import seaborn as sns
import openpyxl
import nltk
import statsmodels
import scipy
import cv2
import yfinance as yf

print("Python version:")
print(sys.version)
print("jupyterlab:", jupyterlab.__version__)
print("pandas:", pd.__version__)
print("pandas_datareader:", pandas_datareader.__version__)
print("numpy:", np.__version__)
print("matplotlib:", matplotlib.__version__)
print("sklearn:", sklearn.__version__)
print("django:", django.__version__)
print("seaborn:", sns.__version__)
print("openpyxl:", openpyxl.__version__)
print("nltk:", nltk.__version__)
print("statsmodels:", statsmodels.__version__)
print("scipy:", scipy.__version__)
print("cv2 (opencv-python):", cv2.__version__)
print("yfinance:", yf.__version__)