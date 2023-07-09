# ----------------------------------------------------------------
# frame

class Item:  # frame
    state = ""
    recipe = [[]]
    name = "item"
    description = "ester egg"
    price = "non-tradable"
    rarity = 10


class Solid(Item):
    state = "solid"


class Liquid(Item):
    state = "liquid"


class Gas(Item):
    state = "gas"


class Special(Item):
    state = "special"


# ----------------------------------------------------------------
# items

# special-----
class Energy(Special):
    name = "생각중"
    description = "거의 모든 기계들이 동작하게 하는 에너지다."


class Blank(Special):
    name = "공백"
    description = "아무것도 없는 땅이다."


# solid-----
class Coal(Solid):
    name = "석탄"
    description = "석탄이다."


class Iron(Solid):
    name = "철"
    description = "철이다."


class Aluminium(Solid):
    name = "알루미늄"
    description = "알루미늄이다."


class Titanium(Solid):
    name = "티타늄"


class Tungsten(Solid):
    name = "텅스텐"


class Manganese(Solid):
    name = "망가니즈"


class Uranium(Solid):
    name = "우라늄"


class Copper(Solid):
    name = "구리"


class Osmium(Solid):
    name = "오스뮴"


# liquid-----
class Water(Liquid):
    name = "물"


class CrudeOil(Liquid):
    name = "원유"


class Slag(Liquid):
    name = "광재"


# gas-----
class Hydrogen(Gas):
    name = "수소"


class Oxygen(Gas):
    name = "산소"


class Argon(Gas):
    name = "아르곤"


# 제작품----------------

# solid-----

class Steel(Solid):
    name = "강철"
    recipe = [[Iron, 1], [Manganese, 1], [Energy, 1]]


# liquid-----

class CollingWater(Liquid):
    name = "냉각수"
    recipe = [[Water, 1], [Energy, 1]]


class Liquidhydrogen(Liquid):
    name = "액화 수소"
    recipe = [[Hydrogen, 1], [CollingWater, 1], [Energy, 1]]


class LiquidOxygen(Liquid):
    name = "액화 산소"
    recipe = [[Oxygen, 1], [CollingWater, 1], [Energy, 1]]


class Oil(Liquid):
    name = "석유"
    recipe = [[Water, 1], [CrudeOil, 2], [Energy, 1]]


# gas-----


# 분류
class Items:
    items = [Energy(), Blank(), Coal(), Iron(), Aluminium(), Titanium(), Tungsten(), Manganese(), Uranium(), Copper(), Osmium(), Water(), CrudeOil(), Slag(), Oxygen(), Argon(), Steel(), CollingWater(), Liquidhydrogen(), LiquidOxygen(), Oil()]
    ores = [Iron(), Aluminium(), Titanium(), Tungsten(), Manganese(), Uranium(), Copper(), Osmium()]
    liqiud = [Water(), CrudeOil(), Slag()]
    naturalResources = [Blank(), Coal(), Iron(), Aluminium(), Titanium(), Tungsten(), Manganese(), Uranium(), Copper(), Osmium()]  # 맵 생성시 필요
    createResource = []
    for list in naturalResources:
        for x in range(1, list.rarity):
            createResource.append(list)

    sumRarity = 0

    def calculateRarity(self):
        for item in self.naturalResources:
            self.sumRarity += item.rarity
