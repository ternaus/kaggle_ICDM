from __future__ import division

__author__ = 'Vladimir Iglovikov'

import pandas as pd

test = pd.read_csv('../data/dev_test_basic.csv')
cookies = pd.read_csv('../data/cookie_all_basic.csv')

result = []

ind = 0
for i in range(test.shape[0]):
  if i >= 100 and i % 100 == 0:
    print i
  try:
    temp = cookies[(cookies['anonymous_5'] == test.loc[i, 'anonymous_5']) & (cookies['anonymous_6'] == test.loc[i, 'anonymous_6']) & (cookies['anonymous_7'] == test.loc[i, 'anonymous_7'])]['cookie_id'].values[0]
  except:
    ind += 1
    temp = 'id_1000182'
  result += [temp]

print 'missing = ', ind

submission = pd.DataFrame()
submission['device_id'] = test['device_id']
submission['cookie_id'] = result
submission.to_csv('predictions/0_567.csv', index=False)