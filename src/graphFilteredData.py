import pandas as pd 
from scipy.ndimage.filters import gaussian_filter1d
import numpy as np
%matplotlib inline
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure

def getSpecific(city):
    df = pd.read_csv('weatherdataman___prepared-temp.csv')
    var = 'tempAvg10'
    df = df[df['City']==city]
    df["datetime"] = pd.to_datetime(df["datetime"])#,dayfirst=True)
    from scipy.ndimage.filters import gaussian_filter1d
    import numpy as np
    %matplotlib inline
    from matplotlib import pyplot as plt
    from matplotlib.pyplot import figure
    figure(num=None, figsize=(25, 15), dpi=80, facecolor='w', edgecolor='k')
    ysmoothed = gaussian_filter1d(np.array(df['pChange']), sigma=1.5)
    plt.plot(np.array(df[var]), ysmoothed, color='orange')
    plt.plot(df[var], df['pChange'])
    plt.xticks(rotation='vertical')
    plt.show()
