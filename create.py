# -*- coding: utf-8 -*-
from sqlManage import SQLManagement
import random
from collections import deque

res = 1
temp = 4999.0/5000

for i in range(0,100):
	print i, i*30/60, res
	res *= temp




# for i in range(0,10):
# 	for j in range(0,15):
# 		temp = i*100 + j
# 		print '  `device_%03d_ID` int(11) DEFAULT NULL,' %temp
# 		print '  `device_%03d_statu` int(11) DEFAULT \'0\',' %temp
# 		print '  `device_%03d_value` int(11) DEFAULT \'-1\',' %temp


# for i in range(0,10):
# 	for j in range(0,15):
# 		temp = i*100 + j
# 		print '  KEY `device_%03d_ID` (`device_%03d_ID`),' %(temp, temp)

# count = 2
# for i in range(0,10):
# 	for j in range(0,15):
# 		temp = i*100 + j
# 		print '  CONSTRAINT `record_ibfk_%d` FOREIGN KEY (`device_%03d_ID`) REFERENCES `device` (`ID`),' %(count, temp)
# 		count += 1

# print "inedfgdfg %s sdfsdfsdf %d" %('maobo', 123)
# print len(roomList)