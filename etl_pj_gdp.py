import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3
import numpy as np
from datetime import datetime

url = 'https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29'
table_attributes = ['Country','GDP(USD_Millions)']
dbName = 'economy.db'
tableName = 'Countries_GDP'
csvPath = 'Countries_GDP.csv'


def extract(url, table_attributes):
    ''' This function extracts the required
    information from the website and saves it to a dataframe. The
    function returns the dataframe for further processing. '''
    # create empty dataframe
    df = pd.DataFrame(columns = table_attributes)
    
    # fetch 3rd table's required contents
    htmlContent = requests.get(url).text
    soup = BeautifulSoup(htmlContent,'html.parser')
    html_elements = soup.find_all('tbody')
    target_table = html_elements[2]
    rows = target_table.find_all('tr')
    for row in rows:
        columns = row.find_all('td')
        if len(columns)!=0:
            if columns[0].find('a') is not None and '—' not in columns[2]:
                data_dict = {"Country": columns[0].a.contents[0],
                             "GDP(USD_Millions)": columns[2].contents[0]}
                df1 = pd.DataFrame(data_dict, index=[0])
                df = pd.concat([df,df1], ignore_index=True)
    return df

def transform(df):
    ''' This function converts the GDP information from Currency
    format to float value, transforms the information of GDP from
    USD (Millions) to USD (Billions) rounding to 2 decimal places.
    The function returns the transformed dataframe.'''

    return df

def load_to_csv(df, csv_path):
    ''' This function saves the final dataframe as a `CSV` file 
    in the provided path. Function returns nothing.'''

def load_to_db(df, sql_connection, table_name):
    ''' This function saves the final dataframe as a database table
    with the provided name. Function returns nothing.'''

def run_query(query_statement, sql_connection):
    ''' This function runs the stated query on the database table and
    prints the output on the terminal. Function returns nothing. '''

def log_progress(message):
    ''' This function logs the mentioned message at a given stage of the code execution to a log file. Function returns nothing'''

''' Here, you define the required entities and call the relevant 
functions in the correct order to complete the project. Note that this
portion is not inside any function.'''

df = extract(url, table_attributes)
print(df)