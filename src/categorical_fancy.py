from __future__ import division
__author__ = 'Vladimir Iglovikov'
import graphlab as gl


print 'Read cookie_id'
cookie = gl.SFrame('../data/cookie_all_basic.csv')

print 'Read ip'
ip = gl.SFrame('../data/id_all_ip.csv')

print 'Read test'
test = gl.SFrame('../data/dev_test_basic.csv')

print 'read property category'
property_category = gl.SFrame('../data/property_category')

print 'split property category into device and cookie'
property_category_device = property_category[property_category['device_or_cookie_indicator'] == 0]
print property_category_device.shape
property_category_cookie = property_category[property_category['device_or_cookie_indicator'] == 1]
print property_category_cookie.shape

print 'split ip into device and cookie'
ip_device = ip[ip['device_or_cookie_id'] == 0]
print 'ip_device.shape = ', ip_device.shape
ip_cookie = ip[ip['device_or_cookie_id'] == 1]
print 'ip_cookie.shape = ', ip_device.shape

print 'remove from cookie rows for which draw_bridge_handle = -1'
print test.shape
test = test[test['drawbridge_handle.1'] != '-1']
print test.shape
test = test[test['drawbridge_handle.1'] != -1]
print test.shape

print 'merge cookie and property'
cookie_property = cookie.join(property_category_cookie, on = {'cookie_id': 'device_or_cookie_id'})
print cookie_property.shape

print 'merge device and property'
device_property = test.join(property_category_device, on = {'device_id': 'device_or_cookie_id'})
print device_property.shape

print 'merge cookie and ip'
cookie_property = cookie_property.join(ip_cookie, on={'cookie_id': 'device_or_cookie_id'})
print cookie_property.shape

print 'merge device and ip'
device_property = device_property.join(ip_device, on={'cookie_id': 'device_or_cookie_id'})
print device_property.shape

print 'merging on ip'
cookie_test_property = device_property.join(cookie_property, on='ip')

print 'save cookie_test_property to file'
cookie_test_property.save('../data/cookie_test_property')