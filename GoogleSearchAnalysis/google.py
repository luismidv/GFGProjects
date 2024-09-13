import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt

trend = TrendReq(hl = 'en-US', tz = 360)
kw_list = ['Cloud Computing']
trend.build_payload(kw_list, cat = 0, timeframe = 'today 12-m')

def interest_over_time():
    data = trend.interest_over_time()
    data.sort_values(by = "Cloud Computing", ascending = False)
    print(data.head(10))

def historical_hour_interest():
    data = trend.get_historical_interest(
        kw_list, year_start = 2018, month_start = 1, day_start = 1,
        hour_start = 0, year_end=2018, month_end = 2, day_end = 2,
        hour_end = 0, cat = 0, gprop = '', sleep=0)
    data.sort_values(by = 'Cloud computing', ascending = False)
    print(data.head(10))

def interest_by_region():
    data = trend.interest_by_region()
    data = data.sort_values(by='Cloud Computing', ascending = False)
    data = data.head(10)
    
    watch_with_charts(data)

def watch_with_charts(data):
    data.reset_index().plot(x = 'geoName', y = 'Cloud Computing',
                            figsize =(10,5), kind='bar')
    plt.style.use('fivethirtyeight')
    plt.show()

def top_charts():
    data = trend.top_charts(2020,hl='en-US',
                            tz = 300, geo = 'GLOBAL')
    data.head(10)
    print(data)

def related_queries():
    trend.build_payload(kw_list = ['Cloud Computing'])
    print(trend.related_queries())

def topic_suggestions():
    keywords = trend.suggestions(
        keyword = "Cloud Computing"
    )
    data = pd.DataFrame(keywords)
    
    print(data.drop(columns = "mid"))
    

#historical_hour_interest()
"""
interest_by_region()
top_charts() 
related_queries()"""
topic_suggestions()

 


