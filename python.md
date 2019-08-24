![](/Volumes/Code/python/images/编码规范.png)

![](/Volumes/Code/python/images/命名规范.png)



操作系统（operating system）

图形用户界面（Graphical User Interface, GUI）

开源（open-source）

编程（programming）

##### 注释（comment）

注释是用英文或其他自然语言写的一行（或一部分）代码，行首均有一个特殊标志告知编程语言忽略这行代码。 Python 用井号（ #）来创建注释。 

```python
# 这是一行注释
```

中文编码声明注释

```python
#coding=编码
#coding:utf-8
```



##### 打印(print)

```python
print("hello world!")
```

输入（input）

```python
a = input("请输入名字：")
```



##### 多行代码



有时一段代码比较长，超过了一行，可以用三引号、圆括号、方括号或者大括号扩展至新一行，示例如下： 

```python
print("""This is a really really
	  really really long line of
	  code.""")
#另外可以使用反斜杠\对代码进行换行。
print\
("""This is a really really
really long line of code.""")
```

上述两个例子的输出结果是一样的。反斜杠可以让我们将("""This is a reallyreally really long line of code.""")和 print 放在不同的行，这种情况一般是不允许的。 

##### 关键字（keyword）

Python 等编程语言中有一些具备特殊意义的字，即关键字（ keyword）。 

##### 缩进

缩进可以告诉 Python解释器代码块的开始与结束 。

```python
for i in range(100):
    print("Hello, World!")
```

##### 数据类型（data type）

Python 将数据划分成不同的类别，即数据类型（ data type）。

在 Python 中，每一个数据值，如 2 或"Hello, World!"，被称为对象（ object） 

对象的唯一标识（identity），指的是其在计算机内存中的地址，该地址不会变化。 

字符串（str，string的缩写），字符串是由引号包括
的一个或多个字符组成的序列。 字符（ character）是类似 a 或 l 这样的单个符号。可以
使用单引号或双引号来表示字符串，但是前后的引号必须保持一致。

整数（ 1， 2， 3， 4 等）的数据类型为整型数据（int，全称为 integer）。 

小数（带小数点的数字）的数据类型为 float。 2.1、 8.2 和 9.9999 都是数据类型为float 的对象，我们称之为浮点数（ floating-point number）。 

数据类型为 bool 的对象被称为布尔值（ boolean），仅有 True 和 False 两个值。 

数据类型为 NoneType 的对象，其值永远为 None，用来表示数据缺失。 

##### 常量和变量

常量（ constant）是一个永远不会改变的值。上面示例中的每一个数字，都是常量；数字 2 永远表示的值为 2。 变量（ variable）则相反，指的是会改变的值。变量由一个或多个字符组成的名称构成，并使用赋值符（ assignment operator）等号赋予了这个名称一个值 。

编程时经常需要增加（ increment）或减小（ decrement）某个变量的值。考虑到这个操作非常普遍， Python 提供了特殊语法进行增减变量的值。 

```python
x = 10
x = x + 1 
# x = += 1
# x = 11

x = 10 
x = x - 1
# x -= 1
# x = 9
```



只要遵守以下 4 条原则，可以随意命名变量。
1．变量名不能包含空格符。如果想在变量名中使用两个单子，可以在中间加入下划线，如 my_variable = "A string!"。
2．变量名只能使用特定的字母、数字和下划线。
3．变量名不能以数字开头。虽然可以使用下划线开头，但是这种命名方式有着特殊的意义，后面内容会提到。因此在此之前尽量避免这种情况。
4．不能使用 Python 关键字作为变量名。可在网页 http://theselftaughtprogrammer.io/keywords 中查看所有关键字。 

##### 语法（syntax）

语法指的是规范一门语言中句子结构，尤其是字词顺序的一整套规则及流程。 

在 Python 中，字符串永远被包括在引号内。 



##### 错误与异常 （exception）

Python 有两种错误： 语法错误和异常。 不属于语法错误的错误， 就是异常（ exception）。 

##### 算术操作符

操作符（ operator）

算术操作符（ arithmetic operator）



| 操作符 | 含义            | 示例    | 运算结果 |
| ------ | --------------- | ------- | -------- |
| **     | 指数运算        | 2 ** 2  | 4        |
| %      | 取模运算        | 14 % 4  | 2        |
| //     | 整除/地板除运算 | 13 // 8 | 1        |
| /      | 除法运算        | 13 / 8  | 1.625    |
| *      | 乘法运算        | 8 * 2   | 16       |
| -      | 减法运算        | 7 - 1   | 6        |
| +      | 加法运算        | 2 + 2   | 4        |

两个数相除时，会有一个商和一个余数。商就是除法运算的结果，余数即剩下的值。取模操作符返回的就是余数。 对两个数取模时，如果没有余数（返回 0），则被取模的数字为另一个数字的倍数。如果有余数，则不是其倍数。因此取模运算被用于检验数字的奇偶性。

操作符两侧的值（以上示例中就是数字）被称为操作数（ operand）。两个操作数和一个操作符共同构成一个表达式（ expression）。 

运算顺序（ order of operation），指的是数学计算中对表达式求值的一套规则。可使用 PEMDAS 方法， 帮助记忆数学公式的运算顺序： 括号（ parentheses）、 指数（ exponents）、乘法（ multiplication）、除法（ division）、加法（ addition）和减法（ subtraction）。括号的优先级大于指数符号，后者又优先于乘法和除法，最后才是加法和减法。

##### 比较操作符（ comparison operator）

比较操作符是 Python 中的另一种操作符。与算术操作符类似，比较操作符可用于表达式任意一侧的操作数；不同的是，带有比较操作符的表达式最后求值的结果不是 True 就是 False。 

| 操作符 | 含义       | 示例     | 运算结果 |
| ------ | ---------- | -------- | -------- |
| >      | 大于       | 100 > 10 | True     |
| <      | 小于       | 100 < 10 | False    |
| >=     | 大于或等于 | 2 >= 2   | True     |
| <=     | 小于或等于 | 1 <= 4   | True     |
| ==     | 等于       | 6 == 9   | False    |
| !=     | 不等于     | 3 != 2   | True     |

#####　逻辑操作符 （ logical operator）

逻辑操作符也是 Python 中的一类操作符。与比较操作符类似，逻辑操作符的求值结果也是 True 或 False。 

| 操作符 | 含义 | 示例          | 运算结果 |
| ------ | ---- | ------------- | -------- |
| and    | 与   | True and True | True     |
| or     | 或   | True or False | True     |
| not    | 非   | not True      | False    |

##### 条件语句 

关键字 if、 elif 和 else 用于条件语句（ conditional statement）。条件语句是一种控制结构（ control structure）：通过分析变量的值从而做出对应决定的代码块。条件语句是可根据条件执行额外代码的代码。  

```python
if x==1:
    print("x is one")
elif x!=1:
    print("x is not one")
else:
    print("other")
```



##### 语句 

语句（ statement）这个术语可用来描述 Python 语言的多种构成部分。可以将一个Python 语句视作一个命令或计算。 

Python 中有两类语句： 简单语句（simple statement） 和复合语句（ compound statement）。简单语句一般就是一行代码， 而复合语句通常包括多行代码。 

复合语句由一个或多个从句（ clause）组成。从句包括两行或多行代码： 代码头（ header）及紧随其后的配套代码（ suite）。 

语句还有一点要注意，语句之间是可以有空格的，这不会影响代码的执行。空格有时被用来提高代码的可读性。 





##### 函数

函数（ function）：可接受输入，执行指令并返回输出的复合语句。通过函数，我们可以在程序中定义功能，并重复使用。 

![](C:\Users\Administrator\Desktop\python\images\function.png)

调用（ call）一个函数，意味着为函数提供执行指令并返回输出所需的输入。函数的每一个输入就是一个参数（ parameter）。当你为函数提供参数时，则被称为“函数传参”。 

```python
def [函数名]([参数]):
6 [函数定义]
#定义一个函数
def f(x):                   #f为函数名，函数命名规则和命名变量规则一致
    return x * 2            #返回值
#调用变量
a = f(6)
print (a)

```

关键字 def 告诉 Python 操作者正在定义一个函数。在 def 关键字后面，指定函数的名称，名称选择遵循与变量名相同的规则。 

按惯例，函数名不应使用大写字母，单词用下划线分隔： like_this。 

最后，函数必须包含 return 语句。如果函数没有 return 语句，则会返回 None。 

##### 内置函数

Python 编程语言中自带了一个被称为内置函数（ builtin function）的函数库，它可执行各式各样的计算和任务，而不需任何额外的工作。 

内置函数type()可以返回变量类型

内置函数id()可以获取变量的内存地址



##### 复用函数

函数不仅可用于计算并返回值，还可以封装我们希望复用的功能。 

```python
def even_odd(x):
    if x % 2 == 0:
        print ("even")
    else:
        print ("odd")

```



函数可接受两种参数。目前所看到的都是必选参数（ required parameter）。当用户调用函数时，必须传入所有必选参数，否则 Python 将报告异常错误。
Python 中还有另一种参数，即可选参数（ optional parameter）。函数只在需要时才会
传入，并不是执行程序所必须的。如果没有传入可选参数，函数将使用其默认值。使用如下语法定义可选参数： [[函数名]([参数名]=[参数值]) ]。与必选参数一样，可选参数也得使用逗号分隔。 



##### 作用域

变量有一个很重要的属性， 作用域（ scope）。定义变量时，其作用域指的是哪部分程序可以对其进行读写。读取一个变量意味着获取它的值，写变量意味着修改它的值。
变量的作用域由其定义在程序中所处的位置决定。 

如果在函数（或类）之外定义了一个变量，则变量拥有全局作用域（ global scope）：即在程序中任意地方都可以对其进行读写操作。带有全局作用域的变量，被称为全局变量（ global variable）。如果在函数（或类）内部定义一个变量，则变量拥有局部作用域（ local scope）：即程序只有在定义该变量的函数内部才可对其进行
读写。 

可以在程序的任何地方对全局变量进行写操作，但是在局部作用域中需稍加注意：必须明确使用 global 关键字，并在其后写上希望修改的变量。  

```python
x = 100
def f():
    global x
    x += 1
    print(x)
```

##### 异常处理

异常处理（ exception handling），支持测试错误条件，在错误发生时捕获异常，然后决定如何
处理 。

异常处理使用 try 和 except 关键字。 try 从句包含可能会发生的错误， except 从句包含仅在错误发生时执行的代码。 

Python 中 的 每 一 个 异 常 都 是 一 个 对 象 ， 可 在 如 下 网 址 查 看 所 有 内 置 异 常 ：
https://www.tutorialspoint.com/python/standard_exceptions.htm。如果你认为代码可能会报
告异常，可使用关键字 try 和 except 来捕获。 

```python
a = input ("type a number:")
b = input ("type another:")
a = int (a)
b = int (b)
print (a/b)
#b如果是0就会报下面错，任何数都不可以除以0的。
Traceback (most recent call last):
  File "E:/code/python/02.py", line 5, in <module>
    print (a/b)
ZeroDivisionError: division by zero
—————————————————————————————————————————————————————————————————————————————————————————
a = input ("type a number:")
b = input ("type another:")
a = int (a)
b = int (b)
try:
    print (a/b)
except ZeroDivisionError:
    print ("b cannot be zero")
#如果用户为 b 参数提供的输入不是 0，则执行 try 代码块， except 代码块不执行。如果用户为 b 参数提供的输
#入为 0， Python 不会报错，而是执行 except 代码块，并打印“b cannot be zero.”。    
—————————————————————————————————————————————————————————————————————————————————————————        
try:
    a = input ("type a number:")
    b = input ("type another:")
    a = int (a)
    b = int (b)
    print (a/b)
except (ZeroDivisionError ,
        ValueError):
    print ("b cannot be zero or Invalid input")
#将收集用户收入的部分代码移入 try 语句内，并让 except 语句注意两个异常（ ZeroDivisionError 和   ValueError）即可解决问题。如果向 int、 str 或 float 等内置函数中传入无效输入，则会出现 ValueError。在 except 关键字后添加圆括号，并用逗号分隔两个异常即可将二者捕获。

```

不要在 except 语句中使用 try 语句定义的变量， 因为异常可能是在变量定义之前发生的，如果在 except 语句中这样做可能又会导致新的异常出现。 

##### 文档字符串

定义一个带参数的函数时，有时要求参数必须是某种数据类型，函数才能成功执行。那么该如何将这点告知函数的调用者？在编写函数时，在函数顶部留下注释来解释每个参数应该为何种数据类型，是比较好的做法。这些注释被称为文档字符串（ docstring）。 

```python
def add (x, y):
    """
    返回 x + y 的值
    :param x: int.
    :param y: int.
    :return: int , x 与 y 之和
    """
    return x + y
```

**只有在后面的程序中会用到数据，才有必要将其保存至变量。不要仅仅为了打印数值就将整数保存至变量。**

#### 容器

容器就像是文件柜，可有效整理数据。3 个常用的容器：列表、元组和字典。 

##### 方法（method）

方法是与指定数据类型紧密相关的函数。方法与函数一样，可执行代码并返回结果。不同的是，只有在对象上才能调用方法。同样也可以传递参数给方法。 

##### 列表（list）

列表（ list）是以固定顺序保存对象的容器 。

![](C:\Users\Administrator\Desktop\python\images\list.png)

```python
#创建一个空列表
fruit = list()
fruit = []
#将水果存进列表fruit
fruit = ["apple","orange","pear"]
#在末尾增加banana和peach
fruit.append("banana")
fruit.append("peach")
```

上述示例中的列表有 3 个元素： "Apple"、 "Orange"和"Pear"。列表中的元素是有序的。除非你重新调整列表中元素的顺序，否则"Apple"永远是第一个元素，"Orange"是第二个元素， "Pear"则是第三个元素。 "Apple"位于列表的开头，末尾则是"Pear"。这里可使用 append 方法向列表中添加一个新元素。 传递给 append 方法的两个对象现在都加入了列表。但 append 方法永远是将新元素添加至列表的末尾。 

**列表不仅可以保存字符串，它还可以保存任意数据类型。 **

```python
random = []
random.append(True)
random.append(100)
random.append(1.1)
random.append("hello")
```

字符串、列表和元组都是可迭代的（ iterable）。如果可以使用循环访问对象中的每一个元素，那么该对象是可迭代的，被称为可迭代对象。可迭代对象中的每一个元素都有一个索引（ index），即表示元素在可迭代对象中位置的数字。列表中第一个元素的索引是 0，而不是 1 .

```python
#获取random列表中的索引2的值
random [2]
```



列表是可变的（ mutable）。如果一个容器是可变的，则可以向该容器中增删对象。将列表中某个元素的索引赋给一个新的对象，即可改变该元素 .

- 也可使用 pop 方法移除列表中的最后一个元素 
- 你可以使用加法操作符来合并两个列表： 
- 也可以使用关键字 in 检查某个元素是否在列表中
- 使用关键字 not 检查某个元素是否不在列表中 
- 使用函数 len 可获得列表的大小（包含元素的个数） 

##### 元组

元组（ tuple）是存储有序对象的一种容器。 与列表不同， 元组是不可变的（ immutable），这意味着其内容不会变化。创建元组后，无法修改其中任何元组的值，也无法添加或修改元素。用圆括号表示元组，且必须用逗号分隔元组中的元素。 

```python
#创建一个空元组
my_tuple = tuple()
my_tuple = ()
#创建一个元组
my_tuple = ("Jackson", 1987, True)
```

**即使元组中只有一个元素，也需要在该元素的后面加上逗号。**只有这样， Python 才能将其与其他为了表示运算顺序而放在圆括号中的数字标记进行区分。 

创建元组之后， 不能再新增元素或修改已有元素。  

可使用与列表一样的方法来获取元组的元素，即引用其索引 

可使用关键字 in 来检查某个元素是否在元组中：

在 in 前加上关键字 not 即可检查元素是否不在元组中：

##### 字典

字典（ dictionary）是另一种用于存储对象的内置容器。它们被用来链接键（ key）和值（ value）这两个对象（如图 5-2 所示）。将一个对象链接至另一个对象，也被称为映射（ mapping），结果为产生一个键值对（ key-value pair）。可将键值对添加到字典，然后使用键在字典中查询，可获得其对应的值。但是无法使用值来查询键。 

![](C:\Users\Administrator\Desktop\python\images\dictionary.png)

字典是可变的，因此可以向字典中新增键值对。与列表和元组不同，字典中存储的对象是无序的。字典的价值在于键与值之间的关联。 

```python
#创建一个空字典
my_dict = dict()
my_dict = {}
#创建一个字典
fruits = {"Apple":
          "green",
          "pear":
          "yellow"}
#添加键-值对
fruits ["Watermelon"] =  "red"
#查找键对应的值
fruits ["Watermelon"]
```

可以在创建字典时直接添加键值对。上述两种语法都要求用冒号分隔键与值，每个键值对之间用逗号分隔。与元组不同的是，如果只有一个键值对，不需要在其后添加逗号。 

字典是可变的。创建字典后，可通过语法[字典名][[键] = [值]添加新的键值对，并通过语法“[字典名][[键]”查找值。 

字典的值可以是任意对象。 但是字典的键必须是不可变的。  字符串或元组可以用作字典的键， 但是列表或字典不可以。 

可以使用关键字 in 检查某个键是否在字典中，但不能用其检查某个值是否在字典
中。 

在关键字 in 之前加上关键字 not，可检查键是否不在字典中。 

可使用关键字 del 删除字典中的键值对。 

##### 容器嵌套容器 

#### 字符串操作

#### 循环（ loop） 

##### for循环

for 循环：一种用来遍历可迭代对象的循环。这个过程被称为遍历（ iterating）。 我们可使用 for 循环来定义可迭代对象中每个元素都要执行一次的指令，然后在指令中对每个元素进行访问和操作。 

可使用语法"for [变量名] in [可迭代对象名]: [指令]"定义 for 循环，其中[变量名]是计划赋给可迭代对象中每个元素值的变量名称， [指令]是每次循环要执行的代码。 

![](C:\Users\Administrator\Desktop\python\images\for.png)

```python
for i in [1,2,3,4,5]:
    print(i)
```

使用 for 循环遍历了列表 x，并通过一个索引变量（ index variable）跟踪列表内当前的元素。索引变量是代表可迭代对象中索引的一个整数，起始值为 0，每循环一次索引变量的值递增一个。 

```python
# 将列表x全部变成大写，需要用for循环遍历x列表，然后调用方法生成大写。
# 新建一个列表
x = ["ha","he","ai"]
# 索引赋给变量a
a = 0                       
# 需要把列表所有字母变成大写
for i in x:
# 把单个字母赋值给变量new    
    new = x[a]
# 把字母调用方法变成大写并保存到变量new
    new = new.upper()
# 将变量new的值赋给列表
    x [a] = new
# 索引加1
    a += 1
print (x)

```

##### range 函数 

使用内置的 range 函数创建一个整数序列，然后通过 for 循环遍历。 range 函数接受两个参数：序列起始数字和结束数字，返回的整数序列包含从第一个参数到第二个参数之间（不含第二个参数）的所有整数。 



```python
for i in range(0,101,2):
    print (i)
```

##### while循环

while 循环：它是一种只要表达式的值为 True 就一直执行代码的循环。 while 循环的语法是“while [表达式]: [执行代码]”，其中“[表达式]”是决定循环是否继续进行的表达式， “[执行代码]”则是只要循环继续就执行的代码。 

```python
x = 10 
while x > 0:
    print (x)
    x -= 1
    
```

如果你定义的 while 循环的表达式求值永远为 True，循环将不会停止执行。一个不会停止执行的循环也被称为死循环（ infinite loop）。 

##### break 语句 

使用 break 语句（带关键字 break 的语句）来终止循环。 

```python
x = 10
while x > 0:
    print (x)
    if x == 5:
        break
        
        
for i in range (0,100):
    print (i)
    if i == 10:
        break
```

##### continue 语句 

使用 continue 语句（带关键字 continue 的语句）来终止循环的当前迭代，并进入下一次迭代。 

```python
#打印从 1 到 5 之间除了 3 以外的所有数字
for i in range (0,10):
    if i == 3:
        continue
    print (i)
```

##### 嵌套循环 

可以通过多种方式对循环进行组合。例如，可以在一个循环里加入另一个循环，甚至在加入的循环里再加一个循环。循环中可嵌套的循环数量没有限制，但是最好要控制数量不要过多。当一个循环位于另一个循环之内时，它就是嵌套在第一个循环中。这种情况下， 内部包含一个循环的循环称为外循环（ outer loop）， 嵌套的循环称为内循环（ inner loop）。当存在嵌套循环时，外循环每遍历一次，内循环就遍历一次其可迭代对象中的所有元素。 

#### 模块

假设你写了一个有 10 000 行代码的程序。如果把全部代码写在一个文件里，查询起来将会非常困难。每次出现错误或异常时，不得不快速浏览 10 000 行代码来查找导致问题的那行。为解决这个问题，程序员将大型程序分割成多个包含 Python 代码的文件，也被称为模块（ module）。 Python 支持在一个模块中使用另一个模块内的代码。 Python 还有内置模块（ builtin module），它是 Python 语言自带的，包含了许多重要的功能。 

##### 导入内置模块

使用模块之前，必须先导入（ import）：意味着要写代码，以便让 Python 知道从哪获取模块。可使用语法 import [模块名]导入模块，将[模块名]替换为希望导入模块的名字。导入模块之后，即可使用其中的变量和函数。 

```python
#导入内置模块
import math
#调用内置模块函数
math.pow(10,30)
```

##### 导入其他模块

本节中，我们将创建一个模块，然后在另一个模块中导入该模块并使用其中的代码。首先， 在计算机上创建一个名为 tstp 的新文件夹。 在文件夹中， 新建一个名为 hello.py的文件。将如下代码添加到 hello.py 并保存文件 



在 tstp 文件夹中，再新建一个名为 project.py 的文件。将如下代码添加到
project.py 中并保存文件： 