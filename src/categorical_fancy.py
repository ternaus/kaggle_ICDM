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

print 'Read test'
test = gl.SFrame('../data/dev_test_basic.csv')

print 'read id_all_property'
id_all_ip = gl.SFrame('../data/id_all_property.csv')

print 'split id_all_ip into device and cookie'
id_all_ip_cookie = id_all_ip[id_all_ip['device_or_cookie_indicator'] == 1]
print id_all_ip_cookie.shape
id_all_ip_device = id_all_ip[id_all_ip['device_or_cookie_indicator'] == 0]
print id_all_ip_device.shape

print 'read_category'
category = gl.SFrame('../data/property_category_corrected.csv')
print category.shape

print 'split ip into device and cookie'
ip_device = ip[ip['device_or_cookie_indicator'] == 0]
print 'ip_device.shape = ', ip_device.shape
ip_cookie = ip[ip['device_or_cookie_indicator'] == 1]
print 'ip_cookie.shape = ', ip_cookie.shape


print 'merge cookie and id_all_ip'
cookie_property = cookie.join(id_all_ip_cookie, on = {'cookie_id': 'device_or_cookie_id'})
print cookie_property.shape

print 'merge device and id_all_ip'
device_property = test.join(id_all_ip_device, on = {'device_id': 'device_or_cookie_id'})
print device_property.shape

print 'merge cookie and ip'
cookie_property = cookie_property.join(ip_cookie, on={'cookie_id': 'device_or_cookie_id'})
print cookie_property.shape

print 'merge device and ip'
device_property = device_property.join(ip_device, on={'cookie_id': 'device_or_cookie_id'})
print device_property.shape

print 'merging on ip'
cookie_test_property = device_property.join(cookie_property, on='ip')
print cookie_test_property.shape

print 'merge with category'
cookie_test_property = cookie_test_property.join(category, on='property_id')
print cookie_test_property.shape
cookie_test_property = cookie_test_property.join(category, on={'property_id.1': 'property_id'})
print cookie_test_property.shape

print 'save cookie_test_property to file'
cookie_test_property.save('../data/cookie_test_property')