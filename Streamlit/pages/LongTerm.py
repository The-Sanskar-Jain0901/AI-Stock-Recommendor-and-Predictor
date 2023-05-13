import pandas as pd
import yfinance as yf
import streamlit as st
import datetime

df = pd.read_excel('AICP_LT.xlsx', index_col='Symbol')
df['weights'] = 0

def filterByCapital(df):
    
    x = st.number_input('Enter your capital')
    
    for i in df.index:
        try:

            start_date = datetime.datetime.now()- datetime.timedelta(days=365)
            end_date = datetime.datetime.now()
            stock = yf.download(i + '.NS', start=start_date,
                                end=end_date, interval='1d')
            
            
            
            if float(x) < float(stock['Close'][len(stock)-1]):
                # print(i)
                df.drop(i, inplace=True)

        except Exception as e:
            print(e)
    return df


def filtersector(df):
    
    x = st.text_input('Enter preferred sector/None')
    if(x != 'None'):
        df1 = df[df["Sector"] == x]
    else:
        return df
    return df1

def alpha_beta(df):
    
    df.loc[df['Alpha']<0 , 'weights'] +=0 
    df.loc[df['Alpha']>0 , 'weights'] +=1 
    df.loc[df['Alpha']>1.5, 'weights']+=1 
    df.loc[df['Alpha']>3 , 'weights'] +=1 
    df.loc[df['Alpha']>7 , 'weights'] +=1 

    
    df.loc[df['Beta']<0.5 , 'weights'] +=1 
    df.loc[df['Beta']<1 , 'weights'] +=1 
    df.loc[df['Beta']<1.5, 'weights']+=1 
    df.loc[df['Beta']<2 , 'weights'] +=1 
    df.loc[df['Beta']>2 , 'weights'] +=0 

def Market_Cap(df):
    df.loc[df['Market Cap.']>45000 , 'weights'] +=0
    df.loc[df['Market Cap.']>100000 , 'weights'] +=1 
    df.loc[df['Market Cap.']>300000 , 'weights'] +=1  
    df.loc[df['Market Cap.']>500000 , 'weights'] +=1 

def ROE(df):
    df.loc[df['ROE']>0 , 'weights'] +=0 
    df.loc[df['ROE']>12 , 'weights'] +=1
    df.loc[df['ROE']>15 , 'weights'] +=1 
    df.loc[df['ROE']>25 , 'weights'] +=1 

def NPM(df):
    df.loc[df['Net profit margin']>0 , 'weights'] +=0 
    df.loc[df['Net profit margin']>10 , 'weights'] +=1 
    df.loc[df['Net profit margin']>15 , 'weights'] +=1 
    df.loc[df['Net profit margin']>20 , 'weights'] +=1 


def Current(df):
    df.loc[df['Current ratio']>0 , 'weights'] +=0 
    df.loc[df['Current ratio']>0.5 , 'weights'] +=1 
    df.loc[df['Current ratio']>1 , 'weights'] +=1 
    df.loc[df['Current ratio']>1.5 , 'weights'] +=1 
    df.loc[df['Current ratio']>3 , 'weights'] +=1 

def PE(df):
    df.loc[(df['PE']-df['SectorPE'])>5 , 'weights'] +=0
    df.loc[(df['PE']-df['SectorPE'])<5 , 'weights'] +=0.25
    df.loc[(df['PE']-df['SectorPE'])<0 , 'weights'] +=0.50
    df.loc[(df['PE']-df['SectorPE'])<-5 , 'weights'] +=0.75
    df.loc[(df['PE']-df['SectorPE'])<-10 , 'weights'] +=1

def EBIDTA(df):
    df.loc[df['DiffEBIDTA']<0 , 'weights'] +=0
    df.loc[df['DiffEBIDTA']>0 , 'weights'] +=0.25
    df.loc[df['DiffEBIDTA']>1000 , 'weights'] +=0.5
    df.loc[df['DiffEBIDTA']>2000 , 'weights'] +=0.75
    df.loc[df['DiffEBIDTA']>3500 , 'weights'] +=1

df=filterByCapital(df)
df=filtersector(df)
EBIDTA(df)
alpha_beta(df)
PE(df)
Current(df)
NPM(df)
ROE(df)
Market_Cap(df)
df=df.sort_values(by=['weights'],ascending=False)
st.dataframe(df)










