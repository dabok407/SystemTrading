from pandas import Series, DataFrame

daeshin = {'open':  [11650, 11100, 11200, 11100, 11000],
           'high':  [12100, 11800, 11200, 11100, 11150],
           'low' :  [11600, 11050, 10900, 10950, 10900],
           'close': [11900, 11600, 11000, 11100, 11050]}

##daeshin_day = DataFrame(daeshin)
date = ['16.02.29', '16.02.26', '16.02.25', '16.02.24', '16.02.23']
daeshin_day = DataFrame(daeshin, columns=['open', 'high', 'low', 'close'], index=date)

##close = daeshin_day['close']
##print(close)

## 아래와 같이 사용 X
##print(daeshin_day['16.02.24'])

##DataFrame 객체의 로우에 접근하려면 loc메서드를 사용하여 인덱스 값 세팅
day_data = daeshin_day.loc['16.02.24']
print(day_data)