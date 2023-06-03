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



	def initHouse(self, house):
		self.house = house

	def initPos(self, posX = -1, posY = -1):
		import random
		#提供的坐标在房间范围内时直接赋值
		if( self.house.getRoomByPos(posX, posY) != None ):
			self.posX = posX
			self.posY = posY
			return
		#提供的坐标超出房间范围时随机赋值
		while( self.house.getRoomByPos(posX, posY) == None):
			self.posX = random.randint(0, self.house.getWidth() - 1)
			self.posY = random.randint(0, self.house.getHeight() - 1)
			return

	# 某些函数在对设备操作时会把人也移动到相应位置，确定是否要做到这一点

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

	# 打开一个房间内的某类属于某人设备
	def turnOnDeviceOfMan(self, roomType, deviceType, ID):
		tempDeviceList = self.house.turnOnDeviceByTypeOfMan(roomType, deviceType, ID)
		if(tempDeviceList != []):
			self.moveTo(tempDeviceList[0].getPosX(), tempDeviceList[0].getPosY())
		return tempDeviceList
	
	# 关闭一个房间内的某类属于某人的设备
	def turnOffDeviceOfMan(self, roomType, deviceType, ID):
		tempDeviceList = self.house.turnOffDeviceByTypeOfMan(roomType, deviceType, ID)
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

	#一些打开/关闭设备函数中是按类来对设备操作，确定是否要做到这一点

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

	# 打开所在房间 某人 的设备
	def turnOnDeviceInRoomOfMan(self, deviceType, ID):
		tempRoom = self.house.getRoomByPos(self.posX, self.posY)
		if (tempRoom != None):
			tempDeviceList = self.turnOnDeviceOfMan(tempRoom.getType(), deviceType, ID)
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
	
	# 关闭所在房间 某人 的设备
	def turnOffDeviceInRoomOfMan(self, deviceType, ID):
		tempRoom = self.house.getRoomByPos(self.posX, self.posY)
		if (tempRoom != None):
			tempDeviceList = self.turnOffDeviceOfMan(tempRoom.getType(), deviceType, ID)
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
	def getID(self):
		return self.ID 
	#获取X坐标
	def getPosX(self):
		return self.posX
	#获取Y坐标
	def getPosY(self):
		return self.posY
	#获取活力
	def getVigour(self):
		return self.vigour
	#设置活力
	def setVigour(self, vigour):
		self.vigour = vigour
	#获取生活规律性
	def getRegular(self):
		return self.regular
	#设置生活规律性
	def setRegular(self, regular):
		self.regular = regular
	#获取细心程度
	def getCarefulness(self):
		return self.carefulness
	#设置细心程度
	def setCarefulness(self, carefulness):
		self.carefulness = carefulness
	#获取当前时间
	def getCurrentTime(self):
		return self.currentTime
	#格式化获取当前时间
	def getCurrentTimeStr(self):
		return time.strftime("%H:%M:%S", time.localtime(self.getCurrentTime()))
	#设置当前时间
	def setCurrentTime(self, currentTime):
		self.currentTime = currentTime
	#获取温度
	def getSimT(self):
		return self.simT
	#获取房屋
	def getHouse(self):
		return self.house
	#获取坐标
	def getPos(self):
		return (self.getPosX(), self.getPosY())
	#获取是否在家
	def isInHome(self):
		return self.inHome
	#调整是否在家
	def leaveHome(self):
		self.inHome = False
		self.moveTo(25, 6)

	def goBackHome(self):
		self.inHome = True
	#设置是否随机移动
	def setRandomMove(self, isRandomMove = True):
		self.isRandomMove = isRandomMove
	#获取睡觉状态
	def isSleeping(self):
		return self.flagSleeping

	#调整睡觉状态
	def goToSleep(self):
		self.flagSleeping = True
		self.setRandomMove(False)
		self.moveTo(3,12)

	def wakeUp(self):
		self.flagSleeping = False
		self.setRandomMove(True)
	#获取当前所在房间
	def getNowRoom(self):
		return self.getHouse().getRoomByPos( self.getPosX(), self.getPosY() )
	#获取当前所在房间的类型
	def getNowRoomType(self):
		tempRoom = self.getHouse().getRoomByPos( self.getPosX(), self.getPosY() )
		if (tempRoom == None):
			return None
		else:	
			return tempRoom.getType()
	#打印当前人的状态（包括人所在位置的房屋地图）
	def printNowStatu(self):
		print('Time:	', self.getCurrentTimeStr(), '	Temperature:	', self.simT.getCurrentTemperature())
		houseMap = self.getHouse().printHouseInfo()
		houseMap[self.posY][self.posX] = 'M'
		for i in range(self.getHouse().getHeight()):
			for j in range(self.getHouse().getWidth()):
					print(houseMap[i][j],)
			print('')
	#输出当前人的状态（包括人所在位置的房屋地图）
	def writeNowStatu(self, fp):
		fp.write ('Time:	' + self.getCurrentTimeStr() + '	Temperature:	%f'  %self.simT.getCurrentTemperature() + '\n')
		houseMap = self.getHouse().printHouseInfo()
		houseMap[self.posY][self.posX] = 'M'
		for i in range(self.getHouse().getHeight()):
			for j in range(self.getHouse().getWidth()):
					fp.write(houseMap[i][j])
			fp.write('\n')
	#获取有人所在位置的房屋地图
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
				#self.ID            = int(temp.get("ID"))
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
		except Exception as error:
			print(error)
			print("sql \n Error!",sql)
			exit(0)
		return True