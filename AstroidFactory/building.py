from AstroidFactory import items


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
    craftperiod = 0
    input = [[]]
    output = [[]]

#----------------------------------------------------------------
#builing

#1차 ddd


class Mine(ProductionBuilding):
    craftPeriod = 5
    price = 100
    width = 2
    height = 2

    def onwhich (ore):
        #이 건물의 xpos, ypos에 겹치는 광석 있는지 확인
        output = [[items.Solid, 1]]


class Pump(ProductionBuilding):
    craftPeriod = 5
    price = 100
    width = 2
    height = 2
    output = [[items.Water, 1]]

#2차


class Refinery(CraftingBuilding):
    craftPeriod = 10
    price = 1000
    width = 4
    height = 4

class Oilrefinery(CraftingBuilding):
    craftPeriod = 10
    price = 1000
    width = 4
    height = 4

class PlasticFactory(CraftingBuilding):
    craftPeriod = 15
    price = 10000
    width = 4
    height = 4

class CoolingWaterFactory(CraftingBuilding):
    craftPeriod = 10
    price = 10000
    width = 4
    height = 4