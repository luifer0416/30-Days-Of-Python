from datetime import datetime
from datetime import date
from datetime import timedelta
"""
now = datetime.now()
print(now)                      # 2021-07-08 07:34:46.549883
day = now.day                   # 8
month = now.month               # 7
year = now.year                 # 2021
hour = now.hour                 # 7
minute = now.minute             # 38
second = now.second
timestamp = now.timestamp()
print(day, month, year, hour, minute)
print('timestamp', timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute}')  # 8/7/2021, 7:38


d = date(2020, 1, 1)
print(d)
print('Current date:', d.today())    # 2019-12-05
# date object of today's date
today = date.today()
print("Current year:", today.year)   # 2019
print("Current month:", today.month) # 12
print("Current day:", today.day)     # 5

today = date(year=2019, month=12, day=5)
new_year = date(year=2020, month=1, day=1)
print(type(new_year))
time_left_for_newyear = new_year - today
# Time left for new year:  27 days, 0:00:00
print('Time left for new year: ', time_left_for_newyear)

t1 = datetime(year = 2019, month = 12, day = 5, hour = 0, minute = 59, second = 0)
t2 = datetime(year = 2020, month = 1, day = 1, hour = 0, minute = 0, second = 0)
diff = t2 - t1
print('Time left for new year:', diff) # Time left for new year: 26 days, 23: 01: 00


from datetime import timedelta
t1 = timedelta(weeks=12, days=1, hours=4, seconds=20)
t2 = timedelta(days=60, hours=5, minutes=3, seconds=30)
print(t1)
print(t2)
t3 = t1 - t2
print("t3 =", t3)
"""
now = datetime.now()
print(now) 
                  
day = now.day                   
month = now.month               
year = now.year                 
hour = now.hour                
minute = now.minute             
second = now.second
timestamp = now.timestamp()
print(day, month, year, hour, minute)
print('timestamp', timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute}:{second}')  # 8/7/2021, 7:38

now2=now.strftime( "%Y-%m-%d, %H:%M:%S")
print(now2) 

today_str= "5 Dec 19"
today_date=datetime.strptime(today_str,"%d %b %y")
print(today_date)


new_year=datetime(2024,12,31)
print(now)
print(new_year)
enero_70=datetime(1970,1,1)
tiempo_para_año_nuevo=now-new_year
print(tiempo_para_año_nuevo)
desde_70_to_now=now-enero_70
print(desde_70_to_now)
"""
###USOS TIME STAMP
Para aplicaciones de tipo agenda, donde se requiere llevar control del tiempo
Para registro de aplicaciones donde se tengan subscripciones
Una aplicación que una función solo sea habilitada en cierto tiempo
Una aplicación automatica que debe realizar una acción a cierta hora o en cierto dia
"""