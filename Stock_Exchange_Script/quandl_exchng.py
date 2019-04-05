import requests
import pandas as pandas
from datetime import date,timedelta

url = "https://www.quandl.com/api/v3/datasets/BSE/BOM500003?start_date=2019-03-29&end_date=2019-03-29&api_key=mVDfexTVqdxa5KZtGiQ7"
dateTime = date.today()
flag=1
#Read qunadl code from csv file
def readQuandlCode():
	quandl_code = pandas.read_csv("BSE_metadata.csv",index_col='name')
	data2 = quandl_code.loc['AEGIS LOGISTICS LTD. EOD Prices']
	print(data2)
	return data2[0]

def currentDate():	
	if flag == 1:
		dateTime1 = dateTime - timedelta(2)
		date_n = dateTime1
		return_date = date_n.strftime('%Y-%m-%d')

	else:
		return_date = dateTime.strftime('%Y-%m-%d')

	return return_date


print(currentDate())
result = requests.get(url.format(currentDate()))

data = result.json()
metadata = data['dataset']['data']


if len(metadata) == 0:
	flag = 1
else:
	flag = 0


#print(metadata)
#data1 = result1.json()

#d = readQuandlCode()
#print(len(d))
#print(d)
