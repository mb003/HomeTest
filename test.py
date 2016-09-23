# -*- coding: utf-8 -*-

roomList = {
	"livingRoom",
	"masterBedroom",
	# "secondBedroom",
	# "thirdBedroom",
	"bathroom",
	"kitchen",
	"diningRoom",
	"studyRoom"
}

width  = 30
height = 30

from houses import house

# myHouse = house(roomList, width, height)
# myHouse.printHouseInfo()

from human import human


# class T:
# 	# value  =  0
# 	# _vlist  =  []
# 	def __init__(self, value):
# 		self.setValue(value)
# 	def setValue(self, value):
# 		self._vlist = []
# 		self.value = value
# 	def getValue(self):
# 		return self.value
# 	def appendValueList(self, value):
# 		self._vlist.append(value)
# 	def printValueList(self):
# 		for v in self._vlist:
# 			print " ", v,
# 		print ''

# tt = T(1234)
# tt.appendValueList(666)


# myList = []

# for i in range(5):
# 	tempT = T(i)
# 	tempT.setValue(i + 5)
# 	myList.append(tempT)

# T.value = 100

# count = 0
# for tT in myList:
# 	for i in range(5):
# 		tT.appendValueList(i + count * 5)
# 	count = count + 1
# 	# print tempT.getValue()
# # myList[0].vlist[3] = 44

# for ttT in myList:
# 	ttT.printValueList()
# 	print ttT.getValue(), T.value

# print 't:	', tt.printValueList()



# roomDict    =   {
# 		"livingRoom"           :           0,
# 		"masterBedroom"        :           100,
# 		"secondBedroom"        :           200,
# 		"thirdBedroom"         :           300,
# 		"bathroom"             :           400,
# 		"kitchen"              :           500,
# 		"diningRoom"           :           600,
# 		"studyRoom"            :           700
# 	}


# print roomDict.get('asdasdad') == None

# import matplotlib.pyplot as plt
# import turtle
# import time
# from graphics import *

# graphics.test()
# win = GraphWin()
# pt = Point(100, 50)
# win.getMouse()
# pt.draw(win)
# win.getMouse()
# cir = Circle(pt, 25)
# win.getMouse()
# cir.draw(win)
# win.getMouse()
# cir.setOutline('red')
# win.getMouse()
# cir.setFill('blue')
# win.getMouse()
# line = Line(pt, Point(150, 100))
# win.getMouse()
# line.draw(win)
# win.getMouse()
# win.close()

# # plt.
# # plt.show()
# turtle.color("purple")
# # turtle.size(5)
# turtle.goto(10,10)
# turtle.forward(100)
# time.sleep(100)

# win = GraphWin()
# pt1 = Point(10,10)
# pt2 = Point(10,100)
# line = Line(pt1, pt2)
# pt1.draw(win)
# pt2.draw(win)
# line.draw(win)
# # line.draw(win)
# for i in range(10,300):
# 	for j in range(10,300):
# 		pt2._move(i,j)
# 		# line.draw(win)
# 		win.getMouse()

import time
currentTimeStr = "2016 6 18 00:00:00"
currentTime = time.mktime(time.strptime(currentTimeStr, "%Y %m %d %H:%M:%S"))

endTimeStr = "2016 6 19 00:00:00"
endTime = time.mktime(time.strptime(endTimeStr, "%Y %m %d %H:%M:%S"))

# startTimeStr = time.strftime("%Y %m %d", time.localtime(currentTime))
# print startTimeStr

# startTime = time.mktime(time.strptime( startTimeStr + " 16:49:19", "%Y %m %d %H:%M:%S"))
# print time.strftime("%H:%M:%S", time.localtime(startTime))

fp = open('light.txt', 'w')

from light import lightSimulator
simL = lightSimulator(currentTime)

while (currentTime < endTime):
    fp.write(time.strftime("%H:%M:%S", time.localtime(currentTime)))
    fp.write("\t")
    fp.write(str(simL.getCurrentLight(currentTime)))
    fp.write("\n")
    currentTime += 30
    if(simL.getCurrentLight(currentTime) > 10):
        simL.setLightOff(currentTime)
    if(simL.isDarkness(currentTime)):
        simL.setLightOn(currentTime)



