import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("data/Order_details(masked).csv")


def add_date_column(data, column):
    datetime = pd.to_datetime(data["Transaction Date"])
    data[column] = datetime
    #check_busiest_hours(data,5)
    addapt_data(data)
    

def check_busiest_hours(data,n):
    """WE HAVE TO GET A SUM OF THE NUMBER OF LINES THAT HAS THE SAME HOUR
       IN ORDER TO GET THE BUSIEST HOURS OF THE SHOP"""
    time = data['Time'].dt.hour
    #print("These are the top", n, "busiest hours of the shop\n",time.value_counts()[:n])
    print(time.value_counts()[:n])
    timemost1 = data['Time'].dt.hour.value_counts().index.tolist()[:n]
    timemost2 = data['Time'].dt.hour.value_counts().values.tolist()[:n]
    print(timemost1)
    print(timemost2)
    


def addapt_data(data):
    timemost = data["Time"].dt.hour.value_counts()
    timemost1 = []
    for i in range(0,23):
        timemost1.append(i)

    timemost2 = timemost.sort_index()
    timemost2 = timemost2.tolist()
    timemost2 = pd.DataFrame(timemost2)
    timemost3 = pd.DataFrame(timemost)
    timemost3 = timemost3.sort_index()
    
    draw_data(timemost3)

def draw_data(data):
    """DRAW HOURS WITH MOST SALES"""
    print(data.index.tolist())
    print(data.values.tolist())
    plt.figure(figsize=(20,10))
    plt.title("Sales Happening depending on hour", fontdict={'fontname': 'monospace', 'fontsize' : 30}, y=1.05)
    plt.ylabel("Number of Purchases", fontsize = 18, labelpad =20)
    plt.xlabel("Hour", fontsize = 18, labelpad = 20)
    plt.plot(data.index.tolist(), data.values.tolist(), color = "r")
    plt.grid()
    plt.show()
add_date_column(data, "Time") 