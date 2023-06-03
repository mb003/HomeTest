# -*- coding: utf-8 -*-

from human import human
from devices import device
from houses import house
import time
import random
from collections import deque
from events import event

# Important parameters
timeSlot = 30
weekdayEventTimeList = {
	"07:55:00"      :      "wakeUp",
	"08:10:00"      :      "eatDinner",
	"08:30:00"      :      "goToSchool",
	"12:10:00"      :      "eatDinner",
	"12:30:00"		:	   "goHome",
	"14:00:00"		:	   "goToSchool",
	"17:00:00"		:	   "eatDinner",
	"17:20:00"      :      "goHome",
	"22:45:00"      :      "takeAShowerStart",
	"23:30:00"      :      "goToSleep"
}

weekendEventTimeList = {
	"08:55:00"      :      "wakeUp",
	"12:10:00"      :      "eatDinner",
	"12:30:00"		:	   "goHome",
	"17:00:00"      :      "eatDinner",
	"17:20:00"      :      "goHome",
	"22:45:00"      :      "takeAShowerStart",
	"23:59:00"      :      "goToSleep"
}


roomList = {
	"bathroom",
	"dormitory",
	"diningRoom",
	"outside"
}



# Time init
strStartTime = "2023 2 10 00:00:00"
startTime = time.mktime(time.strptime(strStartTime, "%Y %m %d %H:%M:%S"))

strEndTime = "2023 3 1 00:00:00"
endTime = time.mktime(time.strptime(strEndTime, "%Y %m %d %H:%M:%S"))

currentTime = startTime

# strOpenAirConditionTime = "2015 1 1 08:00:00"
# openTime = time.mktime(time.strptime(strOpenAirConditionTime, "%Y %m %d %H:%M:%S"))

# strCloseAirConditionTime = "2015 1 1 12:00:00"
# closeTime = time.mktime(time.strptime(strCloseAirConditionTime, "%Y %m %d %H:%M:%S"))

# fp = open('test.txt', 'w')

mainHouse = house(roomList = roomList, width = 30, height = 20,currentTime=currentTime)

person = human(0, 25, 50, 90, 95, 1, 3, currentTime)
two = human(1, 25, 50, 90, 95, 1, 3, currentTime)
three = human(2, 25, 50, 90, 95, 1, 3, currentTime)
four = human(3, 25, 50, 90, 95, 1, 3, currentTime)
five = human(4, 25, 50, 90, 95, 1, 3, currentTime)
humanlist = [person,two,three,four,five]
for i in range(len(humanlist)):
	humanlist[i].readHumanFromDB(ID =25)
	humanlist[i].initHouse(mainHouse)
	humanlist[i].initPos(0,0)
	humanlist[i].moveToRoom('dormitory')

# Event queue init
queues = []
for i in range(len(humanlist)):
	print(humanlist[i].getID())
	a = deque()
	queues.append(a)
print(len(queues))
# Event dispatch 计划事件分配
def timeEventDispatch(man):
	#man = random.choice(humanlist)
	# Time event
	week = int( time.strftime( "%w" , time.localtime(man.getCurrentTime() ) ) )
	if week <= 5:
		# 工作日计划事件
		if(weekdayEventTimeList.get(time.strftime("%H:%M:%S" , time.localtime(man.getCurrentTime())))  !=  None):
			eventType =  weekdayEventTimeList.get( time.strftime("%H:%M:%S" , time.localtime(man.getCurrentTime())) ) 
			newEvent = event(man.getCurrentTime(), eventType)
			queues[man.getID()].append(newEvent)
	else:
		# 周末计划事件
		if(weekendEventTimeList.get(time.strftime("%H:%M:%S" , time.localtime(man.getCurrentTime())))  !=  None):
			eventType =  weekendEventTimeList.get( time.strftime("%H:%M:%S" , time.localtime(man.getCurrentTime())) ) 
			newEvent = event(man.getCurrentTime(), eventType)
			queues[man.getID()].append(newEvent)

# Enviroment event 条件事件分配
def enviromentEventDispatch(man):
	#man = random.choice(humanlist)
	# 不在家时不分配事件
	if( not person.isInHome() ):
		return

	# 温度不适宜时开启空调调整温度
	if( (not man.getSimT().isTemperatureBeenSet()) and (man.getSimT().getCurrentTemperature() < 18 or man.getSimT().getCurrentTemperature() > 28) ):
		percent = timeSlot * 1.0 / (100*60) * man.getVigour()
		if (man.isSleeping()):
			percent *= 0.001
		if (random.uniform(0,100) < percent):
			newEvent = event(man.getCurrentTime(), "adjustTemprature")
			queues[man.getID()].append(newEvent)

	# 随机关闭空调
	if( man.isInHome() and (not man.isSleeping()) and man.getSimT().isTemperatureBeenSet() ):
		deltaTime = man.getCurrentTime() - man.getSimT().getTimeSetTemperature()
		if( deltaTime > 20 * 60 ):
			currentTemperature = man.getSimT().getCurrentTemperature()
			if( currentTemperature > 24 and currentTemperature < 26 ):
				# 依概率关闭空调
				percent = timeSlot * 1.0 / (400*60) * man.getVigour()
				# fp.write( time.strftime("%H:%M:%S", time.localtime(person.getCurrentTime())) + '	 %f\n' %percent)
				if(random.uniform(0,100) < percent):
					newEvent = event(man.getCurrentTime(), "turnOffAirCondition") 
					queues[man.getID()].append(newEvent)


	# 光照过暗时开灯
	if ( man.isInHome() and not man.isSleeping()):
		tempRoom = man.getNowRoom()
		try:
			if(tempRoom.roomType != 'dormitory'):
				return 
			if ( tempRoom.isDarkness(man.getCurrentTime()) ):
				if (random.randint(0,100) < 98):
					newEvent = event(man.getCurrentTime(), "turnOnLampInRoom")
					queues[man.getID()].appendleft(newEvent)
		except Exception as e:
			print(e)
			print("posX,posY",man.posX,man.posY)
			exit(0)

	# 关掉不在的房间的灯
	#if ( man.isInHome() and not man.isSleeping() ):
	#	percent = timeSlot * 1.0 / (3*60) * man.getVigour()
	#	if(random.uniform(0,100) < percent):
	#		newEvent = event(man.getCurrentTime(), "turnOffOtherRoomLamp")
	#		queues[man.getID()].appendleft(newEvent)

	# 如果当前没有事情，随机找事情做
	if (man.isInHome() and not man.isSleeping()):
		if( len(queues[man.getID()]) == 0 ):
			percent = timeSlot * 1.0 / ( random.randint(20,50) * 60) * man.getVigour()
			if (random.uniform(0,100) < percent):
				randomEventList = [ 'defaultEvent'] #待添加 TODO
				eventNum = random.randint(0, len(randomEventList)-1)
				newEvent = event(man.getCurrentTime(), randomEventList[eventNum])
				queues[man.getID()].append(newEvent)

	# 事件队列为空时，随机去卫生间
	if (man.isInHome() and not man.isSleeping()):
		if( len(queues[man.getID()]) == 0 ):
			percent = timeSlot * 1.0 / ( random.randint(30,700) * 60) * man.getVigour()
			if (random.uniform(0,100) < percent):
				newEvent = event(man.getCurrentTime(), "toiletStart")
				queues[man.getID()].append(newEvent)

	# print('eventDispatch', time.strftime("%Y %m %d %H:%M:%S" , time.localtime(currentTime)))

# Event manage 事件执行
def eventManage(man):
	#man = random.choice(humanlist)
	if( len(queues[man.getID()]) == 0 ):
		return
	tempEvent = queues[man.getID()].popleft()
	if(man.getCurrentTime() < tempEvent.getTimestamp()):
		queues[man.getID()].appendleft(tempEvent)
	else:
		nextEvent = tempEvent.eventRun(man)#事件引发的次生事件
		if(nextEvent != None):
			queues[man.getID()].appendleft(nextEvent)

from paintmod import paintMod

housePainter = paintMod()

paint_count = 0

person.add_colum_into_DB()

# Main loop
while(person.getCurrentTime() < endTime):
	
	# paint_count += 1
	# if paint_count % 1000 == 0:
	housePainter.drawHousePicture(mainHouse,humanlist)
		# paint_count = 0

	if(not housePainter.isRun()):
		continue
	
	mainHouse.iterateTime(timeSlot)
	mainHouse.iterateT(timeSlot)
	for person in humanlist:
		person.iterateTime(timeSlot)
		person.iterateT(timeSlot)
		timeEventDispatch(person)
		enviromentEventDispatch(person)
		eventManage(person)
	# fp.write( time.strftime("%H:%M:%S", time.localtime(person.getCurrentTime())) + '	' + str(person.getSimT().getCurrentTemperature()) + '\n')
	# person.writeNowStatu(fp)
	person.saveRecord()

	

print('end')

import os
os.system('pause')

