# -*- coding: utf-8 -*-

import math
import time

class lightSimulator:

	def __init__(self):
		self.addLight = 0
		self.DARKNESS_LIMIT = 3
		# self.BRIGHT_LIMIT = 6
		self.MAX_SUNLIGHT = 15
		self.LAMP_LIGHT = 11

	# 获取当日日出时间
	def getSunRiseTime(self, currentTime):
		day = time.strftime("%j", time.localtime(currentTime))
		day = int(day)
		theta = 2 * math.pi * (day - 74) / 365
		baseTimeStr = time.strftime("%Y %m %d", time.localtime(currentTime))
		utrStr = baseTimeStr + " 07:36:03"  # 北京市最晚日出时间
		dtrStr = baseTimeStr + " 04:45:09"  # 北京市最早日出时间
		utr = time.mktime(time.strptime(utrStr, "%Y %m %d %H:%M:%S"))
		dtr = time.mktime(time.strptime(dtrStr, "%Y %m %d %H:%M:%S"))
		sunriseTime = ( -math.sin(theta) * (utr-dtr)/2) + (utr+dtr)/2
		return sunriseTime

	# 获取当日日落时间
	def getSunSetTime(self, currentTime):
		day = time.strftime("%j", time.localtime(currentTime))
		day = int(day)
		theta = 2 * math.pi * (day - 86) / 365
		baseTimeStr = time.strftime("%Y %m %d", time.localtime(currentTime))
		utsStr = baseTimeStr + " 19:47:05"  # 北京市最晚日落时间
		dtsStr = baseTimeStr + " 16:49:19"  # 北京市最早日落时间
		uts = time.mktime(time.strptime(utsStr, "%Y %m %d %H:%M:%S"))
		dts = time.mktime(time.strptime(dtsStr, "%Y %m %d %H:%M:%S"))
		sunsetTime = math.sin(theta) * (uts-dts)/2 + (uts+dts)/2
		return sunsetTime

	# 获取阳光亮度
	def getSunLight(self, currentTime):
		sunriseTime = self.getSunRiseTime(currentTime)
		sunsetTime = self.getSunSetTime(currentTime)
		if(currentTime < sunriseTime or currentTime > sunsetTime):
			return 0
		else:
			sunTime = sunsetTime - sunriseTime
			deltaTime = currentTime - sunriseTime
			theta = deltaTime * 1.0 / sunTime * math.pi
			sunLight = math.sin(theta) * self.MAX_SUNLIGHT
			return sunLight

	# 获取房间内当前亮度
	def getCurrentLight(self, currentTime):
		return self.addLight + self.getSunLight(currentTime)

	# 判断是否需要开灯
	def isDarkness(self, currentTime):
		return self.getCurrentLight(currentTime) < self.DARKNESS_LIMIT

	# 打开一盏灯时的光线变化
	def setLightOn(self):
		self.addLight += self.LAMP_LIGHT
		# return self.getCurrentLight(currentTime)

	# 关闭一盏灯时的光线变化
	def setLightOff(self):
		self.addLight -= self.LAMP_LIGHT
		if (self.addLight < 0):
			self.addLight = 0
		# return self.getCurrentLight(currentTime)

	# 返回光照百分比
	def getPercentage(self, currentTime):
		tempLight = self.getCurrentLight(currentTime)
		if (tempLight > self.DARKNESS_LIMIT):
			return 1.0
		else:
			return 1.0 * tempLight / self.DARKNESS_LIMIT


