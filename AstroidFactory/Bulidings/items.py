#----------------------------------------------------------------
#frame

class Item: #frame
    state = ""
    recipe = [[]]
    name = "item"
    description = "ester egg"
class Solid(Item):
    state = "solid"

class Liquid(Item):
    state = "liquid"

class Gas(Item):
    state = "gas"

class Special(Item):
    state = "special"

#----------------------------------------------------------------
#items

#special-----
class Energy(Special):
    name = "생각중"

#solid-----
class Coal(Solid):
    name = "석탄"
    description = "석탄이다."
class Iron(Solid):
    name = "철"

class Aluminium(Solid):
    name = "알루미늄"

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

class Steel(Solid):
    name = "강철"
    recipe = [Iron[1], Manganese[1], Energy[1]]

class Osmium(Solid):
    name = "오스뮴"

#liquid-----
class Water(Liquid):
    name = "물"

class Crudeoil(Liquid):
    name = "원유"

class Collingwater(Liquid):
    name = "냉각수"
    recipe = [Water(), Energy[1]]

class Slag(Liquid):
    name = "광재"


# gas-----
class Hydrogen(Gas):
    name = "수소"

class Oxygen(Gas):
    name = "산소"

class Argon(Gas):
    name = "아르곤"

class Methane(Gas):
    name = "메테인"
    recipe = [Coal[1],Energy[1]]

# 액화된 기체
class Liquidhydrogen(Liquid):
    name = "액화 수소"
    recipe = [Hydrogen[1], Collingwater[1], Energy[1]]

class LiquidOxygen(Liquid):
    name = "액화 산소"
    recipe = [Oxygen[1], Collingwater[1], Energy[1]]