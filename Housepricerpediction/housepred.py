import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import OneHotEncoder


dataset = pd.read_excel("data/HousePricePrediction.xlsx")
#print(dataset.head(5))

def check_objects():
    obj = (dataset.dtypes == 'object')
    
    object_cols = list(obj[obj].index)
    return object_cols

def check_int():
    intlist = (dataset.dtypes == 'int')
    print(intlist)
    int_cols = list(intlist[intlist].index)
    print(int_cols)

def check_floats():
    floatlist = (dataset.dtypes == 'float')
    float_cols = list(floatlist[floatlist].index)
    print(float_cols)

def eda_check():
    """EDA REFERS TO DEEP ANALYSIS SO WE CAN CHECK PATTERNS AND ANOMALIES. ITS IS ESSENTIALS BEFORE INFERENCES
    """
    plt.figure(figsize=(12,6))
    sns.heatmap(dataset.corr(),
                cmap = 'BrBG',
                fmt = ".2f",
                linewidths = 2,
                annot = True)
    plt.show()

def draw_unique_values():
    unique_values = []
    object_cols = check_objects()
    for col in object_cols:
        unique_values.append(dataset[col].unique().size)
    plt.figure(figsize=(10,6))
    plt.title("No.Unique values of Categorical Features")
    plt.xticks(rotation = 90)
    sns.barplot(x = object_cols, y = unique_values)
    plt.show()

def draw_unique_valuecounts():
    
    object_cols = check_objects()
    plt.figure (figsize=(18,36))
    plt.title("Categorical Features")
    plt.xticks(rotation = 90)
    index = 1
    for col in object_cols:
        y = dataset[col].value_counts()
        plt.subplot(11,4,index)
        plt.xticks(rotation = 90)
        sns.barplot(x = list(y.index), y = y)
        index +=1
        plt.show()

"""DATA CLEANING SECTION
   IT'S IMPORTANT TO REMOVE NOT IMPORTANT COLUMNS BEFORE DOING ML TRANING"""
def column_removal():
    """CODE THAT REMOVE A COLUMN FROM DATASET"""
    dataset.drop(['Id'],
                 axis = 1,
                 inplace = True)
    print(dataset.head(5))

def replace_nonvalue_with_mean():
    """REPLACE SalePrice empty values with it's mean to make it more symettric """
    dataset['SalePrice'] = dataset['SalePrice'].fillna(dataset['SalePrice'].mean())
    print(dataset['SalePrice'])

def drop_null_values():
    """DROPPING NULL/VOID VALUES"""
    print(dataset.isnull().sum())
    new_dataset = dataset.dropna()
    new_dataset = new_dataset.isnull().sum()
    return new_dataset

def one_hot_encoder():
    
    s = (dataset.dtypes == 'object')
    new_s = list(s[s].index)
    print("Categorical variables:", new_s)
    print("No of categorical features", len(new_s))
    OH_encoder = OneHotEncoder(handle_unknown = "ignore", sparse_output = False).set_output(transform = "pandas")
    #ohtransform = OH_encoder.fit_transform(dataset[new_s])
    ohtrs = OH_encoder.fit_transform(dataset[["MSZoning"]])
    new_data = pd.concat([dataset, ohtrs], axis = 1).drop(columns = ['MSZoning'])
    print(new_data)

def one_hot_trial():
    d = {'sales': [100000,222000,1000000,522000,111111,222222,1111111,20000,75000,90000,1000000,10000], 
        'city': ['Tampa','Tampa','Orlando','Jacksonville','Miami','Jacksonville','Miami','Miami','Orlando','Orlando','Orlando','Orlando'], 
        'size': ['Small', 'Medium','Large','Large','Small','Medium','Large','Small','Medium','Medium','Medium','Small',]}
    
    ohe = OneHotEncoder(handle_unknown="ignore", sparse_output=False).set_output(transform="pandas")
    ohtrs = ohe.fit_transform(d[['city']])
    print(ohtrs)

"""
check_objects()
check_ints2()
check_floats()
check_int()
eda_check()
draw_unique_values()
draw_unique_valuecounts()
column_removal()
replace_0_with_mean())
drop_null_values()"""
one_hot_encoder()
#one_hot_trial()
 


