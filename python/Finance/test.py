import numpy as ny
import pandas as pd
import matplotlib.pyplot as plt


dfNifty=pd.read_csv("data.csv",index_col="Date",parse_dates=True,usecols=["Date","High"])
dfTcs=pd.read_csv("TCS.csv",index_col="Date",parse_dates=True,usecols=["Date","High Price"])
dfInfy=pd.read_csv("infy.csv",index_col="Date",parse_dates=True,usecols=["Date","High Price"])


dfTcs=dfTcs.rename(columns={"High Price":"TCS"})


dfInfy=dfInfy.rename(columns={"High Price":"INFY"})


dfNifty=dfNifty.rename(columns={"High":"Nifty"})



dfTcs=dfTcs.join(dfInfy).join(dfNifty)


dfTcs=dfTcs/dfTcs.ix[1,:]

r_mean=pd.rolling_mean(dfTcs["TCS"],window=20)
r_std=pd.rolling_std(dfTcs["TCS"],window=20)

#bollinger bands
r_mean_plus=r_mean+r_std*2
r_mean_minus=r_mean-r_std*2

#daily returns

daily_returns=dfTcs.copy()
daily_returns["TCS"][1:]=(dfTcs["TCS"][1:]/dfTcs["TCS"][:-1].values)-1

daily_returns.ix[0,:]=0



ax=dfTcs.plot()
ax=r_mean.plot(label="Rolling mean",ax=ax)
ax=r_mean_plus.plot(label="Rolling mean",ax=ax)
ax=r_mean_minus.plot(label="Rolling mean",ax=ax)
ax=daily_returns["TCS"].plot(label="daily returns",ax=ax)


plt.show()
    
