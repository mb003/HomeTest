# -*- coding: utf-8 -*-

from sqlManage import SQLManagement
import time

sqlMana = SQLManagement()

startTime = time.time()

count = 1

for i in range(0,count):
    # res = sqlMana.query('select * from sensor where ID = 3568')
    # sqlMana.update('update sensor set PM25 = 100.23 where ID = 3568')
    sql = "insert into sensor (ADDR,CO2,PM25,TVOC,Temperature,Humidity) values (10, 10, 10, 10, 10, 10);"
    sqlMana.insert(sql)
    res = sqlMana.query('select @@identity as newID')
    # sql = "delete from sensor where ADDR = 10"
    # res = sqlMana.delete(sql)

endTime = time.time()

deltaTime = endTime - startTime

print(res[0].get('newID'))

# print(count / deltaTime)
# print(res[0].get("PM25"))
# print(len(res))
# for temp in res:
	# print(temp.get("PM25"))


# time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))