from __future__ import division

__author__ = 'Vladimir Iglovikov'

'''
I need to figure out how to do cross_validation
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
#merge cookie with ip
cookie_ip = cookie.join(ip, on={'cookie_id': 'device_or_cookie_id'}, how='left')

#merge cookie and train on ip
cookie_train = train_ip.join(cookie_ip, on=['ip'])
#count how many drawbridge_handle match
temp = cookie_train.groupby('device_id', {'drawbridge_hangle': gl.aggregate.SELECT_ONE('drawbridge_handle'),
                                          'drawbridge_hangle.1': gl.aggregate.SELECT_ONE('drawbridge_handle.1'),
                                          'cookie_id': gl.aggregate.SELECT_ONE('cookie_id')})
print temp.shape
print temp[temp['drawbridge_handle'] == temp['drawbridge_handle.1']].shape