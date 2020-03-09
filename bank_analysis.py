## load libraries-----
import pandas as pd

import rpy2.robjects as robjects
from rpy2.robjects import pandas2ri
pandas2ri.activate()
import urllib
import numpy as np
import tensorflow as tf
from tensorflow import keras
import scipy as sc
from scipy import stats
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt

import os
cwd = os.getcwd()
print(cwd)

## location of data-------

url = "https://github.com/Matt-Brigida/FFIEC_Call_Reports/raw/master/1_querying_data_and_analysis/analyses/panel_data_analysis/full_panel/1_panel_with_full_quarter_date/1_one_panel_all_models/full_panel.rds?raw=true"

### download data and save to working directory-----
urllib.request.urlretrieve(url, "./panel.rds")

## read in data
readRDS = robjects.r['readRDS']
df = readRDS("panel.rds")

df = df[["IDRSSD", "quarter", "totSBloans_Delt", "t1_LR_lagged_1_year", "tot_SB_loans_TA_lagged_1", "ROA_lagged_1", "NPA_TA_lagged_1", "total_assets_lagged_1_year", "TD_TA_lagged_1", "african_am_ind", "hispanic_ind", "de_novo", "TETA_lagged_1_year", "post_crisis_ind", "fin_crisis_ind"]]


### Questions:
## what are the summary statistics for De Novo vs non-De Novo banks?
## what are the summary statistics for banks pre-financial crisis, during the financial crisis, and lastly post-crisis?
## what are summary statistics for Minority owned institutions?
