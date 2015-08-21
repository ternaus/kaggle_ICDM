from __future__ import division

__author__ = 'Vladimir Iglovikov'

'''
This script will prepare device_id => list of cookie_id from train set
'''

import graphlab as gl

train = gl.SFrame('../data/dev_train_basic.csv')
print train.shape
cookie = gl.SFrame('../data/cookie_all_basic.csv')
print cookie.shape

#merge train and cookie on drawbridge_handle

train_cookie = train.join(cookie, on='drawbridge_handle')

print train_cookie.shape
print train.column_names()