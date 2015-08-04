from __future__ import division
__author__ = 'Vladimir Iglovikov'

'''
Let's check this approach.
Merge test and cookies on some column. and use device_id, cookie_id of the corresponding pair
'''

import graphlab as gl
import os
import pandas as pd

test = gl.SFrame(os.path.join('..', 'data', 'dev_test_basic.csv'))

print 'test.shape'
print test.shape
cookies = gl.SFrame(os.path.join('..', 'data', 'cookie_all_basic.csv'))

print 'cookies.shape'
print cookies.shape

#Let's merge with anonymous_5

print 'aggregating'
df = cookies.groupby("anonymous_5", {'cookie_id': gl.aggregate.SELECT_ONE('cookie_id')})

print cookies["anonymous_5"].shape
print df.shape

result = test.join(df, on='anonymous_5', how='left')

print 'result.shape'
print result.shape

submission = pd.DataFrame()
submission['device_id'] = result['device_id']
submission['cookie_id'] = result['cookie_id']
print submission.info()

submission.to_csv('predictions/5.csv', index=False)