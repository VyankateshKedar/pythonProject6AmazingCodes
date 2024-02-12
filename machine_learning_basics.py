import pandas as pd
#import data
df=pd.read_csv("weather_data.csv")
print(df)

# Create Data File
weather_data={
    'day': ['1/1/2017','1/2/2017','1/3/2017','1/4/2017','1/5/2017','1/6/2017'],
    'temperature': [32,35,28,24,32,31],
    'windspeed': [6,7,2,7,4,2],
    'event': ['Rain','Sunny','Snow','Snow','Rain','Sunny']
}
df=pd.DataFrame(weather_data)
print(df)

rows,columns=df.shape
print(columns)
print(rows)

#Top & Bottom rows print
head=df.head(2)
print(head)
head=df.tail(1)
print(head)

#selected data
select=df[3:5]
print(select)

col=df.columns
print(col)

event=df['event']
print(event)

select1=df[['event','day']]
print(select1)
select2=df[['event','day','temperature']]
print(select2)

temp=df['temperature'].max()
print(temp)

temp1=df['temperature'].min()
print(temp1)

temp2=df['temperature'].mean()
print(temp2)

#all statistical value
stat=df.describe()
print(stat)

#apply condition to the data
max_value=df[df.temperature>=32]
print(max_value)

value=df[df.temperature==df.temperature.max()]
print(value)

#remove serial number from data
serial=df.set_index('day',inplace=True)
print(serial)

s1=df.loc['1/3/2017']
print(s1)

