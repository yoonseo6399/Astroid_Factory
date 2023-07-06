#----------------------------------------------------------------
#frame

class item: #frame
    state = ""
    recipe = [[]]
    name = "item"
    description = "ester egg"
class solid(item):
    state = "solid"

class liquid(item):
    state = "liquid"

class gas(item):
    state = "gas"

class special(item):
    state = "special"

#----------------------------------------------------------------
#items

#special-----
class energy(special):
    name = "생각중"

#solid-----
class coal(solid):
    name = "석탄"
    description = "석탄이다."
class iron(solid):
    name = "철"

class aluminium(solid):
    name = "알루미늄"

class titanium(solid):
    name = "티타늄"

class tungsten(solid):
    name = "텅스텐"

class manganese(solid):
    name = "망가니즈"

class uranium(solid):
    name = "우라늄"

class copper(solid):
    name = "구리"

class steel(solid):
    name = "강철"
    recipe = [iron[1],manganese[1],energy[1]]

class osmium(solid):
    name = "오스뮴"

#liquid-----
class water(liquid):
    name = "물"

class crudeOil(liquid):
    name = "원유"

class collingWater(liquid):
    name = "냉각수"
    recipe = [water[1],energy[1]]

class slag(liquid):
    name = "광재"


# gas-----
class hydrogen(gas):
    name = "수소"

class oxygen(gas):
    name = "산소"

class argon(gas):
    name = "아르곤"

class methane(gas):
    name = "메테인"
    recipe = [coal[1],energy[1]]

# 액화된 기체
class liquidHydrogen(liquid):
    name = "액화 수소"
    recipe = [hydrogen[1],collingWater[1],energy[1]]

class liquidOxygen(liquid):
    name = "액화 산소"
    recipe = [oxygen[1],collingWater[1],energy[1]]