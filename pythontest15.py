import datetime

for i in range(52):
 d = datetime.date(1476+i*10,1,26).weekday()
 if d == 0:
  print 1476+i*10
