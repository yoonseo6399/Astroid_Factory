#----------------------------------------------------------------
#Frame

class Building: #건물
    price = 0
    Xpos = 0
    Ypos = 0
    width = 0
    length = 0


class ProductionBuilding(Building): #기본 생산 건물
    craftPeriod = 0 #제작 주기
    output = [[]]

class CraftingBuilding(Building):   #2차 생산 건물
    craftPeriod = 0
    input = [[]]
    output = [[]]

#----------------------------------------------------------------
#builing

#1차

class Mine(ProductionBuilding):
    craftPeriod = 5
    price = 100
    width = 2
    height = 2

    def onwhich (ore):
        #이 건물의 xpos, ypos에 겹치는 광석 있는지 확인
        output = ["ore"[1]]

class Pump(ProductionBuilding):
    craftperiod = 5
    price = 100
    width = 2
    height = 2
    output = ["water"[1]]

#2차

class Refinery(CraftingBuilding):
    craftperiod = 10
    price = 1000
    width = 4
    height = 4
