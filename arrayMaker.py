import numpy as np
import json
from googlefinance import getQuotes as getQuotes
import urllib
import fetch
#x = number of elements per array
#y = number of array points per master array
x = 0
y = 0
def test():
    

    TempArray = np.array((3, 5, 2, 15, 7, 9, 45, 6), dtype=float)

arrayFinal = np.array(([4, 6, 8, 10, 12, 14, 16, 18], [1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3, 3, 3], [4, 4, 4, 4, 4, 4, 4, 4] ,[5, 5, 5, 5, 5, 5, 5, 5] ,[6, 6, 6, 6, 6, 6, 6, 6] ,[7, 7, 7, 7, 7, 7, 7, 7] ,[8, 8, 8, 8, 8, 8, 8, 8]), dtype=float)


Data = json.dumps(getQuotes('^GSPC'), indent=2)

base_url = "http://ichart.finance.yahoo.com/table.csv?s="
def make_url(ticker_symbol):
    return base_url + ticker_symbol

output_path = "C:/path/to/output/directory"
def make_filename(ticker_symbol, directory="S&P"):
    return output_path + "/" + directory + "/" + ticker_symbol + ".csv"

def pull_historical_data(ticker_symbol, directory="S&P"):
    try:
        urllib.urlretrieve(make_url(ticker_symbol), make_filename(ticker_symbol, directory))
    except urllib.ContentTooShortError as e:
        outfile = open(make_filename(ticker_symbol, directory), "w")
        outfile.write(e.content)
        outfile.close()
        


# import data from csv files, or fetch using API
# format corresponding pieces of data into TempArray by date
# add TempArray to arrayFinal and move to next day