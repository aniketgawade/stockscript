#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json
page = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=AMZN&interval=1min&apikey={API KEY}')
if page.status_code == 200:
    data = json.loads(page.content)
    for rec in sorted(data["Time Series (1min)"],reverse=True):
        print "(%s)" %(data["Time Series (1min)"][rec]["2. high"])
        break
else:
    print "(ERR)"
