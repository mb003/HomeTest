import math
import time

class temperatureSimulator:

	def __init__(self, currentTime):
		self.currentTemperature = self.getInDoorTemperature(currentTime)
		self.destinationTemperature = self.getInDoorTemperature(currentTime)
		self.isSetTemperature = 0
		self.timeSetTemperature = currentTime

	def getOutDoorTemperatureUp(self, currentTime):
		day = time.strftime("%j", time.localtime(currentTime))
		day = int(day)
		theta = math.pi * (day - 105) / 180
		T = math.sin(theta) * 14.5 + 16.5
		return T

	def getOutDoorTemperatureDown(self, currentTime):
		day = time.strftime("%j", time.localtime(currentTime))
		day = int(day)
		theta = math.pi * (day - 105) / 180
		T = math.sin(theta) * 15.5 + 6.5
		return T

	def getOutDoorTemperature(self, currentTime):
		hour = int(time.strftime("%H", time.localtime(currentTime)))
		minute = int(time.strftime("%M", time.localtime(currentTime)))
		totalMinute = 60 * hour + minute
		theta = math.pi * (totalMinute - 540) / 720
		up = self.getOutDoorTemperatureUp(currentTime)
		down = self.getOutDoorTemperatureDown(currentTime)
		T = math.sin(theta) * (up - down) / 2 + (up + down) / 2
		return T

	def getInDoorTemperature(self, currentTime):
		outDoorT = self.getOutDoorTemperature(currentTime)
		# print(outDoorT)
		T = 0.6 * 25 + 0.4 * outDoorT
		return T

	def getCurrentTemperature(self):
		return self.currentTemperature

	def iterate(self, currentTime, timeSlot):
		if(self.isSetTemperature == 0):
			deltaT = (self.getInDoorTemperature(currentTime) - self.getCurrentTemperature()) / (1000.0 / timeSlot)
			self.currentTemperature = self.currentTemperature + deltaT
		else:
			deltaT = (self.destinationTemperature - self.currentTemperature) / (1000.0 / timeSlot)
			self.currentTemperature = self.currentTemperature + deltaT			
		return self.currentTemperature

	def setTemperatureOn(self, destinationTemperature):
		self.isSetTemperature = 1
		self.destinationTemperature = destinationTemperature

	def setTemperatureOff(self):
		self.isSetTemperature = 0

	def getTimeSetTemperature(self):
		return self.timeSetTemperature

	def isTemperatureBeenSet(self):
		if(self.isSetTemperature == 0):
			return False
		else:
			return True

