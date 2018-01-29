#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json
import datetime
#you can enable this to get timezone tzinfo object
#import pytz
page = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={NASDAQ ID}&interval=1min&apikey={yourapikey}')
if page.status_code == 200:
    data = json.loads(page.content)
    curr_date = datetime.datetime.now() #To chagne timezone(pytz.timezone("America/New_York"))
    #Changing to EST and delayed by 1 min 
    delta_date = curr_date - datetime.timedelta(minutes=1)
    delta_date = delta_date + datetime.timedelta(hours=3)
    recs = data["Time Series (1min)"][delta_date.strftime("%Y-%m-%d %H:%M:00")]["2. high"]
    print "(%s)" %(recs)
else:
    print "(ERR)"
