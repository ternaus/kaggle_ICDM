import graphlab as gl

cookie_ip = gl.SFrame('../data/id_all_ip.csv')
# train = gl.SFrame('../data/dev_train_basic.csv')
# cookies = gl.SFrame('../data/cookie_all_basic.csv')

#For each device_or_cookie_id we find most frequent ip

print
print 'aggregating'
aggregated_ip = cookie_ip.groupby(['device_or_cookie_id', 'ip'], {'ip_freq_count': gl.aggregate.MAX('ip_freq_count')})

print aggregated_ip.shape
print aggregated_ip.head()

