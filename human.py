# -*- coding: utf-8 -*-

from devices import device
from temperature import temperatureSimulator
from houses import house
import time
from sqlManage import SQLManagement

class human:
	# age         =   20
	# vigour      =   50
	# # diligence   =   50
	# regular     =   90
	# carefulness =   95
	# humanID     =   0
	# posX        =   0
	# posY        =   0
	# deviceList  =   []
	# currentTime =   time.mktime(time.strptime("2015 1 1 00:00:00", "%Y %m %d %H:%M:%S"))
	# simT        =   temperatureSimulator(currentTime)
	# inHome      =   True

	roomDict    =   {
		"livingRoom"           :           0,
		"masterBedroom"        :           100,
		"secondBedroom"        :           200,
		"thirdBedroom"         :           300,
		"bathroom"             :           400,
		"kitchen"              :           500,
		"diningRoom"           :           600,
		"studyRoom"            :           700
	}

	# 初始化函数
	def __init__(self, ID = -1, age = 25, vigour = 50, regular = 90, carefulness = 95, posX = 0, posY = 0, currentTime = time.mktime(time.strptime("2015 1 1 00:00:00", "%Y %m %d %H:%M:%S")) ):
		self.ID           =         ID
		self.age          =         age

		# 用户活力
		self.vigour       =         vigour

		# self.diligence    =         diligence

		# 生活规律性
		self.regular      =         regular

		# 细心程度
		self.carefulness  =         carefulness

		# 用户位置
		self.posX         =         posX
		self.posY         =         posY

		# 时间
		self.currentTime  =         currentTime

		# 气温模拟器
		self.simT         =         temperatureSimulator(self.currentTime)

		# 是否在家
		self.inHome       =         True

		# 是否在室内随机移动
		self.isRandomMove =         False

		# 是否睡觉
		self.flagSleeping =         True

		self.count        =         0

		# 数据库连接
		self.sqlMana      =         SQLManagement(db = 'humansimulator')



	def initHouse(self, ID = -1, roomList = [], width = 20, height = 20):
		self.house = house(ID, roomList, width, height)

	def initPos(self, posX = -1, posY = -1):
		import random
		if( self.house.getRoomByPos(posX, posY) != None ):
			self.posX = posX
			self.posY = posY
			return
		while( self.house.getRoomByPos(posX, posY) == None):
			self.posX = random.randint(0, self.house.getWidth() - 1)
			self.posY = random.randint(0, self.house.getHeight() - 1)
			return

	# 打开一个房间内的某类设备
	def turnOnDevice(self, roomType, deviceType):
		tempDeviceList = self.house.turnOnDeviceByType(roomType, deviceType)
		if(tempDeviceList != []):
			self.moveTo(tempDeviceList[0].getPosX(), tempDeviceList[0].getPosY())
		return tempDeviceList

	# 关闭一个房间内的某类设备
	def turnOffDevice(self, roomType, deviceType):
		tempDeviceList = self.house.turnOffDeviceByType(roomType, deviceType)
		if(tempDeviceList != []):
			self.moveTo(tempDeviceList[0].getPosX(), tempDeviceList[0].getPosY())
		return tempDeviceList

	# 打开指定设备名的设备
	def turnOnDeviceByDeviceName(self, roomType, deviceName):
		tempDevice = self.house.turnOnDeviceByName(roomType, deviceName)
		if(tempDevice != None):
			self.moveTo(tempDevice.getPosY(), tempDevice.getPosY)
		return tempDevice

	# 关闭指定设备名的设备
	def turnOffDeviceByDeviceName(self, roomType, deviceName):
		return self.house.turnOffDeviceByName(roomType, deviceName)

	# 改变指定房间指定设备的值
	def setDevice(self, roomType, deviceType, value):
		return self.house.setDeviceValueByType(roomType, deviceType, value)

	# 关闭指定类型的全部设备
	def turnOffAllByDeviceType(self, deviceType, exceptRoomTypeList = []):
		self.house.turnOffAllByDeviceType(deviceType, exceptRoomTypeList)

	# 打开属于某个人的某种类型的设备
	def turnOnDeviceInRoomOfManSelf(self, deviceType ):
		self.house.turnOnAllByDeviceTypeAndOnwner(self.ID, deviceType)

	# 关闭属于某个人的某种类型的设备
	def turnOffDeviceInRoomOfManSelf(self, deviceType ):
		self.house.turnOffAllByDeviceTypeAndOnwner(self.ID, deviceType)

	# 移动到某位置
	def moveTo(self, posX, posY):
		if ( posX < self.house.getWidth() and posY < self.house.getHeight() ):
			self.posX             =         posX
			self.posY             =         posY
			return True
		else:
			return False

	# 移动至某房间
	def moveToRoom(self, roomType):
		for tempRoom in self.house.getRoomList():
			if ( tempRoom.getType() == roomType ):
				import random
				left = tempRoom.getLeft()
				right = tempRoom.getRight()
				top = tempRoom.getTop()
				bottom = tempRoom.getBottom()
				tempX = ( random.randint(left, right) + random.randint(left, right) ) / 2
				tempY = ( random.randint(top, bottom) + random.randint(top, bottom) ) / 2
				self.moveTo(tempX, tempY)
		return False

	# 在房间内随机移动一次
	def moveRandomInRoom(self):
		import random
		if (self.isRandomMove):
			tempRoom = self.getHouse().getRoomByPos(self.posX, self.posY)
			if( tempRoom != None ):
				left = tempRoom.getLeft()
				right = tempRoom.getRight()
				top = tempRoom.getTop()
				bottom = tempRoom.getBottom()
				tempX = ( random.randint(left, right) + random.randint(left, right) ) / 2
				tempY = ( random.randint(top, bottom) + random.randint(top, bottom) ) / 2
				self.moveTo(tempX, tempY)
				return True
			else:
				return False

	# # 关闭所有电灯
	# def turnOffAllLight(self):
	# 	print('Turn off all lights.')
	# 	self.turnOffAllByDeviceType('lamp')

	# # 打开指定房间的电视
	# def turnOnTV(self, roomName):
	# 	print('Turn on TV.')
		

	# # 关闭指定房间的电视
	# def turnOffTV(self, roomName):
	# 	print('Turn off TV.')
	# 	self.turnOffDevice(roomName, 'TV')

	# 关闭所有电视
	# def turnOffAllTV(self):
	# 	print('Turn off all TVs.')
	# 	self.turnOffAllByDeviceType('TV')

	# 打开所在房间的设备
	def turnOnDeviceInRoom(self, deviceType):
		tempRoom = self.house.getRoomByPos(self.posX, self.posY)
		if (tempRoom != None):
			tempDeviceList = self.turnOnDevice(tempRoom.getType(), deviceType)
			if ( tempDeviceList !=[] ):
				tempDevice = tempDeviceList[0]
				self.moveTo( tempDevice.getPosX(), tempDevice.getPosY() )
				# print('Turn on ', deviceType, ' in ', tempRoom.getType())
				return True
			else:
				return False
		else:
			print('Not in any room')
			return False

	# 关闭所在房间的设备
	def turnOffDeviceInRoom(self, deviceType):
		tempRoom = self.house.getRoomByPos(self.posX, self.posY)
		if (tempRoom != None):
			tempDeviceList = self.turnOffDevice(tempRoom.getType(), deviceType)
			if (tempDeviceList != [] ):
				tempDevice = tempDeviceList[0]
				self.moveTo( tempDevice.getPosX(), tempDevice.getPosY() )
				# print('Turn off ', deviceType, ' in ', tempRoom.getType())
				return True
			else:
				return False
		else:
			print('Not in any room')
			return False

	# 设定所在房间的指定设备的值
	def setDeviceValueInRoom(self, deviceType, value):
		tempRoom = self.house.getRoomByPos(self.posX, self.posY)
		if (tempRoom != None):
			tempDeviceList = self.setDevice(tempRoom.getType(), deviceType, value)
			if ( tempDeviceList != [] ):
				tempDevice = tempDeviceList[0]
				self.moveTo( tempDevice.getPosX(), tempDevice.getPosY() )
				# print('Set ', tempDeviceList[0].getName(), ' to ', value, ' in ', tempRoom.getType())
				return True
			else:
				return False
		else:
			print('Not in any room')
			return False

	# 打开距离最近的某类设备
	def turnOnNearDevice(self, deviceType):
		tempDevice = self.house.turnOnNearDevice(self.posX, self.posY, deviceType)
		if (tempDevice != None):
			self.moveTo(tempDevice.getPosX(), tempDevice.getPosY())
			# print('Turn on ', tempDevice.getName())
			return True
		else:
			print('There isn\'t any ', deviceType)
			return False

	# 关闭距离最近的某类设备
	def turnOffNearDevice(self, deviceType):
		tempDevice = self.house.turnOffNearDevice(self.posX, self.posY, deviceType)
		if ( tempDevice != None ):
			self.moveTo(tempDevice.getPosX(), tempDevice.getPosY())
			# print('Turn off ', tempDevice.getName())
			return True
		else:
			print('There isn\'t any ', deviceType)
			return False

	# 设定距离最近指定设备的值
	def setNearDeviceValue(self, deviceType, value):
		tempDevice = self.house.setNearDeviceValue(self.posX, self.posY, deviceType, value)
		if ( tempDevice != None ):
			self.moveTo(tempDevice.getPosX(), tempDevice.getPosY())
			# print('Set ', tempDevice.getName())
			return True
		else:
			print('There isn\'t any ', deviceType)
			return False

	# # 打开附近的空调并设定温度(待修改)
	# def turnOnNearAirCondition(self, destinationTemperature):
	# 	minDis = 100000
	# 	tempDev = self.deviceList[0]
	# 	for dev in self.deviceList:
	# 		if(dev.getType() == 'airCondition' and dev.calDistance(self.posX, self.posY) <= minDis):
	# 			tempDev = dev
	# 			minDis = dev.calDistance(self.posX, self.posY)
	# 	if(minDis < 100000):
	# 		tempDev.turnOn()
	# 		tempDev.setValue(destinationTemperature)
	# 		print('Turn on ', dev.getName(), ' and set destination temperature to ', destinationTemperature)
	# 	else:
	# 		print('There is not any air condition.')






	# # 关闭所有空调
	# def turnOffAllAirCondition(self):
	# 	print('Turn off all air condition.')
	# 	self.turnOffAllByDeviceType('airCondition')

	# 打开附近的电视（待修改）
	# def turnOnNearTV(self):
	# 	minDis = 100000
	# 	tempDev = self.deviceList[0]
	# 	for dev in self.deviceList:
	# 		if(dev.getType() == 'TV' and dev.calDistance(self.posX, self.posY) <= minDis):
	# 			tempDev = dev
	# 			minDis = dev.calDistance(self.posX, self.posY)
	# 	if(minDis < 100000):
	# 		tempDev.turnOn()
	# 		print('Turn on ', dev.getName())
	# 	else:
	# 		print('There is not any TV.')

	# def turnOnDeskLamp(self, room):
		# print('Turn on desk lamp.')

	# def turnOffDeskLamp(self, room):
		# print('Turn off desk lamp.')

	# def turnOnLivingRoomLamp(self):
	# 	print('Turn on the lamp of living room.')

	# def turnOffLivingRoomLamp(self):
	# 	print('Turn off the lamp of living room.')

	# def turnOnBedRoomLamp(self):
	# 	print('Turn on the lamp of bedroom.')

	# def turnOffBedRoomLamp(self):
	# 	print('Turn off the lamp of bedroom.')

	# 打开指定房间的电脑（待修改）
	# def turnOnComputer(self, roomName):
	# 	print('Turn on computer.')
	# 	roomBaseNum = self.roomDict.get(roomName)
	# 	for dev in self.deviceList: 
	# 		if(dev.getId() >= roomBaseNum and dev.getId() < roomBaseNum + 100 and dev.getType() == 'TV'):
	# 			dev.turnOff()

	# def turnOffComputer(self, room):
	# 	print('Turn off computer.')

	# def turnOnHeater(self, room):
	# 	print('Turn on water heater.')

	# def turnOffWaterHeater(self, room):
	# 	print('Turn off water heater.')

	# def openHomeDoor(self):
	# 	print('Open the home door.')

	# def closeHomeDoor(self):
	# 	print('Close the home door.')

	def getPosX(self):
		return self.posX

	def getPosY(self):
		return self.posY

	def getVigour(self):
		return self.vigour

	def setVigour(self, vigour):
		self.vigour = vigour

	def getRegular(self):
		return self.regular

	def setRegular(self, regular):
		self.regular = regular

	def getCarefulness(self):
		return self.carefulness

	def setCarefulness(self, carefulness):
		self.carefulness = carefulness

	def getCurrentTime(self):
		return self.currentTime

	def getCurrentTimeStr(self):
		return time.strftime("%H:%M:%S", time.localtime(self.getCurrentTime()))

	def setCurrentTime(self, currentTime):
		self.currentTime = currentTime

	def getSimT(self):
		return self.simT

	def getHouse(self):
		return self.house

	def getPos(self):
		return (self.getPosX(), self.getPosY())

	def isInHome(self):
		return self.inHome

	def leaveHome(self):
		self.inHome = False
		self.moveTo(0, 0)

	def goBackHome(self):
		self.inHome = True

	def setRandomMove(self, isRandomMove = True):
		self.isRandomMove = isRandomMove

	def isSleeping(self):
		return self.flagSleeping

	def goToSleep(self):
		self.flagSleeping = True
		self.setRandomMove(False)

	def wakeUp(self):
		self.flagSleeping = False
		self.setRandomMove(True)

	def getNowRoom(self):
		return self.getHouse().getRoomByPos( self.getPosX(), self.getPosY() )

	def getNowRoomType(self):
		tempRoom = self.getHouse().getRoomByPos( self.getPosX(), self.getPosY() )
		if (tempRoom == None):
			return None
		else:	
			return tempRoom.getType()

	def printNowStatu(self):
		print('Time:	', self.getCurrentTimeStr(), '	Temperature:	', self.simT.getCurrentTemperature())
		houseMap = self.getHouse().printHouseInfo()
		houseMap[self.posY][self.posX] = 'M'
		for i in range(self.getHouse().getHeight()):
			for j in range(self.getHouse().getWidth()):
					print(houseMap[i][j],)
			print('')

	def writeNowStatu(self, fp):
		fp.write ('Time:	' + self.getCurrentTimeStr() + '	Temperature:	%f'  %self.simT.getCurrentTemperature() + '\n')
		houseMap = self.getHouse().printHouseInfo()
		houseMap[self.posY][self.posX] = 'M'
		for i in range(self.getHouse().getHeight()):
			for j in range(self.getHouse().getWidth()):
					fp.write(houseMap[i][j])
			fp.write('\n')

	def getMap(self):
		houseMap = self.getHouse().printHouseInfo()
		houseMap[self.posY][self.posX] = 'M'
		return houseMap

	# 温度模拟器迭代一次
	def iterateT(self, timeSlot):
		self.simT.iterate(self.currentTime, timeSlot)

	# 时间迭代器迭代一次
	def iterateTime(self, timeSlot):
		self.currentTime = self.currentTime + timeSlot

		# 随机移动
		if(self.isInHome()):
			if(self.isRandomMove):
				import random
				percent = timeSlot * 1.0 / (30*60) * self.getVigour()
				if ( random.uniform(0,100) < percent):
					self.moveRandomInRoom()

		# # 打印信息
		# import os
		# self.count = self.count + 1
		# if (self.count == 20):
		# 	self.count = 0
		# 	# os.system('cls')
		# 	self.printNowStatu()
		# 	# self.writeNowStatu(fp)


	# 从数据库读取个人信息
	def readHumanFromDB(self, ID = None):
		if( ID == None ):
			return False
		else:
			# 读数据
			sql = 'select * from human where ID = %d' %ID
			res = self.sqlMana.query(sql)
			if(len(res) < 1):
				return False
			else:
				temp = res[0]
				self.ID            = int(temp.get("ID"))
				self.age           = int(temp.get("age"))
				self.vigour        = int(temp.get("vigour"))
				self.regular       = int(temp.get("regular"))
				self.carefulness   = int(temp.get("carefulness"))
				self.posX          = float(temp.get("posX"))
				self.posY          = float(temp.get("posY"))
				self.inHome        = bool(temp.get("inHome"))
				self.isRandomMove  = bool(temp.get("isRandomMove"))
				self.flagSleeping  = bool(temp.get("flagSleeping"))
				self.house         = house()
				self.initHouseFromDB()
				return True

	# 存储个人信息到数据库
	def saveInfoToDB(self):
		sql = "select * from human where ID = %d" %self.ID
		res = self.sqlMana.query(sql)
		if(len(res) > 0):
			sql = "update human set age = %d, vigour = %d, regular = %d, carefulness = %d, posX = %lf, posY = %lf, inHome = %d,  isRandomMove = %d, flagSleeping = %d where ID = %d" %(self.age, self.vigour, self.regular, self.carefulness, self.posX, self.posY, self.inHome, self.isRandomMove, self.flagSleeping ,self.ID)
			self.sqlMana.update(sql)
		else:
			sql = "insert into human (age, vigour, regular, carefulness, posX, posY, inHome, isRandomMove, flagSleeping) values (%d, %d, %d, %d, %lf, %lf, %d, %d, %d)" %(self.age, self.vigour, self.regular, self.carefulness, self.posX, self.posY, self.inHome, self.isRandomMove, self.flagSleeping)
			self.sqlMana.insert(sql)
			temp = self.sqlMana.query('select @@identity as newID')
			self.ID = temp[0].get('newID')
		return self.house.saveInfoToDB(humanID = self.ID, sqlMana = self.sqlMana)
		

	# 通过数据库初始化住房
	def initHouseFromDB(self):
		sql = 'select ID from house where humanID = %d' %self.ID
		res = self.sqlMana.query(sql)
		temp = res[0]
		self.house.readInfoFromDB(ID = temp.get('ID'), sqlMana = self.sqlMana)
	
	# 向数据库record 中插入新的列
	def add_colum_into_DB(self):
		column_names = [item for (item,value) in self.house.getInfo(self.currentTime).items()]
		for column in column_names:
			try:
				self.sqlMana.insert("alter table record add column %s int(32) not null"%column)
			except:
				print("%s define twice.\n",column)
		return None

	# 存储一条记录
	def saveRecord(self):
		res = {
			'humanID'       : self.ID,
			'temperature'   : self.simT.getCurrentTemperature(),
			'posX'          : self.getPosX(),
			'posY'          : self.getPosY()
		}
		res =  dict( res.items() + self.house.getInfo(self.currentTime).items() )

		sql = "insert into record ("

		for (item, value) in res.items():
			sql = sql + item
			sql = sql + ','
		sql = sql + 'recTime) values ('

		for (item, value) in res.items():
			sql = sql + str(value)
			sql = sql + ','
		timeStr = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(self.getCurrentTime()))
		sql = sql + "'"
		sql = sql + timeStr
		sql = sql + "')"
		try:
			self.sqlMana.insert(sql)
		except:
			print("sql \n Error!",sql)
			exit(0)
		return True