# -*- coding: utf-8 -*-

import math
import pygame
from sqlManage import SQLManagement

class device:

	typeStrToNum =        {
		"lamp"           :        0,
		"airCondition"   :        1,
		#"TV"             :        2,
		"computer"       :        3,
		"charger"        :        4,
		#"heater"         :        5,
		"door"           :        6,
		"window"         :        7,
		"other"          :        8,
        
        #new
        "audio"          :        9,
        "switch"         :        10,
        "camere"         :        11,
        "thermometer"    :        12,
        "sensor"         :        13,
        "socket"         :        14
	}

	# typeNumToStr =        {
	# 	0                :        "lamp",
	# 	1                :        "airCondition",
	# 	2                :        "TV",
	# 	3                :        "computer",
	# 	4                :        "charger",
	# 	5                :        "heater",
	# 	6                :        "door",
	# 	7                :        "window",
	# 	8                :        "other"
	# }       

	def __init__(self, code = 0, deviceName = 'None', deviceType = 'other', statu = 0, value = -1, posX = 0, posY = 0, ID = -1, ownerID = -1):
		self.code        =  code
		self.name        =  deviceName
		self.deviceType  =  deviceType
		self.statu       =  statu
		self.value       =  value
		self.posX        =  posX
		self.posY        =  posY
		self.ID          =  -1
		self.imageOn     =  pygame.image.load('./pic/' + self.getType() + '_on.png')
		self.imageOff    =  pygame.image.load('./pic/' + self.getType() + '_off.png')
		self.ownerList	 = ownerID


	def getCode(self):
		return self.code

	def setCode(self, code):
		self.code = code

	def setID(self, ID):
		self.ID = ID

	def getID(self):
		return self.ID

	def getName(self):
		return self.name

	def setName(self, deviceName):
		self.name = deviceName

	def getStatu(self):
		if(self.statu == 0):
			return False
		else:
			return True

	def turnOn(self):
		self.statu        =  1
		# print(self.name + ' has been turn on')

	def turnOff(self):
		self.statu        =  0
		# print(self.name + ' has been turn off')

	def getValue(self):
		return self.value

	def setValue(self, value):
		self.value        =  value

	def getType(self):
		return self.deviceType

	def setType(self, Type):
		if(self.typeStrToNum.get(Type) == 'None'):
			self.deviceType    =  'other'
		else:
			self.deviceType    =  Type

	def setPos(self, posX, posY):
		self.posX         =  posX
		self.posY         =  posY

	def getPosX(self):
		return self.posX

	def getPosY(self):
		return self.posY

	def getImage(self):
		if(self.getStatu()):
			return self.imageOn
		else:
			return self.imageOff

	def calDistance(self, posX, posY):
		dx = self.posX - posX
		dy = self.posY - posY
		dis = math.sqrt(dx*dx + dy*dy)
		return dis

	def setRandomDevicePos(self, roomLeft, roomRight, roomTop, roomBottom):
		import random
		if(self.deviceType == 'lamp'):
			tempPosX = int((roomLeft+roomRight)/2)
			tempPosY = int((roomTop+roomBottom)/2)
			self.setPos(tempPosX, tempPosY)
			# print('lamp', self.getPosX(), self.getPosY())
		if(self.deviceType == 'airCondition'):
			direction = random.randint(1, 4)
			if(direction == 1):
				tempPosX = roomLeft
				tempPosY = random.randint(roomTop, roomBottom)
			if(direction == 2):
				tempPosX = roomRight
				tempPosY = random.randint(roomTop, roomBottom)
			if(direction == 3):
				tempPosY = roomTop
				tempPosX = random.randint(roomLeft, roomRight)
			if(direction == 4):
				tempPosY = roomBottom
				tempPosX = random.randint(roomLeft, roomRight)
			self.setPos(tempPosX, tempPosY)
			# print('airCondition', self.getPosX(), self.getPosY())
		if(self.deviceType == 'TV'):
			direction = random.randint(1, 4)
			if(direction == 1):
				tempPosX = roomLeft
				tempPosY = random.randint(roomTop, roomBottom)
			if(direction == 2):
				tempPosX = roomRight
				tempPosY = random.randint(roomTop, roomBottom)
			if(direction == 3):
				tempPosY = roomTop
				tempPosX = random.randint(roomLeft, roomRight)
			if(direction == 4):
				tempPosY = roomBottom
				tempPosX = random.randint(roomLeft, roomRight)
			self.setPos(tempPosX, tempPosY)
			# print('TV', self.getPosX(), self.getPosY())
		if(self.deviceType == 'computer'):
			tempPosX = random.randint(roomLeft, roomRight)
			tempPosY = random.randint(roomTop, roomBottom)
			self.setPos(tempPosX, tempPosY)
			# print('computer', self.getPosX(), self.getPosY())
		if(self.deviceType == 'charger'):
			tempPosX = random.randint(roomLeft, roomRight)
			tempPosY = random.randint(roomTop, roomBottom)
			self.setPos(tempPosX, tempPosY)
			# print('charger', self.getPosX(), self.getPosY())
		if(self.deviceType == 'heater'):
			tempPosX = random.randint(roomLeft, roomRight)
			tempPosY = random.randint(roomTop, roomBottom)
			self.setPos(tempPosX, tempPosY)
			# print('heater', self.getPosX(), self.getPosY())
		# 随机定义位置
		if(self.deviceType == 'sensor'):
			tempPosX = random.randint(roomLeft, roomRight)
			tempPosY = random.randint(roomTop, roomBottom)
			self.setPos(tempPosX, tempPosY)

		if(self.deviceType == 'thermometer'):
			tempPosX = random.randint(roomLeft, roomRight)
			tempPosY = random.randint(roomTop, roomBottom)
			self.setPos(tempPosX, tempPosY)

		if(self.deviceType == 'voice_assistant'):
			tempPosX = random.randint(roomLeft, roomRight)
			tempPosY = random.randint(roomTop, roomBottom)
			self.setPos(tempPosX, tempPosY)

		if(self.deviceType == 'camere'):
			direction = random.randint(1, 4)
			if(direction == 1):
				tempPosX = roomLeft
				tempPosY = random.randint(roomTop, roomBottom)
			if(direction == 2):
				tempPosX = roomRight
				tempPosY = random.randint(roomTop, roomBottom)
			if(direction == 3):
				tempPosY = roomTop
				tempPosX = random.randint(roomLeft, roomRight)
			if(direction == 4):
				tempPosY = roomBottom
				tempPosX = random.randint(roomLeft, roomRight)
			self.setPos(tempPosX, tempPosY)

		if(self.deviceType == 'switch'):
			direction = random.randint(1, 4)
			if(direction == 1):
				tempPosX = roomLeft
				tempPosY = random.randint(roomTop, roomBottom)
			if(direction == 2):
				tempPosX = roomRight
				tempPosY = random.randint(roomTop, roomBottom)
			if(direction == 3):
				tempPosY = roomTop
				tempPosX = random.randint(roomLeft, roomRight)
			if(direction == 4):
				tempPosY = roomBottom
				tempPosX = random.randint(roomLeft, roomRight)
			self.setPos(tempPosX, tempPosY)

		if(self.deviceType == 'socket'):
			direction = random.randint(1, 4)
			if(direction == 1):
				tempPosX = roomLeft
				tempPosY = random.randint(roomTop, roomBottom)
			if(direction == 2):
				tempPosX = roomRight
				tempPosY = random.randint(roomTop, roomBottom)
			if(direction == 3):
				tempPosY = roomTop
				tempPosX = random.randint(roomLeft, roomRight)
			if(direction == 4):
				tempPosY = roomBottom
				tempPosX = random.randint(roomLeft, roomRight)
			self.setPos(tempPosX, tempPosY)

		if(self.deviceType == 'door'):
			direction = random.randint(1, 4)
			if(direction == 1):
				tempPosX = roomLeft
				tempPosY = random.randint(roomTop, roomBottom)
			if(direction == 2):
				tempPosX = roomRight
				tempPosY = random.randint(roomTop, roomBottom)
			if(direction == 3):
				tempPosY = roomTop
				tempPosX = random.randint(roomLeft, roomRight)
			if(direction == 4):
				tempPosY = roomBottom
				tempPosX = random.randint(roomLeft, roomRight)
			self.setPos(tempPosX, tempPosY)
			# print('door', self.getPosX(), self.getPosY())
		if(self.deviceType == 'window'):
			direction = random.randint(1, 4)
			tempPosX = int( (roomLeft+roomRight)/2 )
			tempPosY = int( (roomTop+roomBottom)/2 )
			if(direction == 1):
				tempPosX = roomLeft
				tempPosY = random.randint(roomTop, roomBottom)
			if(direction == 2):
				tempPosX = roomRight
				tempPosY = random.randint(roomTop, roomBottom)
			if(direction == 3):
				tempPosY = roomTop
				tempPosX = random.randint(roomLeft, roomRight)
			if(direction == 4):
				tempPosY = roomBottom
				tempPosX = random.randint(roomLeft, roomRight)
			self.setPos(tempPosX, tempPosY)
			# print('window',  self.getPosX(), self.getPosY())

		if(self.deviceType == 'other'):
			tempPosX = random.randint(roomLeft, roomRight)
			tempPosY = random.randint(roomTop, roomBottom)
			self.setPos(tempPosX, tempPosY)
			# print('other:	', self.getPosX(), self.getPosY())

	def getTypeAbbr(self):
		if(self.deviceType == 'computer'):
			return 'P'
		return self.deviceType[0]

	# 从数据库中读取数据（待验证）
	def readInfoFromDB(self, ID = None, sqlMana = None):
		if(ID == None or sqlMana == None):
			return False
		else:
			# 读数据（待验证）
			sql = 'select * from device where ID = %d' %ID
			res = sqlMana.query(sql)
			if(len(res) < 1):
				return False
			else:
				temp = res[0]
				self.ID         = temp.get("ID")
				self.deviceType = temp.get("deviceType")
				self.name       = str(temp.get("name"))
				self.statu      = temp.get("statu")
				self.value      = temp.get("value")
				self.posX       = temp.get("posX")				
				self.posY       = temp.get("posY")
				self.code       = temp.get("code")
				self.imageOn    = pygame.image.load('./pic/' + self.getType() + '_on.png')
				self.imageOff   = pygame.image.load('./pic/' + self.getType() + '_off.png')
				return True


	# 向数据库中存储该设备信息
	def saveInfoToDB(self, roomID = None, sqlMana = None):
		if(roomID == None or sqlMana == None):
			return False
		else:
			# 存数据
			sql = 'select * from device where ID = %d' %self.ID
			res = sqlMana.query(sql)
			if(len(res) > 0):
				sql = "update device set roomID= %d, deviceType = '%s', name = '%s', statu = %d, value = %lf, posX = %lf, posY = %lf, code = %d where ID = %d" %(roomID, self.deviceType, self.name, self.statu, self.value, self.posX, self.posY, self.code, self.ID)
				sqlMana.update(sql)
			else:
				sql = "insert into device (roomID, deviceType, name, statu, value, posX, posY, code) values (%d, '%s', '%s', %d, %lf, %lf, %lf, %d)" %(roomID, self.deviceType, self.name, self.statu, self.value, self.posX, self.posY, self.code) 
				sqlMana.insert(sql)
				temp = sqlMana.query('select @@identity as newID')
				self.ID = temp[0].get('newID')
			return True

	# 获取设备信息，用于保存记录
	def getInfo(self):
		tempStr = 'device_%03d_' %self.code
		res = {
			tempStr + 'ID'    : int(self.ID),
			tempStr + 'statu' : int(self.statu),
			tempStr + 'value' : float(self.value)
		}
		return res

	# 获取设备的所有者
	def getOwner(self):
		return 