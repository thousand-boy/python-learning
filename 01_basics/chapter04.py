coin = [1,5,10,50,100,500]
print(coin)
print(type(coin))

profile = ["ぱいせん",165,42.5,True]
print(profile)

sweets = ["プリン","ケーキ","チョコ"]
print(sweets[0])
print(sweets[1])
print(sweets[2])

sweets = ["プリン","ケーキ","チョコ"]
sweets[1] = "アイス"
print(sweets)

sweets = ["プリン","ケーキ","チョコ"]
sweets.append("アイス")
print(sweets)

sweets = ["プリン","ケーキ","チョコ"]
sweets.extend(["アイス","クッキー","ガム"])
print(sweets)

sweets = ["プリン","ケーキ","チョコ"]
del sweets[1]
print(sweets)

sweets = ["プリン","ケーキ","チョコ"]
print(len(sweets))

onsen = {"下呂温泉":"岐阜県","草津温泉":"群馬県"}
print(onsen)

onsen = {"下呂温泉":"岐阜県","草津温泉":"群馬県"}
print(onsen.get("下呂温泉"))

onsen = {"下呂温泉":"岐阜県","草津温泉":"群馬県"}
onsen["有馬温泉"] = "兵庫県"
print(onsen)

onsen = {"下呂温泉":"岐阜県","草津温泉":"群馬県","有馬温泉":"兵庫県"}
onsen["下呂温泉"] = "岐阜県下呂市"
print(onsen)

rivers1 = {"信濃川":367,"利根川":322}
rivers2 = {"石狩川":268,"天塩川":256}
rivers1.update(rivers2)
print(rivers1)

rivers1 = {"信濃川":367,"利根川":322,"石狩川":268,"天塩川":256}
del rivers1['天塩川']
print(rivers1)

rivers1 = {"信濃川":367,"利根川":322,"石狩川":268}
print(len(rivers1))

def add_numbers(a,b):
    print(a+b)

add_numbers(3,5)

add_numbers(3,5)

def add_numbers(a,b):
    return a+b

output=add_numbers(5,7)
print(output)