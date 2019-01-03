# SpyOnWeb

Python3 wrapper and CLI for the SpyOnWeb.com API

## Install

Install the [PyPi package](https://pypi.org/project/spyonweb/) : `pip install spyonweb`

You can also install it manually :
```
git clone https://github.com/Te-k/spyonweb.git
cd spyonweb
pip install .
```

## CLI

```
$ spyonweb config --token 2wldRA5t5xL9
In /home/user/.config/spyonweb:
[SpyOnWeb]
token = 2wldRA5t5xL9

$ spyonweb adsense pub-5953444431482912
--------------- pub-5953444431482912 -----------------
Fetched 10 domains over 10
-short-haircuts.org (2013-07-29)
-long-haircuts.com (2013-07-30)
-hewlettpackardprinterdrivers.net (2013-07-29)
-bobhairstyles.biz (2013-07-27)
-liver-disease-symptoms.com (2014-03-21)
-howtopatentanidea.net (2014-03-21)
-fullmooncalendar.net (2013-07-29)
-mens-haircuts.net (2014-03-24)
-bronchitis-symptoms.biz (2015-02-28)
-hernia-symptoms.com (2014-03-20)
```

## API

```python
from spyonweb import SpyOnWeb
client = SpyOnWeb(API_KEY)
client.analytics('UA-34505845')

{'fetched': 9,
 'found': 9,
 'items': {'bobhairstyles.biz': '2016-04-11',
  'bronchitis-symptoms.biz': '2015-02-28',
  'fullmooncalendar.net': '2017-10-02',
  'hewlettpackardprinterdrivers.net': '2016-04-17',
  'howtopatentanidea.net': '2016-04-18',
  'liver-disease-symptoms.com': '2016-04-21',
  'long-haircuts.com': '2016-04-21',
  'mens-haircuts.net': '2016-04-22',
  'short-haircuts.org': '2016-04-27'}}

client.ip('157.166.226.25')
{'fetched': 35,
 'found': 35,
 'items': {'ac360.com': '2015-05-26',
  'amanpour.com': '2017-09-25',
  'cnn.co.hu': '2017-05-18',
  'cnn.hu': '2017-09-29',
  'cnn.net': '2016-09-21',
  'cnn.tv': '2017-09-29',
[SNIP]
```
