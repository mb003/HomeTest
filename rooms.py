# -*- coding: utf-8 -*-
import time
from devices import device
from light import lightSimulator
from sqlManage import SQLManagement

class room:


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


	def __init__(self, ID = -1, roomType = 'None', roomLeft = 0, roomRight = 0, roomTop = 0, roomBottom = 0):
		# print('in __init__ of room')
		
		# self.roomType   = self.roomDict.get(roomType)
		self.ID         = ID
		self.setType(roomType)
		self.roomLeft   = roomLeft
		self.roomRight  = roomRight
		self.roomTop    = roomTop
		self.roomBottom = roomBottom
		self.deviceList = []
		self.simL       = lightSimulator()
		# self.initDeviceList()

	# def antiRoomDict(self, roomType):
	# 	for i in roomDict:
	# 		if (roomType == self.roomDict.get(i)):
	# 			return i

	def printInfo(self):
		print("Room type:	", self.roomType)
		print("Room left:	", self.roomLeft)
		print("Room right:	", self.roomRight)
		print("Room top:	", self.roomTop)
		print("Room bottom:	", self.roomBottom)

	def getID(self):
		return self.ID

		def isInRoom(self, posX, posY):
			return ( posX <= self.roomRight and  posX >= self.roomLeft and posY <= self.roomBottom and posY >= self.roomTop )

	def getLeft(self):
		return self.roomLeft

	def setLeft(self, roomLeft):
		self.roomLeft = roomLeft

	def getRight(self):
		return self.roomRight

	def setRight(self, roomRight):
		self.roomRight = roomRight

	def getBottom(self):
		return self.roomBottom

	def setBottom(self, roomBottom):
		self.roomBottom = roomBottom

	def getTop(self):
		return self.roomTop

	def setTop(self, roomTop):
		self.roomTop = roomTop

	def getType(self):
		return self.roomType

	def setType(self, roomType):
		if (self.roomDict.get(roomType) == None):
			self.roomType = None
		else:
			self.roomType = roomType
		# self.initDeviceList();

	def getSquare(self):
		dx = self.roomRight  - self.roomLeft + 1
		dy = self.roomBottom - self.roomTop  + 1
		square = dx * dy
		return square

	def getDeviceList(self):
		return self.deviceList

	def initDeviceList(self):
		# print('in initDeviceList:	', self.getType())
		# Livingroom
		if (self.roomType == 'livingRoom'):
			livingRoomTV             = device(0, 'livingRoomTV', 'TV', 0, 0)
			self.deviceList.append(livingRoomTV)

			livingRoomLamp           = device(1, 'livingRoomLamp', 'lamp', 0, 0)
			self.deviceList.append(livingRoomLamp)

			livingRoomDoor           = device(2, 'livingRoomDoor', 'door', 0, 0)
			self.deviceList.append(livingRoomDoor)

			livingRoomWindow         = device(3, 'livingRoomWindow', 'window', 0, 0)
			self.deviceList.append(livingRoomWindow)

			livingRoomComputer       = device(4, 'livingRoomComputer', 'computer', 0, 0)
			self.deviceList.append(livingRoomComputer)

			livingRoomCharger        = device(5, 'livingRoomCharger', 'charger', 0, 0)
			self.deviceList.append(livingRoomCharger)

			livingRoomAirCondition   = device(6, 'livingRoomAirCondition', 'airCondition', 0, 25)
			self.deviceList.append(livingRoomAirCondition)

			livingRoomAudioSystem    = device(7, 'livingRoomAudioSystem', 'other', 0, 0)
			self.deviceList.append(livingRoomAudioSystem)

		# Master Bedroom
		if (self.roomType == 'masterBedroom'):
			masterBedRoomTV          = device(100, 'masterBedRoomTV', 'TV', 0, 0)
			self.deviceList.append(masterBedRoomTV)

			masterBedRoomCeilingLamp = device(101, 'masterBedRoomCeilingLamp', 'lamp', 0, 0)
			self.deviceList.append(masterBedRoomCeilingLamp)

			masterBedRoomBedLamp     = device(102, 'masterBedRoomBedLamp', 'lamp', 0, 0)
			self.deviceList.append(masterBedRoomBedLamp)

			masterBedRoomDoor        = device(103, 'masterBedRoomDoor', 'door', 0, 0)
			self.deviceList.append(masterBedRoomDoor)

			masterBedRoomWindow      = device(104, 'masterBedRoomWindow', 'window', 0, 0)
			self.deviceList.append(masterBedRoomWindow)

			masterBedRoomAirCondition= device(105, 'masterBedRoomAirCondition', 'airCondition', 0, 25)
			self.deviceList.append(masterBedRoomAirCondition)

			masterBedRoomComputer    = device(106, 'masterBedRoomComputer', 'computer', 0, 0)
			self.deviceList.append(masterBedRoomComputer)

			masterBedRoomCharger     = device(107, 'masterBedRoomCharger', 'charger', 0, 0)
			self.deviceList.append(masterBedRoomCharger)

		# Second Bedroom
		if (self.roomType == 'secondBedroom'):
			secondBedRoomTV          = device(200, 'secondBedRoomTV', 'TV', 0, 0)
			self.deviceList.append(secondBedRoomTV)

			secondBedRoomCeilingLamp = device(201, 'secondBedRoomCeilingLamp', 'lamp', 0, 0)
			self.deviceList.append(secondBedRoomCeilingLamp)

			secondBedRoomBedLamp     = device(202, 'secondBedRoomBedLamp', 'lamp', 0, 0)
			self.deviceList.append(secondBedRoomBedLamp)

			secondBedRoomDoor        = device(203, 'secondBedRoomDoor', 'door', 0, 0)
			self.deviceList.append(secondBedRoomDoor)

			secondBedRoomWindow      = device(204, 'secondBedRoomWindow', 'window', 0, 0)
			self.deviceList.append(secondBedRoomWindow)

			secondBedRoomAirCondition= device(205, 'secondBedRoomAirCondition', 'airCondition', 0, 25)
			self.deviceList.append(secondBedRoomAirCondition)

			secondBedRoomComputer    = device(206, 'secondBedRoomComputer', 'computer', 0, 0)
			self.deviceList.append(secondBedRoomComputer)

			secondBedRoomCharger     = device(207, 'secondBedRoomCharger', 'charger', 0, 0)
			self.deviceList.append(secondBedRoomCharger)

		# Third Bedroom
		if (self.roomType == 'thirdBedroom'):
			thirdBedRoomTV          = device(300, 'thirdBedRoomTV', 'TV', 0, 0)
			self.deviceList.append(thirdBedRoomTV)

			thirdBedRoomCeilingLamp = device(301, 'thirdBedRoomCeilingLamp', 'lamp', 0, 0)
			self.deviceList.append(thirdBedRoomCeilingLamp)

			thirdBedRoomBedLamp     = device(302, 'thirdBedRoomBedLamp', 'lamp', 0, 0)
			self.deviceList.append(thirdBedRoomBedLamp)

			thirdBedRoomDoor        = device(303, 'thirdBedRoomDoor', 'door', 0, 0)
			self.deviceList.append(thirdBedRoomDoor)

			thirdBedRoomWindow      = device(304, 'thirdBedRoomWindow', 'window', 0, 0)
			self.deviceList.append(thirdBedRoomWindow)

			thirdBedRoomAirCondition= device(305, 'thirdBedRoomAirCondition', 'airCondition', 0, 25)
			self.deviceList.append(thirdBedRoomAirCondition)

			thirdBedRoomComputer    = device(306, 'thirdBedRoomComputer', 'computer', 0, 0)
			self.deviceList.append(thirdBedRoomComputer)

			thirdBedRoomCharger     = device(307, 'thirdBedRoomCharger', 'charger', 0, 0)
			self.deviceList.append(thirdBedRoomCharger)

		# Bathroom
		if (self.roomType == 'bathroom'):
			bathroomLamp            = device(400, 'bathroomLamp', 'lamp', 0, 0)
			self.deviceList.append(bathroomLamp)

			bathroomWaterHeater     = device(401, 'bathroomWaterHeater', 'heater', 0, 0)
			self.deviceList.append(bathroomWaterHeater)

			bathroomDoor            = device(402, 'bathroomDoor', 'door', 0, 0)
			self.deviceList.append(bathroomDoor)

			bathroomWindow          = device(403, 'bathroomWindow', 'window', 0, 0)
			self.deviceList.append(bathroomWindow)

			bathroomCharger         = device(404, 'bathroomCharger', 'charger', 0, 0)
			self.deviceList.append(bathroomCharger)

			bathroomFan             = device(405, 'bathroomFan', 'other', 0, 0)
			self.deviceList.append(bathroomFan)

		# Kitchen	
		if (self.roomType == 'kitchen'):
			kitchenLamp             = device(500, 'kitchenLamp', 'lamp', 0, 0)
			self.deviceList.append(kitchenLamp)

			kitchenDoor             = device(501, 'kitchenDoor', 'door', 0, 0)
			self.deviceList.append(kitchenDoor)

			kitchenWindow           = device(502, 'kitchenWindow', 'window', 0, 0)
			self.deviceList.append(kitchenWindow)

			kitchenVentilator       = device(503, 'kitchenVentilator', 'other', 0, 0)
			self.deviceList.append(kitchenVentilator)

		# Dining Room	
		if (self.roomType == 'diningRoom'):
			diningRoomLamp          = device(600, 'diningRoomLamp', 'lamp', 0, 0)
			self.deviceList.append(diningRoomLamp)

			diningRoomDoor          = device(601, 'diningRoomDoor', 'door', 0, 0)
			self.deviceList.append(diningRoomDoor)

			diningRoomFan           = device(602, 'diningRoomFan', 'other', 0, 0)
			self.deviceList.append(diningRoomFan)

			diningRoomWindow        = device(603, 'diningRoomWindow', 'window', 0, 0)
			self.deviceList.append(diningRoomWindow)

			diningRoomAirCondition  = device(604, 'diningRoomAirCondition', 'airCondition', 0, 0)
			self.deviceList.append(diningRoomAirCondition)

		# Study Room
		if (self.roomType == 'studyRoom'):
			studyRoomCeilingLamp    = device(700, 'studyRoomCeilingLamp', 'lamp', 0, 0)
			self.deviceList.append(studyRoomCeilingLamp)

			studyRoomDeskLamp       = device(701, 'studyRoomDeskLamp', 'lamp', 0, 0)
			self.deviceList.append(studyRoomDeskLamp)

			studyRoomAirCondition   = device(702, 'studyRoomAirCondition', 'airCondition', 0, 0)
			self.deviceList.append(studyRoomAirCondition)

			studyRoomDoor           = device(703, 'studyRoomDoor', 'door', 0, 0)
			self.deviceList.append(studyRoomDoor)

			studyRoomWindow         = device(704, 'studyRoomWindow', 'window', 0, 0)
			self.deviceList.append(studyRoomWindow)

			studyRoomComputer       = device(705, 'studyRoomComputer', 'computer', 0, 0)
			self.deviceList.append(studyRoomComputer)

			studyRoomCharger        = device(706, 'studyRoomCharger', 'charger', 0, 0)
			self.deviceList.append(studyRoomCharger)

			studyRoomAudioSystem    = device(707, 'studyRoomAudioSystem', 'other', 0, 0)
			self.deviceList.append(studyRoomAudioSystem)

		self.setDevicesPosRandom()


	def setDevicesPosRandom(self):
		for tempDevice in self.deviceList:
			tempDevice.setRandomDevicePos(self.roomLeft, self.roomRight, self.roomTop, self.roomBottom)

	# def changeDeviceByType(self, deviceType, newStatu, newValue):
	# 	for tempDevice in self.deviceList:
	# 		if(tempDevice.getType() == deviceType):

	# 开启指定设备类型的设备，返回指定类型的设备列表
	def turnOnDeviceByType(self, deviceType):
		resDeviceList = []
		for tempDevice in self.deviceList:
			if ( tempDevice.getType() == deviceType ):
				tempDevice.turnOn()
				resDeviceList.append(tempDevice)
				if(tempDevice.getType() == 'lamp'):
					self.simL.setLightOn()
		return resDeviceList

	# 关闭指定设备类型的设备，返回指定类型的设备列表
	def turnOffDeviceByType(self, deviceType):
		resDeviceList = []
		for tempDevice in self.deviceList:
			if ( tempDevice.getType() == deviceType ):
				tempDevice.turnOff()
				resDeviceList.append(tempDevice)
				if(tempDevice.getType() == 'lamp'):
					self.simL.setLightOff()
		return resDeviceList

	# 开启制定设备名的设备，返回对应设备
	def turnOnDeviceByName(self, deviceName):
		for tempDevice in self.deviceList:
			if ( tempDevice.getName() == deviceName ):
				tempDevice.turnOn()
				if(tempDevice.getType() == 'lamp'):
					self.simL.setLightOn()
				return tempDevice
		return None

	# 关闭制定设备名的设备，返回对应设备
	def turnOffDeviceByName(self, deviceName):
		for tempDevice in self.deviceList:
			if( tempDevice.getName() == deviceName ):
				tempDevice.turnOff()
				if(tempDevice.getType() == 'lamp'):
					self.simL.setLightOff()
				return tempDevice
		return None

	# 设置制定设备类型的设备的值，返回指定类型的设备列表
	def setDeviceValueByType(self, deviceType, value):
		resDeviceList = []
		for tempDevice in self.deviceList:
			if ( tempDevice.getType() == deviceType ):
				tempDevice.setValue(value)
				resDeviceList.append(tempDevice)
		return resDeviceList

	# 获取房间当前亮度
	def getLight(self, currentTime):
		return self.simL.getCurrentLight(currentTime)

	# 房间是否黑暗
	def isDarkness(self, currentTime):
		return self.simL.isDarkness(currentTime)

	# 获取房间亮度百分比
	def getLightPercentage(self, currentTime):
		return self.simL.getPercentage(currentTime)

	# 存储房间信息到数据库
	def saveInfoToDB(self, houseID = None, sqlMana = None):
		if(houseID == None or sqlMana == None):
			return False
		else:
			# 存储数据
			flag = True
			sql = 'select * from room where ID = %d' %self.ID
			res = sqlMana.query(sql)
			if(len(res) > 0):
				sql = "update room set houseID= %d, roomType = '%s', roomLeft = %lf, roomRight = %lf, roomTop = %lf, roomBottom = %lf where ID = %d" %(houseID, self.roomType, self.roomRight, self.roomTop, self.roomBottom, self.ID)
				sqlMana.update(sql)
			else:
				sql = "insert into room (houseID, roomType, roomLeft, roomRight, roomTop, roomBottom) values (%d, '%s', %lf, %lf, %lf, %lf)" %(houseID, self.roomType, self.roomLeft, self.roomRight, self.roomTop, self.roomBottom) 
				# print("sdfsdfsdfsfdfssfsfd: ", sql)
				sqlMana.insert(sql)
				temp = sqlMana.query('select @@identity as newID')
				self.ID = temp[0].get('newID')
			for tempDevice in self.deviceList:
				flag = tempDevice.saveInfoToDB(self.ID, sqlMana) and flag
			return flag

	# 从数据库中读取房间信息（待验证）
	def readInfoFromDB(self, ID = None, sqlMana = None):
		if(ID == None or sqlMana == None):
			return False
		else:
			# 读数据（待验证）
			sql = 'select * from room where ID = %d' %ID
			res = sqlMana.query(sql)
			if(len(res) < 1):
				return False
			else:
				temp = res[0]
				self.ID         = int(temp.get("ID"))
				self.roomType   = str(temp.get("roomType"))
				self.roomLeft   = float(temp.get("roomLeft"))
				self.roomRight  = float(temp.get("roomRight"))
				self.roomTop    = float(temp.get("roomTop"))
				self.roomBottom = float(temp.get("roomBottom"))
				self.simL       = lightSimulator()
				self.deviceList = []
				self.initDeviceListFromDB(sqlMana)
				return True

	# 通过数据库初始化设备列表
	def initDeviceListFromDB(self, sqlMana = None):
		sql = 'select ID from device where roomID = %d' %self.ID
		res = sqlMana.query(sql)
		for temp in res:
			tempDevice = device()
			tempDevice.readInfoFromDB(temp.get('ID'), sqlMana)
			self.deviceList.append(tempDevice)

	# 获取房间全部信息，用于保存记录
	def getInfo(self, currentTime):
		tempCode = int(self.roomDict.get(self.roomType) / 100)
		tempStr = "light_%d" %tempCode
		tempLight = self.simL.getCurrentLight(currentTime)
		res = {
			tempStr : tempLight
		}
		for tempDevice in self.deviceList:
			res = dict( res.items() + tempDevice.getInfo().items() )
		return res




