from __future__ import division
__author__ = 'Vladimir Iglovikov'

'''
Basic script in which I will check ideas using train set
'''

'''
Let's check idea about merging on IP and selecting one randomly
'''

import graphlab as gl
import pandas as pd
from sklearn.metrics import f1_score

# print 'reading train'
# train = gl.SFrame('../data/dev_train_basic.csv')
#
# print 'reading ip'
# ip = gl.SFrame('../data/id_all_ip.csv')
#
# print 'reading cookie'
# cookie = gl.SFrame('../data/cookie_all_basic.csv')

print 'reading ground truth'
ground_truth = gl.SFrame('../data/train_cross.csv')

# print 'merge train and ip'
# train_ip = train.join(ip, on={'device_id': 'device_or_cookie_id'})

# print 'merge cookie and ip'
# cookie_ip = cookie.join(ip, on={'cookie_id': 'device_or_cookie_id'})
# cookie_ip = gl.SFrame('../data/cookie_with_ip')

# print 'merge train_ip and cookie_ip'
print 'read train_ip and cookie_ip'
# train_cookie = train_ip.join(cookie_ip, on='ip')
train_cookie = gl.SFrame('../data/cookie_train')

# print 'adding space for each cookie_id'
train_cookie['cookie_id'] = train_cookie['cookie_id'].apply(lambda x: x + ' ')

print 'unstucking'
result = train_cookie.groupby('device_id', {'cookie_id': gl.aggregate.CONCAT('cookie_id')})

print 'converting back to graphlab and merging with result'
result = result.join(ground_truth, on='device_id')

print result.column_names()
print result.head()


def helper(x):
  return f1_score(x['cookie_id.1'].strip().split(), x['cookie_id.1'].strip().split())

result['f1'] = result.apply(helper)

score = result['f1'].mean()
print score
