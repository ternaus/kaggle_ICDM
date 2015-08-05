from __future__ import division


'''
New idea.
[1] merge cookies with IP
[2] merge train and test with IP
[3] merge cookies and train/test using ip
[4] Use group by after this.
'''
import graphlab as gl
#
# cookie_ip = gl.SFrame('../data/id_all_ip.csv')
# print
# print 'ip_shape'
# print cookie_ip.shape
#
# cookies = gl.SFrame('../data/cookie_all_basic.csv')
#
# print
# print 'cookies_shape'
# print cookies.shape
#
# train = gl.SFrame('../data/dev_train_basic.csv')
#
# print
# print 'train_shape'
# print train.shape
#
# test = gl.SFrame('../data/dev_test_basic.csv')
#
# print
# print 'test_shape'
# print test.shape
#
#
# print 'merging cookie and ip'
#
# cookie_with_ip = cookies.join(cookie_ip, on={'cookie_id': 'device_or_cookie_id'}, how='left')
#
# print 'saving cookie_with_ip'
# cookie_with_ip.save('../data/cookie_with_ip')
#
# print 'merging train and ip'
# train_ip = train.join(cookie_ip, on={'device_id': 'device_or_cookie_id'}, how='left')
# print 'saving train_ip to file'
# train_ip.save('../data/train_with_ip')
#
# print 'merging test and ip'
# test_ip = test.join(cookie_ip, on={'device_id': 'device_or_cookie_id'}, how='left')
# print 'saving test_with_ip to file'
# test_ip.save('../data/test_with_ip')
#
# print 'merging cookies and train on ip'
# cookie_train = train_ip.join(cookie_with_ip, on='ip')
#
# print 'saving cookie_train to file'
# cookie_train.save('../data/cookie_train')
#
# print 'merging cookies and test on ip'
# cookie_test = test_ip.join(cookie_with_ip, on='ip')
#
# print 'saving cookie_train to file'
# cookie_test.save('../data/cookie_test')

print 'reading cookie_train from file'
cookie_train = gl.SFrame('../data/cookie_train')

print cookie_train.column_names()
print cookie_train.shape
print sum(cookie_train['drawbridge_handle'] == cookie_train['drawbridge_handle.1'])

# #For each device_or_cookie_id we find most frequent ip
#
# print
# print 'aggregating'
# aggregated_ip = cookie_ip.groupby(['device_or_cookie_id', 'ip'], {'ip_freq_count': gl.aggregate.MAX('ip_freq_count')})
# print aggregated_ip.shape
#
# print 'merging cookies'
# cookies_new = cookies.join(aggregated_ip, on={'cookie_id': 'device_or_cookie_id'}, how='left')
# print cookies_new.shape
#
#
#
# ind = 2
#
# if ind == 1:
#   train = gl.SFrame('../data/dev_train_basic.csv')
#
#   print
#   print 'train_shape'
#   print train.shape
#   print 'merging train'
#   train_new = train.join(aggregated_ip, on={'device_id': 'device_or_cookie_id'}, how='left')
#   print train_new.shape
#
#   print 'merging cookies and train'
#   train_cookies = train_new.join(cookies_new, on='ip')
#   print train_cookies.shape
#   print train_cookies.column_names()
#   print train_cookies.head()
#
#   print 'subsetting cookies'
#   train_cookies = train_cookies[(train_cookies['anonymous_c0'] == train_cookies['anonymous_c0.1'])
#                                 & (train_cookies['anonymous_c1'] == train_cookies['anonymous_c1.1'])
#                                 & (train_cookies['anonymous_c2'] == train_cookies['anonymous_c2.1'])
#                                 & (train_cookies['anonymous_5'] == train_cookies['anonymous_5.1'])
#                                 & (train_cookies['anonymous_6'] == train_cookies['anonymous_6.1'])
#                                 & (train_cookies['anonymous_7'] == train_cookies['anonymous_7.1'])
#   ]
#   print train_cookies.shape
#   print 'grouping train'
#   grouped_train = train_cookies.groupby(['drawbridge_handle', 'device_id'],
#                                         {'drawbridge_handle.1': gl.aggregate.SELECT_ONE('drawbridge_handle.1')},
#                                         {'cookie_id': gl.aggregate.SELECT_ONE('cookie_id')})
#
#   print grouped_train.shape
#
#   print sum(grouped_train['drawbridge_handle'] == grouped_train['drawbridge_handle.1'])
# elif ind == 2:
#   test = gl.SFrame('../data/dev_test_basic.csv')
#
#   print
#   print 'test_shape'
#   print test.shape
#   print 'merging test'
#   test_new = test.join(aggregated_ip, on={'device_id': 'device_or_cookie_id'}, how='left')
#
#   print test_new.shape
#
#   print 'merging cookies and test'
#   test_cookies = test_new.join(cookies_new, on='ip')
#
#   print test_cookies.shape
#   print test_cookies.column_names()
#   print test_cookies.head()
#   test_cookies = test_cookies[(test_cookies['anonymous_c0'] == test_cookies['anonymous_c0.1'])
#                                 & (test_cookies['anonymous_c1'] == test_cookies['anonymous_c1.1'])
#                                 & (test_cookies['anonymous_c2'] == test_cookies['anonymous_c2.1'])
#                                 & (test_cookies['anonymous_5'] == test_cookies['anonymous_5.1'])
#                                 & (test_cookies['anonymous_6'] == test_cookies['anonymous_6.1'])
#                                 & (test_cookies['anonymous_7'] == test_cookies['anonymous_7.1'])
#   ]
#
#   print 'grouping test'
#   grouped_test = test_cookies.groupby('device_id', {'cookie_id': gl.aggregate.SELECT_ONE('cookie_id')})
#
#   print grouped_test.shape
#   submission = gl.SFrame('../data/sampleSubmission.csv')
#   del submission['cookie_id']
#   submission = submission.join(grouped_test, how='left')
#   submission = submission.fillna('cookie_id', 'id_10')
#   submission.save('predictions/merge_frequent_ip_012567.csv')