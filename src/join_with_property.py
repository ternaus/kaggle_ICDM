from __future__ import division

__author__ = 'Vladimir Iglovikov'

'''
Let's try to add category to my dataset, so that I can use it in my prediction
'''

import graphlab as gl

print 'read property'
property = gl.SFrame('../data/id_all_property.csv')

print 'read category'
category = gl.SFrame('../data/property_category_corrected.csv')

print 'join property and category'
property_category = property.join(category)

print 'save property_category to file'

property_category.save('../data/property_category')