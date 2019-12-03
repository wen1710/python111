name = 'hello world!'
print(name.title())
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)


#list
names = ['lily', 'jivan', 'tom' ,'samon']
print(names[0].title())
print(names[1])
print(names[-1])


#操作list，list的增删改查
names.append('ketty')#在list增加一个值，只能在最后增加。
names.insert(0, 'jane')#在list任意地方增加一个值
del names[0]#删除list其中一个元素
name = names.pop(1)#删除list其中一个元素，并把它保存到一个变量，可以使用它。
names.remove('tom')#直接删除list其中一个值
names[0] = 'kate'#修改list其中一个值
print(names)
print(name)
print(names[0])

cars = ['bmw', 'audi', 'toyota', 'subaru']
#组织列表
print(cars) 
cars.sort()#按字母a-z的顺序从新排列。
print(cars)
cars.sort(reverse = True)#增加reverse参数为True按a-z倒序排列
print(cars)
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars))#临时按字母a-z的顺序排列。
print(sorted(cars, reverse = True))#增加reverse参数为True临时按a-z倒序排列
print(cars)


