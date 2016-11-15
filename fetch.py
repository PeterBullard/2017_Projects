from yahoo_finance import Share


name = Share('YHOO')
temp = (name.get_historical('2014-04-25', '2015-04-29'))

print (temp)


