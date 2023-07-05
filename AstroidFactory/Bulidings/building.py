class Building:
    size = 0
    price = 0
    
    positionX = 0
    positionY = 0
    width = 0
    length = 0


class ProductionBuilding(building):
    craftPeriod = 0
    output = 0


class CraftingBuilding(building):
    craftPeriod = 0
    input = 0
    output = 0