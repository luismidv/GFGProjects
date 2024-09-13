import pandas as pd 
import numpy as np


def year_create():
    dates = pd.date_range(start = "1/1/2010", end= "1/1/2021", periods = 100)
    years = dates.year
    
    shares =(np.random.randint(1425504460, 1425599999, 100))
    trades =(np.random.randint(4000000, 5000000, 100))
    dollars =(np.random.randint(30000000,50000000,100))
    
    new_frame = pd.DataFrame()
    new_frame["years"] = years
    new_frame["date"] = dates
    new_frame["shares"] = shares
    new_frame["trades"] = trades
    new_frame["dollars"] = dollars

    new_frame.to_csv('out.csv', index = False)

    print(new_frame.head(5))
    
    

def crea_csv():
    new_frame  = pd.read_csv('out.csv')
    print(type(new_frame["shares"]))

crea_csv()