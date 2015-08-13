from __future__ import division

__author__ = 'Vladimir Iglovikov'

'''
I need to figure out how to do cross_validation.

Main idea so far is to predict device - cookie, pair, merge it with train/cookie and see how many handles matched.
'''

import graphlab as gl
#read train
train = gl.SFrame('../data/dev_train_basic.csv')
print train.shape
#read ip
ip = gl.SFrame('../data/id_all_ip.csv')
#merge train with ip
print train.column_names()
train_ip = train.join(ip, on={'device_id': 'device_or_cookie_id'}, how='left')

#read cookie
cookie = gl.SFrame('../data/cookie_all_basic.csv')
print 'cookie shape'
print cookie.shape
cookie = cookie[cookie['drawbridge_handle'] != '-1']
print cookie.shape

print 'merge cookie with ip'
cookie_ip = cookie.join(ip, on={'cookie_id': 'device_or_cookie_id'}, how='left')

print 'merge cookie and train on ip'
cookie_train = train_ip.join(cookie_ip, on='ip')


ind = 2

if ind == 1: #pick random device_id, cookie_id pairs
  print 'grouping train'
  temp = cookie_train.groupby('device_id', {'drawbridge_handle': gl.aggregate.SELECT_ONE('drawbridge_handle'),
                                            'drawbridge_handle.1': gl.aggregate.SELECT_ONE('drawbridge_handle.1'),
                                            'cookie_id': gl.aggregate.SELECT_ONE('cookie_id')})
  print temp.column_names()
  print temp.shape
  print 'count how many drawbridge_handle match'
  print temp[temp['drawbridge_handle'] == temp['drawbridge_handle.1']].shape
elif ind == 2:#pick device_id, cookie_id pairs when they have maximum count of common IP
  print 'grouping train'
  temp = cookie_train.groupby(['device_id', 'cookie_id'],
                              {'count_ip': gl.aggregate.COUNT('ip')})

  print 'finding cookie_id with maximum match'
  temp_new = temp.groupby('device_id', {'cookie_id': gl.aggregate.ARGMAX('count_ip', 'cookie_id')})

  #Now I need to merge these device_id, cookie_id pairs with initial train/cookie to be able to estimate number of matches.
  print 'joining with train and cookie'
  result = temp_new.join(train, on='device_id').join(cookie, on='cookie_id')
  print result.shape
  print result[result['drawbridge_handle'] == result['drawbridge_handle.1']].shape

