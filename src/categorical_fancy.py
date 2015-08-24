from __future__ import division
__author__ = 'Vladimir Iglovikov'
import graphlab as gl


print 'Read cookie_id'
cookie = gl.SFrame('../data/cookie_all_basic.csv')


print 'remove from cookie rows for which draw_bridge_handle = -1'
print cookie.shape
cookie = cookie[cookie['drawbridge_handle'] != '-1']
print cookie.shape

print 'Read ip'
ip = gl.SFrame('../data/id_all_ip.csv')
print ip.shape

print 'split ip into cookie and device'
ip_cookie = ip[ip['device_or_cookie_indicator'] == 1]

ip_device = ip[ip['device_or_cookie_indicator'] == 0]

print 'Read test'
test = gl.SFrame('../data/dev_test_basic.csv')
print test.shape

print 'read id_all_property'
id_all_property = gl.SFrame('../data/id_all_property.csv')
print id_all_property.shape


id_all_property_cookie = id_all_property[id_all_property['device_or_cookie_indicator'] == 1]
print id_all_property_cookie.shape
id_all_property_device = id_all_property[id_all_property['device_or_cookie_indicator'] == 0]
print id_all_property_device.shape

print 'read_category'
category = gl.SFrame('../data/property_category_corrected.csv')
print category.shape

print 'merging id_all_ip_cookie and category'
id_all_property_cookie = id_all_property_cookie.join(category, on='property_id')
print id_all_property_cookie.shape

print 'merging id_all_ip_device and category'
id_all_property_device = id_all_property_device.join(category, on='property_id')
print id_all_property_device.shape

print 'unstucking cookie category'
id_all_cookie = id_all_property_cookie.unstack('device_or_cookie_id', new_column_name='category_id')
print id_all_cookie.shape

print 'unstucking device category'
id_all_device = id_all_property_device.unstack('device_or_cookie_id', new_column_name='category_id')
print id_all_device.shape

print 'merging cookie and ip'
ip_cookie = cookie.join(ip_cookie, on={'cookie_id': 'device_or_cookie_id'})
print ip_cookie.shape

print 'merging cookie and ip'
ip_device = test.join(ip_device, on={'device_id': 'device_or_cookie_id'})
print ip_device.shape

print 'merge cookie and device on ip'
device_cookie = ip_device.join(ip_cookie, on='ip')
print device_cookie.shape

print 'merge device_cookie and id_all_property_device'
device_cookie = device_cookie.join(id_all_property_device, on={'device_id': 'device_or_cookie_id'})
print device_cookie.shape

print 'merge device_cookie and id_all_property_cookie'
device_cookie = device_cookie.join(id_all_property_cookie, on={'cookie_id': 'device_or_cookie_id'})
print device_cookie.shape

print device_cookie.head()
device_cookie.save('../data/device_cookie_category')

#
# print 'merge cookie and id_all_ip'
# cookie_property = cookie.join(id_all_ip_cookie, on={'cookie_id': 'device_or_cookie_id'})
# print cookie_property.shape
#
# print 'merge device and id_all_ip'
# device_property = test.join(id_all_ip_device, on={'device_id': 'device_or_cookie_id'})
# print device_property.shape
#
# print 'merge cookie and ip'
# cookie_property = cookie_property.join(ip_cookie, on={'cookie_id': 'device_or_cookie_id'})
# print cookie_property.shape
# print 'save cookie_property to file'
# cookie_property.save('../data/cookie_property')
#
# print 'merge device and ip'
# device_property = device_property.join(ip_device, on={'device_id': 'device_or_cookie_id'})
# print device_property.shape
# print 'save device_property to file'
# device_property.ssave('../data/device_property')
#
#
# print 'merging on ip'
# cookie_test_property = device_property.join(cookie_property, on='ip')
# print cookie_test_property.shape
#
# print 'save to file cookie_test_propery'
# cookie_test_property.save('../data/cookie_test_property')
#
# print 'merge with category'
# cookie_test_property = cookie_test_property.join(category, on='property_id')
# print cookie_test_property.shape
# cookie_test_property = cookie_test_property.join(category, on={'property_id.1': 'property_id'})
# print cookie_test_property.shape
#
# print 'save cookie_test_property to file'
# cookie_test_property.save('../data/cookie_test_category')