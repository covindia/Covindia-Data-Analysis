import numpy as np
import pandas as pd # pandas
import datetime as dt # module for manipulating dates and times
import scipy.stats as stats
#pip install iso8601
import iso8601
import time
import datetime as dt
import requests


pincodes = pd.read_csv("/content/pinCodeData.csv")
pincodes = pincodes[["City", "Pincode"]]
print(pincodes)

