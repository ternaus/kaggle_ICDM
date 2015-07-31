from __future__ import division

__author__ = 'Vladimir Iglovikov'

import graphlab as gl

test = gl.SFrame('../data/dev_test_basic.csv')
cookies = gl.SFrame('../data/cookie_all_basic.csv')


def helper(x):
  try:
    temp = cookies[(cookies['anonymous_5'] == x['anonymous_5'])]
    # temp = temp[temp['anonymous_6'] == x['anonymous_6']]
    # temp = temp[temp['anonymous_7'] == x['anonymous_7']]
    temp = temp['cookie_id'][0]
    # temp = cookies[(cookies['anonymous_5'] == x['anonymous_5']) & (cookies['anonymous_6'] == x['anonymous_6']) & (cookies['anonymous_7'] == x['anonymous_7'])]['cookie_id'][0]
  except:
    temp = 'id_1000182'
  return temp

submission = gl.SFrame()
submission['device_id'] = test['device_id']
submission['cookie_id'] = test.apply(helper)

submission.save('predictions/0_5.csv')