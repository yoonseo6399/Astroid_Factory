#----------------------------------------------------------------
#Frame

class building: #건물
    price = 0
    Xpos = 0
    Ypos = 0
    width = 0
    length = 0


class productionBuilding(building): #기본 생산 건물
    craftPeriod = 0 #제작 주기
    output = [[]]

class craftingBuilding(building):   #2차 생산 건물
    craftPeriod = 0
    input = [[]]
    output = [[]]

#----------------------------------------------------------------
#builing

#1차

class mine(productionBuilding):
    craftPeriod = 5
    price = 100
    width = 2
    height = 2

    def onwhich (ore):
        #이 건물의 xpos, ypos에 겹치는 광석 있는지 확인
        output = ["ore"[1]]

class pump(productionBuilding):
    craftperiod = 5
    price = 100
    width = 2
    height = 2
    output = ["water"[1]]

#2차

class refinery(craftingBuilding):
    craftperiod = 10
    price = 1000
    width = 4
    height = 4
    input = ["water"[1], "ore"[2], "energy"[1]]