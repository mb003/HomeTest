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
		"studyRoom"            :           700,
        "dormitory"            :           1000
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
        #dormitory
		if (self.roomType == 'dormitory'):
            #小爱音箱*5
			dormitoryXiaoaiAudio1 = device(1001, 'dormitoryXiaoaiAudio1', 'audio', 0, 0)
			self.deviceList.append(dormitoryXiaoaiAudio1)
			dormitoryXiaoaiAudio2 = device(1002, 'dormitoryXiaoaiAudio2', 'audio', 0, 0)
			self.deviceList.append(dormitoryXiaoaiAudio2)
			dormitoryXiaoaiAudio3 = device(1003, 'dormitoryXiaoaiAudio3', 'audio', 0, 0)
			self.deviceList.append(dormitoryXiaoaiAudio3)
			dormitoryXiaoaiAudio4 = device(1004, 'dormitoryXiaoaiAudio4', 'audio', 0, 0)
			self.deviceList.append(dormitoryXiaoaiAudio4)
			dormitoryXiaoaiAudio5 = device(1005, 'dormitoryXiaoaiAudio5', 'audio', 0, 0)
			self.deviceList.append(dormitoryXiaoaiAudio5)
            #蓝牙温湿度计
			dormitoryThermometer = device(1006, 'dormitoryThermometer', 'thermometer', 0, 0)
			self.deviceList.append(dormitoryThermometer)
            #摄像机
			dormitoryCamere1 = device(1007, 'dormitoryCamere1', 'camere', 0, 0)
			self.deviceList.append(dormitoryCamere1)
            #门窗传感器*3
			dormitoryDoorWindowSensor1 = device(1008, 'dormitoryDoorWindowSensor1', 'sensor', 0, 0)
			self.deviceList.append(dormitoryDoorWindowSensor1)
			dormitoryDoorWindowSensor2 = device(1009, 'dormitoryDoorWindowSensor2', 'sensor', 0, 0)
			self.deviceList.append(dormitoryDoorWindowSensor2)
			dormitoryDoorWindowSensor3 = device(1010, 'dormitoryDoorWindowSensor3', 'sensor', 0, 0)
			self.deviceList.append(dormitoryDoorWindowSensor3)
            #人体移动传感器*2
			dormitoryHumanSensor1 = device(1011, 'dormitoryHumanSensor1', 'sensor', 0, 0)
			self.deviceList.append(dormitoryHumanSensor1)   
			dormitoryHumanSensor2 = device(1012, 'dormitoryHumanSensor2', 'sensor', 0, 0)
			self.deviceList.append(dormitoryHumanSensor2)
            #三开关单控开关
			dormitoryThreeSwitch = device(1013, 'dormitoryThreeSwitch', 'switch', 0, 0)
			self.deviceList.append(dormitoryThreeSwitch)  
            #窗帘伴侣
			dormitoryCurtainCompanion = device(1014, 'dormitoryCurtainCompanion', 'switch', 0, 0)
			self.deviceList.append(dormitoryCurtainCompanion) 
            #智能插座
			dormitorySmartSocket = device(1015, 'dormitorySmartSocket', 'socket', 0, 0)
			self.deviceList.append(dormitorySmartSocket) 

            
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

	# 开启某人指定设备类型的设备，返回指定类型的设备列表
	def turnOnDeviceByType(self, deviceType, ID):
		resDeviceList = []
		for tempDevice in self.deviceList:
			for ownerID in tempDevice.getOwnerID():
				if ( tempDevice.getType() == deviceType and ownerID == ID):
					tempDevice.turnOn()
					resDeviceList.append(tempDevice)
					if(tempDevice.getType() == 'lamp'):
						self.simL.setLightOn()
		return resDeviceList

	# 关闭某人指定设备类型的设备，返回指定类型的设备列表
	def turnOffDeviceByTypeOfMan(self, deviceType, ID):
		resDeviceList = []
		for tempDevice in self.deviceList:
			for ownerID in tempDevice.getOwnerID():
				if ( tempDevice.getType() == deviceType and ownerID == ID):
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
    
	#根据类型和拥有者来打开设备，返回设备
	def turnOnDeviceByTypeAndOwner(self,  deviceType, OwnerID):
		for tempDevice in self.deviceList:
			if( tempDevice.getType() == deviceType and tempDevice.getOwner() == OwnerID):
				tempDevice.turnOn()
				if(tempDevice.getType() == 'lamp'):
					self.simL.setLightOn()
				return tempDevice
		return None
	
	#根据类型和拥有者来关闭设备，返回设备
	def turnOffDeviceByTypeAndOwner(self, deviceType, OwnerID):
		for tempDevice in self.deviceList:
			if( tempDevice.getType() == deviceType and tempDevice.getOwner() == OwnerID):
				tempDevice.turnOff()
				if(tempDevice.getType() == 'lamp'):
					self.simL.setLightOff()
				return tempDevice
		return None
        
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


    

