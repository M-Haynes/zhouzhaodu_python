# 字典
#   概念： 无序的，可变的键值对集合
#   方式1：
#       {key：value, key: vlaue}
#   方式2：
#       fromkeys(S,v = None)
#       静态方法：类和对象都可以调用
#           类调用： dict.formakeys("abs",666) -- ("a":666,"b":666,"c":666)
#           对象调用： dic.formakeys("abc":666) -- ("a":666,"b":666,"c":666)  --- 这个方式没什么意义
#                   此处的dic, 是实例化的字典对象
#   注意：
#       1, key 不能重复，如果重复，后值会把前值覆盖
#       2，key 必须是任意不可变类型
#           可变集合：列表、字典...
#           不可变集合：数值、布尔、字符串、元组


d = dict.fromkeys("abc")
print(d)  # {'a': None, 'b': None, 'c': None}

d = d.fromkeys([1,2,4], 777)
print(d)  # {1: 777, 2: 777, 4: 777}

dd = {1: 2}.fromkeys("abc", 333)
print(dd)  #  {'a': 333, 'b': 333, 'c': 333}


d = {1: "a", 2: "c", 1: "c"}  # key重复的情况下，只会保留一个，后面的会覆盖前面的
print(d)  # {1: 'c', 2: 'c'}

# c = {[1,2,3]: "132"} # 这里的key 必须是一个不可变的值
# print(c)  # TypeError: unhashable type: 'list'


# ---------------------------字典的常用操作----------------------------------------------

# -------------------------------- 增 ------------------------------------
#   dict[key] = value
#       当key在原字典中不存在时，即为新增操作
d = {"name": "sz", "age": 18}

d["height"] = 18
print(d)  # {'name': 'sz', 'age': 18, 'height': 18}
print(id(d))  # 2409422058240 表示存储位置没有改变 -- 改的是之前的对象


# -------------------------------- 删 ------------------------------------
# 方式一：
#   del dic[key]
#   注意： 这里的key一定时要存在的
d = {"name": "asds", "age": 18, "height": 18}
del d["age"]
print(d)  # {'name': 'asds', 'height': 18}


# 方式二：
#   dic.pop(key[,default])
#       删除指定的键值对，并返回对应的值
#       如果key， 不存在，则直接返回给定的default值 -- 不做删除动作
#       如果没有给定默认值，则报警

v = d.pop("name")
print(v,d)   # asds {'height': 18}

s = d.pop("heightsss", 111)  # 这里没有heightsss 键值，所以返回default值
print(s,d)   # 111 {'height': 18}}


#方式三：
#   dic.popitem()
#       删除最后一个键值对，并以元组的形式返回该键值对
#       如果字典为空， 则报警

d = {"name": "asds", "age": 18, "height": 18}
res = d.popitem()
print(res, d)  # ('height', 18) {'name': 'asds', 'age': 18}


# 方式四：
#   dic.clear()
#   删除字典内所有键值对
#   返回None


d = {"name": "asds", "age": 18, "height": 18}
print(d.clear())  # None
print(d)  # {}
# 对比

# del d
# print(d)  # NameError: name 'd' is not defined


# -------------------------------- 改 ------------------------------------
#   只能改值，不能改key
#   修改单个键值对：
#       dic[key] = value
#           直接设置，如果key不存在，则新增，存在则修改
d = {"name": 'ss', "age": 123, "wei": 89}
print(d)  # {'name': 'ss', 'age': 123, 'wei': 89}
d["name"] = "asds"
print(d)  # {'name': 'asds', 'age': 123, 'wei': 89}

#   批量修改键值对：
#       oldDIc.update(newDic)
#           根据新的字典，批量修改旧字典中的键值对
#           如果旧字典没有对应的key，则新增键值对

d = {"name": 'ss', "age": 123, "wei": 89}
d.update({"name": 'asds', "age": 3, "niu":666})
print(d)  # {'name': 'asds', 'age': 3, 'wei': 89, 'niu': 666}


# -------------------------------- 查询 --------------------------------
# 获取单个值
# 方式一：
#   dic[key]
#       如果key不存在，会报错
d = {"name": 'ss', "age": 123, "wei": 89}
print(d["name"], type(d["name"]))  # ss, <class 'str'>

# 方式二：
#   dic.get(key[,default])
#       如果不存在对应的key，则去给定的默认值 default，如果没有默认值，则为None，但是不会报错，但是原字典不会新增键值对
d = {"name": 'ss', "age": 123, "wei": 89}
print(d.get("name", 111))  # ss
print(d.get("sss", 111))  # 111

# 方式三：
#   dic.setdefault(key[,default])
#       获取指定key对应的值
#       如果key不存在，则设定默认值，并返回该值，default，如果没给定，则使用None代替
#       如果查询的key不存在,则会在原字典里新增一个查找的键值对
d = {"name": 'ss', "age": 123, "wei": 89}
print(d)  # {'name': 'ss', 'age': 123, 'wei': 89}
print(d.setdefault("lll", 111)) # 111
print(d)  # {'name': 'ss', 'age': 123, 'wei': 89, 'lll': 111}


# 获取所有的值
#   dic.values()
d = {"name": 'ss', "age": 123, "wei": 89}
vs = d.values()
print(vs)  # dict_values(['ss', 123, 89])

# 获取所有的键
#   dic.key()
d = {"name": 'ss', "age": 123, "wei": 89}
ks = d.keys()
print(ks)  # dict_keys(['name', 'age', 'wei'])

# 获取字典的键值对
#   dic.items()
d = {"name": 'ss', "age": 123, "wei": 56}
ites = d.items()
print(ites) # dict_items([('name', 'ss'), ('age', 123), ('wei', 56)])

# 注意： 这里获取到的值，都是以字典视图的形式展示，要想取到其中的值，需要进行类型转换 --- list、tuple


# -------------------------------- 遍历 ------------------------------------
# for in
# 先遍历所有的key， 然后，根据指定的key，获取到对应的值
d = {"name": 'ss', "age": 123, "wei": 89}
for k in d.keys():
    print(k)  # name
    print(k, d[k])  # name , ss


# for k,v in dic.items():
# 直接遍历所有的键值对
for k, v in d.items():
    print(k, v)  # name ss


# --------------------------------- 计算 ---------------------------------
# len(dic)
#   键值对的个数
d = {"name": 'ss', "age": 123, "wei": 89}
print(len(d))


# --------------------------------- 判断 ------------------------------------
# in 、  not in

# x in dic
#   判定dic中的key，是否存在x
d = {"name": 'ss', "age": 123, "wei": 89}
print("name" in d) # True
print("ss" in d)  # False


# x not in dic
#   判定dic中的key，是否不存在x
d = {"name": 'ss', "age": 123, "wei": 89}
print("name" not in d)  # False
print("ss" not in d)  # True


