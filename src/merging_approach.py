from __future__ import division
__author__ = 'Vladimir Iglovikov'

'''
Let's check this approach.
Merge test and cookies on some column. and use device_id, cookie_id of the corresponding pair
'''

import graphlab as gl
import os

test = gl.SFrame(os.path.join('..', 'data', 'dev_test_basic.csv'))

print 'test.shape'
print test.shape
cookies = gl.SFrame(os.path.join('..', 'data', 'cookie_all_basic.csv'))

print 'cookies.shape'
print cookies.shape

result = test.join(cookies, on='anonymous_5', how='left')

print 'result.shape'
print result.shape

result.save(os.path.join('..', 'data', 'A5'))
