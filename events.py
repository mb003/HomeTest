# -*- coding: utf-8 -*-

import time
import random

class event:

	# 上学事件（计划事件）
	def goToSchool(self, man):
		if(not man.isInHome()):
			return None
		print('\nRule:	go to school.')
		if(random.uniform(0,100) < man.getCarefulness()):
			man.turnOffAllByDeviceType("lamp")
		if(random.uniform(0,100) < man.getCarefulness() ):
			man.turnOffAllByDeviceType("airCondition")
			man.getSimT().setTemperatureOff()
		if(random.uniform(0,100) < man.getCarefulness() ):
			man.turnOffAllByDeviceType("computer")
		
		#没有TV
		# if(random.uniform(0,100) < man.getCarefulness() ):
		# 	man.turnOffAllByDeviceType("TV")
		
		self.turnOffAllSundries(man)
		man.turnOnDevice("dormitory", "door")
		man.turnOffDevice("dormitory", "door")
		man.leaveHome()
		return None

	# 回家事件（计划事件）
	def goHome(self, man):
		print('\nRule:	go home.')
		man.goBackHome()
		man.turnOnDevice('dormitory', 'door')
		if(random.uniform(0,100) < man.getVigour()):
			man.turnOnDevice('dormitory', 'lamp')
		if(random.uniform(0,100) < man.getRegular()):
			man.turnOnDevice('dormitory', 'TV')
		return None

	# 睡觉事件（计划事件）
	def goToSleep(self, man):
		if(not man.isInHome()):
			return None
		print('\nRule:	go to sleep.')
		# if(random.uniform(0,100) < man.getCarefulness() ):
		self.turnOffAllSundries(man)
		if(random.uniform(0,100) < man.getCarefulness() ):
			man.turnOffDevice('dormitory', 'door')
		if(random.uniform(0,100) < man.getCarefulness() ):
			man.turnOffAllByDeviceType('lamp')
		if(random.uniform(0,100) < man.getVigour()):
			man.turnOffAllByDeviceType('lamp')
		man.goToSleep()
		return event( man.getCurrentTime() + 5*60*60, "defaultEvent" )


	# 调整室温事件
	def adjustTemprature(self, man):
		if(not man.isInHome()):
			return None
		print('\nRule:	adjust Temprature.')
		man.getSimT().setTemperatureOn(25)
		man.turnOnDeviceInRoom("airCondition")
		if ( man.setDeviceValueInRoom("airCondition", 25) ):
			return None
		else:
			man.setNearDeviceValue("airCondition", 25)
			return None

	# 起床事件（计划事件）
	def wakeUp(self, man):
		if(not man.isInHome()):
			return None
		print('\nRule:	wake up.')
		man.wakeUp()
		#人体传感器检测到人体移动，在下面桌子上
		man.turnOnDevice('dormitory','humanSensor')
		#太暗了就开灯，这个灯是共用灯
		if(man.getNowRoom().isDarkness(man.getCurrentTime())):
			self.turnOnLampInRoom(man)
		#开门，去刷牙
		man.turnOnDevice('dormitory', 'door')
		man.turnOffDevice('dormitory', 'door')
		man.moveTo('bathroom')
		#刷牙, 2-15分钟
		lockEvent = event(man.getCurrentTime() + random.randint(2, 15)*60, "defaultEvent")
		#刷完牙回寝
		man.turnOnDevice('dormitory', 'door')
		man.turnOffDevice('dormitory', 'door')
		man.moveTo('dormitory')
		return lockEvent

	# 读书事件（计划事件）
	def readBook(self, man):
		if(not man.isInHome()):
			return None
		self.turnOffDevicesListInRoom(man = man)
		if(random.randint(0,100) > man.getRegular() ):
			# 较小概率去看电视或打游戏
			if (random.randint(0,100) < man.getVigour()):
				return event(man.getCurrentTime(), "playVideoGame")
			else:
				return event(man.getCurrentTime(), "watchTV")
		if(man.getHouse().roomExist('studyRoom')):
			print('\nRule:	read book start.')
			man.turnOnDevice('studyRoom', 'door')
			if(random.uniform(0,100) < 20):
				man.turnOnDeviceByDeviceName('studyRoom', 'studyRoomCeilingLamp')
			man.turnOnDeviceByDeviceName('studyRoom', 'studyRoomDeskLamp')
			if(random.uniform(0,100) < 5):
				man.turnOnDeviceByDeviceName('studyRoom', 'studyRoomAudioSystem')
			if(random.uniform(0,100) < 50):
				man.turnOffDevice('studyRoom', 'door')
			man.moveToRoom('studyRoom')
			lockEvent = event(man.getCurrentTime() + random.randint(15, 40)*60, "defaultEvent")
			return lockEvent
		else:
			print('There is not any studyRoom')
			return None

	# 玩游戏（计划事件）
	def playVideoGame(self, man):
		if(not man.isInHome()):
			return None
		man.turnOnDeviceInRoom('computer')
		return None

	# 吃饭（计划事件）
	def eatDinner(self, man):
		if(not man.isInHome()):
			return None
		print('\nRule:	eat dinner.')
		#去吃饭，关掉自己的设备后出寝室，到达食堂
		self.turnOffDevicesListOfManSelf(man = man)
		if( man.getHouse().roomExist('diningRoom') ):
			man.moveToRoom('diningRoom')
			lockEvent = event(man.getCurrentTime() + 15*60 + random.randint(0, 15) * 60, "defaultEvent" )
			return lockEvent
		else:
			man.moveToRoom('')
			lockEvent = event(man.getCurrentTime() + 15*60 + random.randint(0, 15) * 60, "defaultEvent" )
			if( man.getNowRoom().isDarkness(man.getCurrentTime()) ):
				man.turnOnLampInRoom(man)
			return lockEvent
		return None

	# 打开房间的灯
	def turnOnLampInRoom(self, man):
		if(not man.isInHome()):
			return None
		print('\nRule:	turn on lamp in room.')
		tempX = man.getPosX()
		tempY = man.getPosY()
		man.turnOnDeviceInRoom('lamp')
		man.moveTo(tempX, tempY)
		return None

	# 关闭其他房间的灯
	def turnOffOtherRoomLamp(self, man):
		if(not man.isInHome()):
			return None
		# print('\nRule:	turn off lamps in other rooms.')
		if( random.randint(0, 100) < man.getCarefulness() ):
			tempX = man.getPosX()
			tempY = man.getPosY()
			nowRoomType = man.getNowRoomType()
			exceptRoomTypeList = []
			exceptRoomTypeList.append(nowRoomType)
			man.turnOffAllByDeviceType('lamp', exceptRoomTypeList)
			man.moveTo(tempX, tempY)

    # 打开所在房间的某类设备并回到原位
	def turnOnDeviceInRoom(self, man, deviceType):
		if(not man.isInHome()):
			return None
		print('\nRule:	turn on %s in room.' %deviceType)
		tempX = man.getPosX()
		tempY = man.getPosY()
		man.turnOnDeviceInRoom(deviceType)
		man.moveTo(tempX, tempY)
		return None

	# 关闭所在房间的指定列表的设备
	def turnOffDevicesListInRoom(self, man, deviceTypeList = ['lamp', 'TV', 'computer', 'heater', 'charger', 'other']):
		if(not man.isInHome()):
			return None
		tempX = man.getPosX()
		tempY = man.getPosY()
		for tempDeviceType in deviceTypeList:
			man.turnOffDeviceInRoom(tempDeviceType)
		man.moveTo(tempX, tempY)
		return None
	
	#关闭寝室里的属于自己的设备
	def turnOffDevicesListOfManSelf(self,man,deviceTypeList = ['lamp','computer','other',]):
		if(not man.isInHome()):
			return None
		tempX = man.getPosX()
		tempY = man.getPosY()
		for tempDeviceType in deviceTypeList:
			#属于自己,或者别人临时授权了
				man.turnOffDeviceInRoomOfManSelf(tempDeviceType)
		man.moveTo(tempX, tempY)
		return None

	# 打开窗户(待修改)
	def openWindow(self, man):
		if(not man.isInHome()):
			return None
		print('Rule:    open the window in the room which the man in')
		tempX = man.getPosX()
		tempY = man.getPosY()
		man.turnOnDeviceInRoom('window')
		man.moveTo(tempX, tempY)
		return None

	# 关闭窗户(待修改)
	def closeWindow(self, man):
		if(not man.isInHome()):
			return None
		print('Rule:    close the window in the room which the man in')
		tempX = man.getPosX()
		tempY = man.getPosY()
		man.turnOffDeviceInRoom('window')
		man.moveTo(tempX, tempY)
		return None

	# 开始洗澡事件（计划事件）
	def takeAShowerStart(self, man):
		if(not man.isInHome()):
			return None
		print('Rule:	take a shower start.')
		if( man.getHouse().roomExist('bathroom') ):
			man.turnOnDevice('dormitory', 'door')
			man.turnOffDevice('dormitory', 'door')
			man.moveToRoom('bathroom')
			showerTime = 10 + random.randint( int(8 * man.getRegular()/100.0),  int(8 + 8 * (1.0 - man.getRegular()/100.0)) ) 
			lockEvent = event(man.getCurrentTime() + showerTime*60, "takeAShowerEnd" )
			return lockEvent
		else:
			print('There is not any bathroom.')
			return None

	# 洗澡结束
	def takeAShowerEnd(self, man):
		if(not man.isInHome()):
			return None
		print('Rule:	take a shower end')
		if( man.getHouse().roomExist('bathroom') ):
			man.turnOnDevice('dormitory', 'door')
			if(random.uniform(0,100) < man.getCarefulness()):
				man.turnOffDevice('dormitory', 'door')
			man.moveToRoom('dormitory')
			return None
		else:
			print('There is not any bathroom.')
			return None

	# 如厕事件
	def toiletStart(self, man):
		print('Rule:	go to toilet.')
		if( man.getHouse().roomExist('bathroom') ):
			man.turnOnDevice('dormitory', 'door')
			if (random.uniform(0,100) < man.getCarefulness()):
				man.turnOffDevice('dormitory', 'door')
			toiletTime = 2 + random.randint( int(4 * man.getRegular()/100.0),  int(4 + 4 * (1.0 - man.getRegular()/100.0)) ) 
			lockEvent = event(man.getCurrentTime() + toiletTime*60, "toiletEnd", man.getPosX(), man.getPosY() )
			return lockEvent
		else:
			print('There is not any bathroom.')
			return None

	# 如厕结束事件
	def toiletEnd(self, man):
		print('Rule:	end of toilet.')
		man.turnOnDevice('dormitory', 'door')
		if(random.uniform(0,100) < man.getCarefulness()):
			man.turnOffDevice('dormitory', 'door')
		man.moveTo(self.recordPosX, self.recordPosY)
		return None

	# 默认事件，什么都不做
	def defaultEvent(self, man):
		# print('Rule:	default event.')
		return None

	# 关闭空调事件
	def turnOffAirCondition(self, man):
		if( not man.isInHome() ):
			return None
		# print('Rule:    turn off air condition')
		tempRoomType = man.getNowRoomType()
		man.turnOffAllByDeviceType("airCondition")
		man.getSimT().setTemperatureOff()
		if(tempRoomType != None):
			man.moveToRoom(tempRoomType)
		return event()



	# 关闭所有杂项电器（包括 TV, computer, charger, heater, other）
	def turnOffAllSundries(self, man):
		if( not man.isInHome() ):
			return None
		# print('Rule:	turn off all sundries')
		tempRoomType = man.getNowRoomType()
		man.turnOffAllByDeviceType("computer")
		man.turnOffAllByDeviceType("charger")
		man.turnOffAllByDeviceType("other")
		if( tempRoomType != None ):
			man.moveToRoom(tempRoomType)
		return None

	info        =        {
		"goToSchool"          :        goToSchool,
		"goHome"              :        goHome,
		"goToSleep"           :        goToSleep,
		"wakeUp"              :        wakeUp,
		"readBook"            :        readBook,
		"takeAShowerStart"    :        takeAShowerStart,
		"takeAShowerEnd"      :        takeAShowerEnd,
		"watchTV"             :        watchTV,
		"eatDinner"           :        eatDinner,
		"cook"                :        cook,
		"adjustTemprature"    :        adjustTemprature,
		"toiletStart"         :        toiletStart,
		"toiletEnd"           :        toiletEnd,
		# "turnOnAirCondition"  :        turnOnAirCondition,
		"turnOffAirCondition" :        turnOffAirCondition,
		"turnOnLampInRoom"    :        turnOnLampInRoom,
		"turnOffAllTV"        :        turnOffAllTV,
		"turnOffAllSundries"  :        turnOffAllSundries,
		"playVideoGame"       :        playVideoGame,
		"turnOffOtherRoomLamp":        turnOffOtherRoomLamp,
		"defaultEvent"        :        defaultEvent
	}

	def __init__(self,timestamp =  time.mktime(time.strptime("2000 1 1 00:00:00", "%Y %m %d %H:%M:%S")), eventType = "defaultEvent", posX = 0, posY = 0):
		self.timestamp      =      timestamp
		self.eventType      =      eventType
		self.recordPosX     =      posX
		self.recordPosY     =      posY
		# self.isLocked       =      isLocked

	def getTimestamp(self):
		return self.timestamp

	def eventRun(self, man):
		# print('eventRun:     ', self.eventType)
		return self.info.get(self.eventType)(self, man)