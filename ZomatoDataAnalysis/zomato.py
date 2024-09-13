import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.read_csv('data/Zomatodata.csv')
#print(data)

def convert_float_rdenomin(value):
    """FUNCTION THAT CONVERTS A NUMBER TO FLOAT AND REMOVES IT'S DENOMINATOR"""
    value = str(data["rate"])
    list = value.split("/")
    return list[0]

def convert_float_myform(value):
    """FUNCTION THAT CONVERTS A NUMBER TO FLOAT AND REMOVES IT'S DENOMINATOR"""
    value = str(data["rate"])
    list = value.split("/")
    return list[0]

def show_type_restaurants():
    """SHOWING NUMBERS OF RESTAURANTS BY TYPE"""
    sns.countplot(x = data['listed_in(type)'])
    plt.xlabel("Type of restaurant")
    plt.show()

def watch_type_votes():
    """SHOWING VOTES OF EACH TYPE"""
    grouped_data = data.groupby('listed_in(type)')['votes'].sum()
    print(grouped_data)
    plt.plot(grouped_data, c= "red", marker = "o")
    plt.show()
    #result = pd.DataFrame({'votes': grouped_data})

def show_max_and_name():
    """SHOW MAX AND MIN VOTES AND FIND RESTURANT NAME WITH MAX VOTES"""
    max = data['votes'].max()
    print(max)
    max = data['votes'].min()
    print(min)
    print("Showing restaurant with max votes")
    restaurant_max = data.loc[data['votes'] == max,'name']
    print(restaurant_max)
    
def show_online_orders():
    """SHOW RESTURANT WITH ONLINE POSSIBILITIES"""
    sns.countplot(data['online_order'])
    plt.xlabel("Resturant with online orders")
    plt.show()

def show_online_orders_name():
    """SHOW RESTAURANT'S NAME THAT ALLOWS ONLINE ORDERS"""
    online_orders = data.loc[data['online_order'] == 'Yes', 'name']
    no_online_orders = data.loc[data['online_order']== 'No', 'name']
    print("Resturants with online order", online_orders)
    print("Resturants without online order",no_online_orders)
    
def show_rate_column_info():
    """FIRST LET'S SHOW EACH RESTAURANT VOTES"""
    """LET'S SHOW VOTE'S COUNTPLOT"""
    print(data['votes'] >= 5)
    x = data['votes'].tail(5)
    sns.countplot(y = x)
    plt.show()

def show_rate_column_condition():
    """LET'S SHOW RESTAURANT WITH MORE THAN 500 VOTES"""
    restaurants = data.loc[data['votes'] >= 500, ['name', 'votes', 'rate', 'online_order']]
    print(restaurants)

def approx_cost_explore():
    """EXPLORING APPROX COST DATA, WATCH RESTAURANT WITH < 400 COST"""
    couple_data = data['approx_cost(for two people)']
    print(couple_data)
    new_couple_data = data.loc[data['approx_cost(for two people)'] <= 400, 'approx_cost(for two people)']
    print(new_couple_data)
    sns.countplot(x = new_couple_data)
    plt.show()

def online_info():
    """WATCHING RATINGS WHEN WE HAVE ONLINE AND OFFLINE ORDERS"""
    sns.boxplot(x = data['online_order'], y =data['rate'] )
    plt.show()

def pivot_table_info():
    """DRAWS A PIVOT TABLE COMPARING RESTAURANTS SIZE TAKING INTO ACCOUNT ONLINE ORDER AND TYPE OF RESTAURANT"""
    pivot_table = data.pivot_table(index = 'listed_in(type)', columns = 'online_order', aggfunc='size', fill_value=0)
    sns.heatmap(pivot_table, annot= True, cmap="YlGnBu", fmt = "d")
    plt.title("Pivot_table")
    plt.xlabel("Online order")
    plt.ylabel("Type")
    plt.show()

"""
print(data.head())
data["rate"] = convert_float_myform(data["rate"])
print(data.head())
print(data.info())
show_type_restaurants()
watch_type_votes()
show_max_and_name()
show_online_orders()"""
show_online_orders_name()
#show_rate_column_info()
#show_rate_column_condition()
#approx_cost_explore()
#online_info()
#pivot_table_info()
