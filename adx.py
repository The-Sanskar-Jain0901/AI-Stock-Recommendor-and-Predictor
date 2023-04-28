import ta
import yfinance as yf
import datetime


def adx(df):
    df['adx'] = ta.trend.ADXIndicator(
        df['High'], df['Low'], df['Close'], window=14).adx()
    # df['adx'] = adx
    df['+DI'] = ta.trend.ADXIndicator(
        df['High'], df['Low'], df['Close'], window=14).adx_pos()
    df['-DI'] = ta.trend.ADXIndicator(
        df['High'], df['Low'], df['Close'], window=14).adx_neg()
    if df['adx'][len(df)-1] >= 20 and df['+DI'][len(df)-1] > df['-DI'][len(df)-1]:
        return 1
    return 0


start_date = datetime.datetime.now() - datetime.timedelta(days=365)
end_date = datetime.datetime.now()
df = yf.download('ICICIBANK' + '.NS', start=start_date,
                 end=end_date, interval='1d')
# print(df)
print(adx(df))
