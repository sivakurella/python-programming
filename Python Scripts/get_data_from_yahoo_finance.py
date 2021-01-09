from yahoo_finance import Share
import csv

goog = Share('GOOG')
data = goog.get_historical('2012-01-01', '2017-03-17')