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
    
#######################################################################################    
    
def getNationalData():
    cities = ['Ahmadabad', 'Bangalore', 'Chennai', 'Delhi', 'Hyderabad', 'Jaipur', 'Mumbai', 'Thane', 'Indore', 'Jodhpur','Pune', 'Kasaragod']
    dtsetsuffix = {'date':'datetime','dwpt':'dewPtAvg10','relhum':'relHumAvg10','shum':'spcHumAvg10','temp':'tempAvg10'}
    for type in dtsetsuffix:
        df = pd.read_csv('weatherdataman___prepared-'+type+'.csv')
        var = dtsetsuffix[type]
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
        plt.xlabel(dtsetsuffix[type])
        plt.ylabel("Percentage change in reported cases: ")
        plt.xticks(rotation='vertical')
        plt.savefig("/content/nationalGraphs/"+dtsetsuffix[type]+ ".png")#regionalGraphs
        plt.show()
        
#######################################################################################


def getCityData():    
    cities = ['Ahmadabad', 'Bangalore', 'Chennai', 'Delhi', 'Hyderabad', 'Jaipur', 'Mumbai', 'Thane', 'Indore', 'Jodhpur','Pune', 'Kasaragod']
    dtsetsuffix = {'date':'datetime','dwpt':'dewPtAvg10','relhum':'relHumAvg10','shum':'spcHumAvg10','temp':'tempAvg10'}
    for type in dtsetsuffix:
        var = dtsetsuffix[type]
        for city in cities:
            df = pd.read_csv('weatherdataman___prepared-'+type+'.csv')
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
            plt.xlabel(dtsetsuffix[type]+' of '+city)
            plt.ylabel("Percentage change in reported cases in "+ city + ": ")
            plt.xticks(rotation='vertical')
            plt.savefig("/content/districtGraphs/"+city+dtsetsuffix[type]+ ".png")#regionalGraphs
            plt.show()
            
#######################################################################################

if __name__ == "__main__":
    getNationalData()
    getCityData()
    getSpecific("Bangalore")
