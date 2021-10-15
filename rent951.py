#!bin/python3

import requests
import sys
import json
import datetime

base_url = "https://rent.591.com.tw/home/search/rsList?is_format_data=1&is_new_list=1&type=1"
url = "https://rent.591.com.tw/?section=371&searchtype=1&multiPrice=0_5000&other=newPost&kind=8"
condition = "&section=371&searchtype=1&kind=2&multiPrice=0_5000&other=newPost"
headers = {
	'Connection': 'keep-alive',
	'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
	'Accept': 'application/json, text/javascript, */*; q=0.01',
	'X-CSRF-TOKEN': 'VAZDQ933mo2BMx2CRKWdeMVLLbI8uSULcrnJ2nLn',
	'sec-ch-ua-mobile': '?0',
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
	'X-Requested-With': 'XMLHttpRequest',
	'sec-ch-ua-platform': '"macOS"',
	'Sec-Fetch-Site': 'same-origin',
	'Sec-Fetch-Mode': 'cors',
	'Sec-Fetch-Dest': 'empty',
	'Referer': 'https://rent.591.com.tw/',
	'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
	'Cookie': 'T591_TOKEN=db2907eae51344dd37182fa2b5315bf8; tw591__privacy_agree=0; _ga=GA1.4.1216380023.1627267619; _ga=GA1.3.1216380023.1627267619; __auc=f30319e517ae0b558823c00393d; _fbp=fb.2.1627267619964.1570448758; webp=1; PHPSESSID=5d2hgui2gcb1u9j1d0mg80pon5; urlJumpIp=4; urlJumpIpByTxt=%E6%96%B0%E7%AB%B9%E5%B8%82; is_new_index=1; is_new_index_redirect=1; _gid=GA1.3.2069843648.1634302683; user_index_role=8; user_browse_recent=a%3A3%3A%7Bi%3A0%3Ba%3A2%3A%7Bs%3A4%3A%22type%22%3Bi%3A8%3Bs%3A7%3A%22post_id%22%3Bi%3A117156%3B%7Di%3A1%3Ba%3A2%3A%7Bs%3A4%3A%22type%22%3Bi%3A1%3Bs%3A7%3A%22post_id%22%3Bi%3A11396700%3B%7Di%3A2%3Ba%3A2%3A%7Bs%3A4%3A%22type%22%3Bi%3A1%3Bs%3A7%3A%22post_id%22%3Bs%3A8%3A%2211181234%22%3B%7D%7D; _gat_UA-97423186-1=1; _gat=1; _dc_gtm_UA-97423186-1=1; __asc=77a5e5d817c840b197b8c3999d2; __utma=82835026.1216380023.1627267619.1634302892.1634302892.1; __utmc=82835026; __utmz=82835026.1634302892.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmb=82835026.1.10.1634302892; newUI=1; _gid=GA1.4.2069843648.1634302683; XSRF-TOKEN=eyJpdiI6IjJBMk5kQndXWkZvNUR6UUV3T09TMmc9PSIsInZhbHVlIjoiZHlCcUE5bTdTXC8xNWFGT25nbzA5RmZHZzI5cEZqTEVjSEp4WlwvVlZ1VlRuNmVTZFNFQzYwRU5BbkxIWHE3dHJ6bjBZS2g2Nm9uMlR3WmlacjhhNGZUdz09IiwibWFjIjoiOGEyODAxZGMyZWY3YzQ3MzQ0MTQxN2YzZTk3MjlkMTgwYzRjODUyMTExNDQ5OWE4MDI0YTc5YjIxMmY3YTM1NCJ9; new_rent_list_kind_test=0; 591_new_session=eyJpdiI6IldUTmlCMTFVdjYzdDhsbHdQdlJ4cFE9PSIsInZhbHVlIjoiR2hoRWxBdW1tQVlSYnJDRXhHaWt0Q29aRVV6U3IzblhvQkJDVU15SU5cL1JwT2pvMExWOTA0TDVFQXdlNWJuRUp4UnNYUTRHTDdMb3hPSllHdkdEWVBRPT0iLCJtYWMiOiJlYjliODMyMTM0NWY2NGI2YmM0MDNmYzc2NjQ0YTRmNjliZGM4NmVhMGFkZDQ5ZDk0NTJlN2YxODk3NDkzNzBkIn0%3D;'
}

file_name = "rent_" + datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + ".csv"
file_ptr = ""

def file_init():
	global file_name
	global file_ptr

	print("Filename: ", file_name)
	file_ptr = open(file_name, mode='w', encoding = "Big5")

	file_write('title, name, phone, url')

def file_write(context):
	global file_ptr

	file_ptr.write(context.encode('big5','replace').decode('big5','replace') + '\n')

def file_end():
	global file_ptr

	file_ptr.close()

def get_token():
	global headers

	res = requests.get("https://rent.591.com.tw/", headers=headers, stream=True)
	print(res.headers['Set-Cookie'])
	#print(res.headers)
	if (int(res.status_code) != 200):
		print("Get token error.")
		exit()


def get_itemdata(post_id):
	headers = {
		'Connection' :'keep-alive',
		'deviceid' :'db2907eae51344dd37182fa2b5315bf8',
		'X-CSRF-TOKEN' :'VAZDQ933mo2BMx2CRKWdeMVLLbI8uSULcrnJ2nLn',
		'sec-ch-ua-mobile' :'?0',
		'User-Agent' :'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
		'Accept' :'*/*',
		'device' :'pc',
		'token' :'5d2hgui2gcb1u9j1d0mg80pon5',
		'sec-ch-ua-platform' :'"macOS"',
		'sec-ch-ua' :'"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
		'Origin' :'https://rent.591.com.tw',
		'Sec-Fetch-Site' :'same-site',
		'Sec-Fetch-Mode' :'cors',
		'Sec-Fetch-Dest' :'empty',
		'Referer' :'https://rent.591.com.tw/',
		'Accept-Language' :'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
	}

	item_url = "https://bff.591.com.tw/v1/house/rent/detail?id=" + str(post_id)

	res = requests.get(item_url, headers=headers)
	print("Item url: ", item_url)
	ret_json = json.loads(res.text)
	if (int(res.status_code) != 200):
		print("Get item error.")
		exit()

	file_write(ret_json['data']['title'] + "," + ret_json['data']['linkInfo']['imName'] + "," + ret_json['data']['linkInfo']['mobile'].replace("-", "") + "," + "https://rent.591.com.tw/home/" + str(post_id))

def get_apagedata(index = 0, max = 0):
	global base_url
	global condition
	global headers

	if (max <= index):
		return

	page_url = base_url + condition + "&firstRow=" + str(index)

	res = requests.get(page_url, headers=headers)
	print("Page url: ", page_url)
	ret_json = json.loads(res.text)
	if (int(res.status_code) != 200):
		print("Get page error.")
		exit()
	
	# Item get
	item_num = len(ret_json['data']['data'])
	print("Item number: ", item_num)
	for index in range(0, item_num):
		get_itemdata(ret_json['data']['data'][index]['post_id'])

def __main__():
	global base_url
	global url
	global condition
	global headers

	if len(sys.argv) > 1:
		url = sys.argv[1]
		try:
			condition = url.split("/?")[1]
			condition = "&" + condition
		except:
			print("Url Error.")
			exit()

	print("Url  =", url)
	print("Cond =", condition)

	res = requests.get(base_url + condition, headers=headers)
	ret_json = json.loads(res.text)
	if (int(res.status_code) != 200):
		print("Get 591 error.")
		exit()

	# Record numbers
	record_num = int(ret_json['records'])

	page = 0
	for index in range(0, record_num, 30):
		page = page + 1
		print("Page: ", page)
		get_apagedata(index, record_num)

# Start main
get_token()
file_init()
__main__()
file_end()