from investiny import historical_data, search_assets
import pandas as pd
from datetime import date
import time

today1 = date.today()

# mm/dd/y
today = today1.strftime("%m/%d/%Y")

with open ("share_list.txt", "w") as o:
  o.write(f"Following Stocks meets the selection Criteria as at {today} : \n\n")

with open ("moving_averages.txt","w") as p:
  p.write(f"Following Stocks are perfectly aligned with the moving averages as at {today}. \n\n ")

all_shares_list = ['EMER','RICH']

all_shares_list1 = [ 'SINI', 'ACME', 'BALA','EMER','CTC','DIMO', 'MGT', 'MBSL', 'RGEM', 'GLAS', 'RCL', 'SIL', 'RHTL', 'LHL', 'WATA', 'YORK', 'ALLI', 'BBH', 'CTLD', 'CARS', 'CHLt', 'CTEA','DPL', 'GEST', 'ASPH', 'KGAL', 'KDL', 'LDEV', 'COCO', 'CSD', 'UML', 'CIND', 'CINS','CCS', 'HARI', 'HOPL', 'HUNA', 'KHL', 'LOLC', 'LITE', 'NTB', 'NHL', 'PALM', 'SHOTt', 'ABAN', 'CARG','CINV', 'SOY',  'RNUK', 'RENU', 'SLTL', 'SUN', 'PARQ', 'TRAN', 'CHL', 'DOCK', 'PHAR', 'EDEN','LAMB', 'TILE', 'MARA', 'SINS', 'TAJ', 'TAFL', 'BRWN', 'CFIN', 'CICt', 'COLO', 'DIPD', 'GHLL','ONAL', 'SHOT', 'BUKI', 'UAL',  'REEF', 'STAF', 'EBCR', 'HHL', 'HSIG', 'LVEN']

all_shares_list2 = ['ASIA', 'ASSO', 'BROW', 'DIAO', 'CEYL', 'CDBF', 'COMN','BERU', 'EXPO', 'HAYL', 'HUNT', 'HVAF', 'HYDP', 'IDL', 'JINS', 'LALU', 'LOLF', 'LWL', 'LGGL','MWEL', 'MSL', 'MULT', 'LOLD', 'NEH', 'ODEL', 'PANA', 'PEOP','RAIG', 'RFLL', 'RAFL', 'RHL', 'SANA', 'SIFI', 'SOCL', 'SOFT', 'AMBE', 'TEEJ','UNIO', 'UCHE', 'VALL', 'VALI', 'CITW', 'LANK', 'GOOD', 'AFSL', 'ALUM', 'ABLT', 'HPWR','CITH', 'ASHO', 'BANS', 'SLND', 'MHDL', 'SFL', 'CAPR']

all_shares_list3 =['CIT', 'SHAL', 'ARIC', 'SWAD', 'INDO', 'SIGH', 'PEIN', 'ORIT', 'COCOt', 'SFL_p', 'ANTK','LGGLt', 'RHLt', 'CDBFt', 'MALt', 'MELS', 'JETW', 'LVLE', 'HATT', 'MAHA', 'RENH', 'SMOT', 'SEYBt','SEMBt', 'SPEN', 'ATL', 'CONN', 'BFL', 'CHOT', 'DIAL', 'ECL', 'HEXP', 'LLUB','HASU', 'KCAB', 'CERA', 'LCEY', 'REG', 'SIRA', 'AUTO', 'APLA', 'ACAP', 'CIC', 'KHC', 'TYRE','NEST', 'SAMP', 'CTHR', 'CWM', 'JKL', 'SEYB', 'SEMB', 'ACL', 'ETWO', 'LFIN', 'SHAW', 'VLL','DFCC', 'LIOC', 'CARE', 'SELI', 'TESS', 'CHMX', 'HAYC', 'UNIS', 'ACCE', 'AGST', 'ASAS']

all_shares_list4 =['ABEO', 'BLUE', 'DIST', 'GUAR', 'LPRT', 'CFLB', 'HDFC', 'COMD', 'LHCL', 'BLUEt', 'AHUN', 'COMBt','PABC', 'MAL', 'CLND', 'AHPL', 'BOPL', 'COMB', 'WAPO', 'KVAL', 'NDB', 'TSML', 'UDPL', 'SFTL','BREW','HAPU', 'MULL', 'OSEA', 'PEG', 'PMB', 'RPBH', 'TKYOt', 'AMSL', 'ASIR', 'HNBt', 'SERC', 'SIGV','TPL', 'LION', 'TKYO', 'AGAL', 'CABO', 'GRAN', 'CFVF', 'LMF', 'NAMU', 'REXP', 'TANG', 'VPEL','BOGA', 'KAHA', 'MADU', 'MRH', 'MASK', 'EAST', 'ELPL', 'HNB', 'JKH', 'KFP', 'KOTA', 'CSF']

def share_criteria(share_list_no):
  for x in share_list_no:
    time.sleep(1)
    try:
      search_results_list = search_assets(query=x, limit=25, type="Stock")
      search_results_df= pd.DataFrame(search_results_list) 
      
      stock_row = search_results_df[search_results_df['exchange']=='Colombo']

      stock_symbol = stock_row.symbol.iloc[0]
      stock_description = stock_row.description.iloc[0]
      stock_ticker = stock_row.ticker.iloc[0]
      
      data = historical_data(investing_id=stock_ticker,from_date="05/01/2021", to_date=today)

      df = pd.DataFrame.from_dict(data)
      
      # 20 Moving average caculation
      MA20 = pd.Series(df['close'].rolling(20).mean(), name = 'SMA')
      MA20_value = MA20.iat[-1]

      # 50 Moving average caculation
      MA50 = pd.Series(df['close'].rolling(50).mean(), name = 'SMA') 
      MA50_value = MA50.iat[-1]

      # 100 Moving average caculation
      MA100 = pd.Series(df['close'].rolling(100).mean(), name = 'SMA') 
      MA100_value = MA100.iat[-1]

      # 150 Moving average caculation
      MA150 = pd.Series(df['close'].rolling(150).mean(), name = 'SMA') 
      MA150_value = MA150.iat[-1]

      # 200 Moving average caculation
      MA200 = pd.Series(df['close'].rolling(200).mean(), name = 'SMA') 
      MA200_value = MA200.iat[-1]

      # RSI caculation

      close = df['close']
      close_delta = close.diff()
      up = close_delta.clip(lower=0)
      down = -1 * close_delta.clip(upper=0)
      ma_up = up.ewm(com = 14 - 1, adjust=True, min_periods = 14).mean()
      ma_down = down.ewm(com = 14 - 1, adjust=True, min_periods = 14).mean()

      rsi = ma_up / ma_down
      rsi = 100 - (100/(1 + rsi))
      rsi_value = rsi.iat[-1]
     
      #Getting last closing price
      last_price = df['close'].iat[-1]
      
      #Getting 52 week high
    
      fiftytwo_high = pd.Series(df['high'].rolling(260).max(), name = '52weekhigh')
      fiftytwo_high_value = fiftytwo_high.iat[-1]
      
      #Getting 52 week high low
      fiftytwo_low = pd.Series(df['low'].rolling(260).min(), name = '52weeklow')
      fiftytwo_low_value = fiftytwo_low.iat[-1]

      #Stock Evaluations
      if last_price >= MA20_value >= MA50_value >= MA100_value >= MA150_value >= MA200_value: #condition 1
        with open ("moving_averages.txt", "a") as p:
                    p.write(f"{stock_symbol}' : '{stock_description}' : \n✅ Closing Price is {last_price} \n✅ 20 day mov avg : {'%.2f' % MA20_value} \n✅ day mov avg : {'%.2f' % MA50_value}\n✅ 52 Week High :{fiftytwo_high_value}\n✅ Closing price is {mov20_vs_closing_price} % higher/lower than the 20 day mov avg \n\n")   

        print(f"\n✅'{stock_symbol}' : '{stock_description}' is perfectly aligned with the moving averages.\n")     
        
      #condition 2
      if last_price >= MA20_value >= MA50_value >= MA100_value and last_price >= MA200_value and rsi_value >= 65 and (float(fiftytwo_high_value)*.75) <= last_price and (float(fiftytwo_low_value)*1.3) <=last_price:

        mov20_vs_closing_price = int((last_price-MA20_value)/last_price*100)

        with open ("share_list.txt", "a") as o:
                    o.write(f"{x} : \n✅ Closing Price is {last_price} \n✅ 20 day mov avg : {'%.2f' % MA20_value} and 50 day mov avg : {'%.2f' % MA50_value}\n✅ 52 Week High :{fiftytwo_high_value}\n✅ Closing price is {mov20_vs_closing_price} % higher/lower than the 20 day mov avg \n\n")

      
    except Exception as e: #getting the error message as e
            print(f"\n🧧 Error in the stock {stock_symbol}.\nError message : {e}\n")

share_criteria(all_shares_list)
share_criteria(all_shares_list1)
time.sleep(10)
print("\nall_shares_list1 completed")
share_criteria(all_shares_list2)
time.sleep(10)
print("\nall_shares_list2 completed")
share_criteria(all_shares_list3)
time.sleep(10)
print("\nall_shares_list3 completed")
share_criteria(all_shares_list4)
print("\nall_shares_list4 completed")

