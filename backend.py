import pandas as pd
df = pd.read_excel('AICP.xlsx')
df['weights'] = 0



def shortTermAnalysis(df):
    print('short term')

def midTermAnalysis(df):
    print('mid  term')

def longTermAnalysis(df):
    print('long term')


# 1.High Alpha
# alpha -  -ve (0)
# 0 to 1.5 (1)
# 1.5 to 3 (2)
# 3 to 7 (3)
# 7 to infinity (4)

#  2.Low Beta
# 0 to 0.5 (4)
# 0.5 to 1 (3)
# 1 to 1.5 (2)
# 1.5 to 2 (1)
# 2 to infinity(0)


# 3.Market Cap
# 45-1
# 1-3
# 3-5
# 5-15


#4. ROE
# 0-12
# 12-15
# 15-25
# 25-50

# 4.	Net profit margin>10
# 7.	Debt to equity ratio<1
# 8.	Current ratio


def alpha_beta(df):
    # alpha
    df.loc[df['Alpha']<0 , 'weights'] +=0 
    df.loc[df['Alpha']>0 , 'weights'] +=1 
    df.loc[df['Alpha']>1.5, 'weights']+=1 
    df.loc[df['Alpha']>3 , 'weights'] +=1 
    df.loc[df['Alpha']>7 , 'weights'] +=1 

    # beta
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


PE(df)
alpha_beta(df)
Current(df)
NPM(df)
ROE(df)
Market_Cap(df)

print(df)

def filterByCapital(df):
    for i in df.Symbol:
        try:

            ltp = yf.Ticker(i+'.NS')
            ltp = ltp.info['regularMarketPrice']
            # print(ltp)

            filterprice(df)

        except Exception as e:
            print(e)
    return df


def filtersector(df):
    x=input('Enter preffered sector/None')
    if(x!=None):
        df1=df[df["Sector"] == x] 
    else:
        return df
    return df1

def filterprice(df):
    x=input('Enter price')
    
    return df[int(df["Price"]) >=x ] 




# print(df)

