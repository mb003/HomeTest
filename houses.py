# -*- coding: utf-8 -*-
import time
import random
from rooms import room
from sqlManage import SQLManagement

class house:

	# roomDict    =   {
	# 	"livingRoom"           :           0,
	# 	"masterBedroom"        :           100,
	# 	"secondBedroom"        :           200,
	# 	"thirdBedroom"         :           300,
	# 	"bathroom"             :           400,
	# 	"kitchen"              :           500,
	# 	"diningRoom"           :           600,
	# 	"studyRoom"            :           700
	# }

	# 初始化函数
	def __init__(self, ID = -1, roomList = [], width = 20, height = 20):
		print 'in __init__ of house'
		self.ID       = ID
		self.width    = width
		self.height   = height
		self.roomList = []
		self.createHouseStructure(roomList)
		self.initRoomAndDevice()

	def getID(self):
		return self.ID

	def getWidth(self):
		return self.width

	def getHeight(self):
		return self.height

	def getRoomList(self):
		return self.roomList

	# 生成房间结构
	def createHouseStructure(self, roomList):
		print 'in createHouseStructure'
		self.roomList = []
		roomNum = len(roomList)
		for roomName in roomList:
			flag = True
			while(flag):
				flag = False
				tempPosX = random.randint(0, self.width  * 2/3 - 1)
				tempPosY = random.randint(0, self.height * 2/3 - 1)
				for tempRoom in self.roomList:
					if (tempPosX == tempRoom.getLeft() and tempPosY == tempRoom.getTop()):
						flag = True
						break;
			newRoom = room(-1, roomName, tempPosX, tempPosX, tempPosY, tempPosY)
			self.roomList.append(newRoom)

		# print 'end of seed create'

		endFlag = False
		while(not endFlag):
			endFlag = True
			for tempRoom in self.roomList:
				# right add
				flag       = True
				newRight   = tempRoom.getRight() + 1
				if(newRight >= self.width):
					flag = False
				for tempY in range(tempRoom.getTop(), tempRoom.getBottom() + 1):
					for existRoom in self.roomList:
						if(existRoom.isInRoom(newRight,tempY)):
							flag = False
							break;
						if(newRight-tempRoom.getLeft()>self.width/3):
							flag = False
							break;
					if(flag == False):
						break;
				if(flag):
					tempRoom.setRight(newRight)
					endFlag = False
				# bottom add
				flag      = True
				newBottom = tempRoom.getBottom() + 1 
				if(newBottom >= self.height):
					flag = False
				for tempX in range(tempRoom.getLeft(), tempRoom.getRight()+1):
					for existRoom in self.roomList:
						if(existRoom.isInRoom(tempX, newBottom)):
							flag = False
							break;
						if(newBottom - tempRoom.getTop() > self.height/3):
							flag = False
							break;
					if(flag == False):
						break;
				if(flag):
					tempRoom.setBottom(newBottom)
					endFlag = False
			# print 'loop'

		flag = True
		for tempRoom in self.roomList:
			if ( tempRoom.getSquare() <  (self.height * self.width)/roomNum/4):
				flag = False
		if (not flag):
			self.createHouseStructure(roomList)

	# 为各房间添加设备
	def initRoomAndDevice(self):
		for tempRoom in self.roomList:
			tempRoom.initDeviceList()

	# 判断是否存在某房间
	def roomExist(self, roomType):
		for tempRoom in self.roomList:
			if(tempRoom.getType() == roomType):
				return True
		return False

	# 在住房中添加房屋
	def appendRoom(self, ID, roomType, centerPosX, centerPosY, width, height):
		newRoom = room(-1, roomType, centerPosX, centerPosY, width, height)
		roomList.append(newRoom)
		return 

	# 打印房间信息及房间结构草图
	def printHouseInfo(self):
		for tempRoom in self.roomList:
			tempRoom.printInfo
		# print "House Map:"
		houseMap = [ [' ' for col in range(self.width)] for row in range(self.height)]
		for i in range(self.width):
			for j in range(self.height):
				count = 0
				for tempRoom in self.roomList:
					if ( tempRoom.isInRoom(i,j) and ( j == tempRoom.getTop() or j == tempRoom.getBottom() or i == tempRoom.getLeft() or i == tempRoom.getRight()) ):
						# houseMap[j][i] = count
						houseMap[j][i] = tempRoom.getType()[0]
					count = count + 1

		# print 'Len of roomList:	', len(self.roomList)
		for tempRoom in self.roomList:
			# print 'Room Type:	', tempRoom.getType(), len(tempRoom.deviceList)
			for tempDevice in tempRoom.deviceList:
				# print 'Device Type:	', tempDevice.getType()
				x = tempDevice.getPosX()
				y = tempDevice.getPosY()
				houseMap[y][x] = tempDevice.getTypeAbbr()

		# for i in range(self.height):
		# 	for j in range(self.width):
		# 			print houseMap[i][j],
		# 	print ''
		return houseMap

	# 开启指定房间内指定设备类型的设备，返回设备列表
	def turnOnDeviceByType(self, roomType, deviceType):
		for tempRoom in self.roomList:
			if ( tempRoom.getType() == roomType ):
				return tempRoom.turnOnDeviceByType(deviceType)
		return []

	# 关闭指定房间内指定设备类型的设备，返回设备列表
	def turnOffDeviceByType(self, roomType, deviceType):
		for tempRoom in self.roomList:
			if ( tempRoom.getType() == roomType ):
				return tempRoom.turnOffDeviceByType(deviceType)
		return []

	# 开启指定房间内指定设备名的设备，返回对应设备
	def turnOnDeviceByName(self, roomType, deviceName):
		for tempRoom in self.roomList:
			if ( tempRoom.getType() == roomType ):
				return tempRoom.turnOnDeviceByName(deviceName)
		return None

	# 关闭指定房间内指定设备名的设备，返回对应设备
	def turnOffDeviceByName(self, roomType, deviceName):
		for tempRoom in self.roomList:
			if ( tempRoom.getType() == roomType ):
				return tempRoom.turnOffDeviceByName(deviceName)
		return None


	# 设置指定房间内指定设备类型的设备的值，返回设备列表
	def setDeviceValueByType(self, roomType, deviceType, value):
		for tempRoom in self.roomList:
			if ( tempRoom.getType() == roomType ):
				return tempRoom.setDeviceValueByType(deviceType, value)
		return []


	# 获取指定坐标所处的房间
	def getRoomByPos(self, posX, posY):
		for tempRoom in self.roomList:
			if ( tempRoom.isInRoom(posX, posY) ):
				return tempRoom
		return None

	# 关闭指定类型的全部设备
	def turnOffAllByDeviceType(self, deviceType, exceptRoomTypeList = []):
		for tempRoom in self.roomList:
			flag = True
			for exceptRoomType in exceptRoomTypeList:
				if tempRoom.getType() == exceptRoomType:
					flag = False
			if (flag):
				tempRoom.turnOffDeviceByType(deviceType)

	# 获得距离最近的指定类型设备
	def getNearDevice(self, posX, posY, deviceType):
		import math
		desDevice = None
		mindis = float('inf')
		for tempRoom in self.roomList:
			for tempDevice in tempRoom.getDeviceList():
				if (tempDevice.getType == deviceType):
					dx = posX - tempDevice.getPosX()
					dy = posY - tempDevice.getPosY()
					dis = math.sqrt( dx*dx + dy*dy )
					if (mindis > dis):
						mindis = dis
						desDevice = tempDevice
		return desDevice

	# 打开距离最近的指定类型设备，返回对应设备
	def turnOnNearDevice(self, posX, posY, deviceType):
		tempDevice = self.getNearDevice(posX, posY, deviceType)
		if ( tempDevice == None ):
			return None
		else:
			tempDevice.turnOn()
			return tempDevice

	# 关闭距离最近的指定类型设备，返回对应设备
	def turnOffNearDevice(self, posX, posY, deviceType):
		tempDevice = self.getNearDevice(posX, posY, deviceType)
		if ( tempDevice == None ):
			return None
		else:
			tempDevice.turnOff()
			return tempDevice

	# 设定距离最近的指定设备的值，返回对应设备
	def setNearDeviceValue(self, posX, posY, deviceType, value):
		tempDevice = self.getNearDevice(posX, posY, deviceType)
		if ( tempDevice == None ):
			return None
		else:
			tempDevice.setValue(value)
			return tempDevice

	# 向数据库中存储住房信息
	def saveInfoToDB(self, humanID = None, sqlMana = None):
		if(humanID == None or sqlMana == None):
			return False
		else:
			flag = True
			sql = 'select * from house where ID = %d' %self.ID
			res = sqlMana.query(sql)
			if(len(res) > 0):
				sql = "update house set humanID= %d, width = %lf, height = %lf where ID = %d" %(humanID, self.width, self.height, self.ID)
				sqlMana.update(sql)
			else:
				sql = "insert into house (humanID, width, height) values (%d, %lf, %lf)" %(humanID, self.width, self.height)
				sqlMana.insert(sql)
				temp = sqlMana.query('select @@identity as newID')
				self.ID = temp[0].get('newID')
			for tempRoom in self.roomList:
				flag = tempRoom.saveInfoToDB(self.ID, sqlMana) and flag
			return flag


	# 从数据库中读取住房信息（待验证）
	def readInfoFromDB(self, ID = None, sqlMana = None):
		if( ID == None or sqlMana == None):
			return False
		else:
			# 读数据（待验证）
			sql = 'select * from house where ID = %d' %ID
			res = sqlMana.query(sql)
			if(len(res) < 1):
				return False
			else:
				temp = res[0]
				self.ID       = int(temp.get("ID"))
				self.width    = float(temp.get("width"))
				self.height   = float(temp.get("height"))
				self.roomList = []
				self.initRoomListFromDB(sqlMana)
				return True
		
	# 通过数据库初始化房间列表（待验证）
	def initRoomListFromDB(self, sqlMana = None):
		sql = 'select ID from room where houseID = %d' %self.ID
		res = sqlMana.query(sql)
		for temp in res:
			tempRoom = room()
			tempRoom.readInfoFromDB(temp.get('ID'), sqlMana)
			self.roomList.append(tempRoom)

	# 获得住房全部信息，用于保存记录
	def getInfo(self, currentTime):
		res = dict()
		for tempRoom in self.roomList:
			res = dict(res.items() + tempRoom.getInfo(currentTime).items())
		return res
