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
print train_cookie.column_names()

#aggregate by device_id

train_cookie['cookie_id'] = train_cookie['cookie_id'].apply(lambda x: x + ' ').to_dataframe()

print train_cookie['cookie_id'].head()

result = train_cookie.groupby('device_id')['cookie_id'].sum()

# result = train_cookie.groupby('device_id', {'cookie_id': gl.aggregate.SUM('cookie_id')})
result['device_id'] = result['device_id'].apply(lambda x: x.strip(), 1)

print result.shape

#save result to file
result.to_csv('../data/train_cross.csv', index=False)
