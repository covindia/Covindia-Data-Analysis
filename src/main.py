import numpy as np
import pandas as pd # pandas
import datetime as dt # module for manipulating dates and times
import scipy.stats as stats
#pip install iso8601
import iso8601
import time
import datetime as dt
import requests
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

pincodes = pd.read_csv("/content/pinCodeData.csv")
pincodes = pincodes[["City", "Pincode"]]
print(pincodes)

def scrape_weather(from_date,to_date):
    
    weather = pd.DataFrame(columns=['precip', 'snowfall', 
    'temp', 'timestamp', 'datetime'])

    # Loop through all days of interest and obtain hourly 
    i = 0

    weather
    for cities, pins in pincodes[["City", "Pincode"]].itertuples(index=False):
        print(cities)
        url = "https://api.weathersource.com/v1//postal_codes/" + str(pins)+ ",IN/history.json?period=day&timestamp_between=" + from_date + "T00:00," + to_date + "T00:00&fields=allTemp,allHum" 
        response = requests.get(url).json()
        df = pd.DataFrame(response)
        df['datetime'] = [iso8601.parse_date(hour['timestamp']) for hour in response]
        #NaN = np.nan
        #city = pd.DataFrame([[cities]])
        weather = weather.append(df,ignore_index=True)
        weather = weather.append(pd.DataFrame([[cities]]), ignore_index=True)#pincodes.loc[i,['City']],ignore_index=True)
        i = i+1
        time.sleep(6.1)
    #print(weather)
    #weather.reset_index(inplace=True)
    #weather.drop('index', axis=1, inplace=True)

    return weather
if __name__ == "__main__":
  weatherlon = scrape_weather("2020,3,13","2020,4,3"))
  weatherlon.head()
  weatherlon.to_csv('weatherdata.csv', index = False)
