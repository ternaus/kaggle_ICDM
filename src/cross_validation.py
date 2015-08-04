import graphlab as gl

cookie_ip = gl.SFrame('../data/id_all_ip.csv')
train = gl.SFrame('../data/dev_train_basic.csv')
cookies = gl.SFrame('../data/cookie_all_basic.csv')

#For each device_or_cookie_id we find most frequent ip

print
print 'aggregating'
aggregated_ip = cookie_ip.groupby(['device_or_cookie_id', 'ip'], {'ip_freq_count': gl.aggregate.MAX('ip_freq_count')})

print 'merging cookies'
cookies_new = cookies.join(aggregated_ip, on={'cookie_id': 'device_or_cookie_id'}, how='left')

print 'merging train'
train_new = train.join(aggregated_ip, on={'device_id': 'device_or_cookie_id'}, how='left')

print 'merging cookies and train'

train_cookies = train_new.join(cookies_new, on='ip')
print train.shape
print train.column_names()
print train.head()