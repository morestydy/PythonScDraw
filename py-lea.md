[toc]

# python

## 1. python的数据类型

1. 数字

   + int:213,9999,0,-126

   + float:1.23,3.14,-9.002,1.23$$\times10^9$$(1.2e9)
   + Boolean:true,false

2. 字符串  :以'',""括起来的任意文本

   + " I 'm OK' ", 'I\'m ok'
   + r"字符内容"防止字符转义
   + 三引号允许一个字符串跨行

3. distance = 1000

   + 使用type(name)查询数据类型

4. 运算符

   \+ - X / % //(整除) **(次方运算)

5. 赋值运算符

   x+=y  x=x+y

   x/=y  x=x/y

6. 比较运算符

7. 列表  list类型

   1. 使用[]标识

      classmates = ['Michael','Bob','Trancy']

   2. ![image-20221021221407393](py-lea.assets/image-20221021221407393.png)

      索引从0开始  classmates[0]

   3. 截取区间:classmates[0:1]

      classmates[:2]:截取0到2的元素

      classmates[1:]:从2到最后的元素

   4. 替换元素

      1. classmates[2]='Andy'

   5. 添加新元素

      classmates.append('Andy')

      使用insert()方法插入置顶的索引位置,之前位置不改变,后面后移

   6. 删除元素  默认删除最尾部元素

      classmates.pop(1):之后位置的元素前移

8. 元组类型 yuple

   1. 采用()标识,与列表类似,但不可修改
   2. (element1,element2,element3...)

9. 字典类型 dictionary

   1. 使用{}标识,存放具有映射关系的数据

   2. {'key':'value,'key2':'value}

   3. ![image-20221021222356470](py-lea.assets/image-20221021222356470.png)

   4. 通过key访问value

      + key不允许重复

   5. 添加或修改value:dict['key'] = 'value'

      dict['年龄'] = 23

   6. 删除字典数据: pop(key)

      dict.pop('高压')

10. 集合(set)

    1. 一组无序且不重复元素的集合

    2. parame = {ele1,ele2,...}

       parame = set()[ele1,ele2,ele3...])

    3. 如创建空集合用set()函数

    4. 使用in 或 not in 判读男是否存在于集合中

    5. 添加元素

       s.add('element')

    6. 删除元素: s.remove('element')

       s.clear()删除集合中所有的元素

    7. 并集 S1 | S2

       交集 S1 & S3

       补集 S1 - S2

### 控制语句

1. 顺序结构

2. 选择结构

   if.......else.....

   if.......elif........else......

3. 循环

   + while循环

   ```python
   while condition:
   	run1:
   run2:
   ```

   + for-in循环

   使用range()函数

   ```python
   for 变量名 in range(5):
   	代码块
   ```

   ```
   # 创建一整个函数列表
   range(start,end,step=1)
   
   ```

   使用序列选项迭代列表对象

   for x in sequence:

   ​	代码块

   ```python
   patient = {"Al","Bob","Cath"}
   for p_name in patient:
   	print(p_name)
   ```

   使用枚举函数迭代对象

   ```python
   for index,x in enumerate(sequence):
   	代码块
   ```

   break和continue

   ​	break:提前退出

   ​	continue:跳出当前这次循环,直接下一次循环

   

## Pandas数据分析工具

`import pandas as pd`

两个数据结构:Series,DataFrame

1. series

   带索引的一维数组

   `pd.Series([1,'apple','3.5,4])`

2. DataFrame

   表格型的数据结构

   `pd.DataFrame({'Animal':['dog','cat'],'owner':['A','B']})`

   <img src="py-lea.assets/image-20221022105004139.png" alt="image-20221022105004139" style="zoom:50%;" />

3. 文件读写

   绝对路径

   - 'C:\\Users\\text.txt'
   - r'C:\Users\text.txt
   - 'C:/Users/text.txt'

   相对路径

   - ,\:当前目录
   - ..\上级文件
   - os.getcwd()查看当前路径

   `data = pd.read_csv('sample.txt',sep=' ')`

   ```python
   data = pd.read_csv('sample.csv')
   ```

   + seq:默认使用逗号分隔
   + 第一行不是列明,`data=pd.readcsv(file,header=None)`

   ```
       0      1     2
   0  ID   Name  temp
   1   1  Alice    70
   2   2    Bob  37.1
   3   3  Cathy    37
   ```

   ​	

   1. 读入某列的文本

      ```python
      data = pd,read_csv("E:\\sample.csv",usecols=['id','Age'])
      ```

   2. 读入前N行的文本

      ```python
      data = pd,read_csv("E:\\sample.csv",nrows=2)
      
      ###
         ID   Name  temp
      0   1  Alice  70.0
      1   2    Bob  37.1
      ```

      `pd.read_csv(file,skiprows=2)`从第三行开始读取(包含列名)

   3. 文本的写入

      + 覆盖已有文件:`data.to_csv(file,index=False)`不写入行索引.`encoding = 'utf_8_sig'`中文支持
      + 追加内容:``data.to_csv(file,index=False,mod='a')``

4. EXcel文件的读写

   1. 单一sheet的读取:data=pd.read_excel(file)

   2. 多个Sheet的读取:`data=pd.read_excel(file,sheet_name='Sheet_2')`

      `data=pd.read_excel(file,usecols=['id','Age])`

   3. 写入单一Sheet

      `data.to_excel(file,sheet_name='sheet1',index=False)`

   4. 同时写入多个Sheet

      ```python
      with pd.ExcelWriter(file) as writer:
          data.to_excel(writer,sheet_name='sheet1',index=false)
          data_1.to_excel(writer,sheet_name='sheet2',index=False)
          
      ```

      ​	<img src="py-lea.assets/image-20221022155703060.png" alt="image-20221022155703060" style="zoom:33%;" />

   5. 数据分析文件的读取

      1. sas文件读取

         `data = pd.read_sas('filepath')`

      2. spass文件读取

         `data=pd.read_spass('filepath\xx.sav')`

   6. ![image-20221022160154197](py-lea.assets/image-20221022160154197.png)

##  文件的操作

1. 获取目录下文件:自带标准库pathlib

   from pathlib impore Path

   f=Path('test.csv')

   <img src="py-lea.assets/image-20221022172918658.png" alt="image-20221022172918658" style="zoom:67%;" />

   <img src="py-lea.assets/image-20221022172857510.png" alt="image-20221022172857510" style="zoom:33%;" />

2. 获取目录的子目录或文件

   ```python
   from pathlib import Path
   file = Path('./datafolder')
   for file in filepath.iterdir():
   	printf(file)
   ```

   > 此时不能获取目录文件中子目录下的文件

   ```python
   from pathlib import Path
   filepath = Path('./datafolder')
   for file in filepath.rglob('*.*'):
   	print(file)
   ```

   > rglob()函数:递归遍历所有满足条件的文件
   >
   > \*.\*:匹配多个字符
   >
   > + \*.csv:获取所有的csv文件
   > + data.*:获取所有名为data的是所有类型的文件

3. 文件批量移动

   ```python
   from pathlib import Path
   import shutil
   dstpath = Path('./des')
   filepath = Path('/datafolder')
   filelist = filepath.rglob('*.csv')
   for file in filelist:
   	shutil.copy(file,dstpath)
   ```

4. 文件批量重命名

   ![image-20221022173920066](py-lea.assets/image-20221022173920066.png)

   5. 文件批量读写

      <img src="py-lea.assets/image-20221025090146150.png" alt="image-20221025090146150" style="zoom:67%;" />

      + pd.condat([df1,df2])

        `axis=0`默认列对齐

        ​		- `axis=1`行对齐

        `keys = ['df1','df2']`

        `join='outer'达到两个表的并集`

        		- `join='inner'得到两个表的交集`

        `ignore_index=false`重新排列索引

        <img src="py-lea.assets/image-20221025090421957.png" alt="image-20221025090421957" style="zoom:50%;" />

        ![image-20221025090815961](py-lea.assets/image-20221025090815961.png)

        ![image-20221025091053477](py-lea.assets/image-20221025091053477.png)

      

      pd.append(df2)

      
      
      
      
      
      
      ```python
      from pathlib import Path
      import shutil
      
      print(Path.cwd())
      file = Path(./file)
      # print(file.absolute())
      # print(file.parent)
      folder = Path(''./file')
      # 获取目录的文件和目录
      for file in folder.iterdir():
      		print(filr.name)
      for file in folder.rglob('*.*')
              print(file.name)
      # 文件批量移动shutil
      dstfile = Path('./dstfile')	
      if not dstfile.exists():
              dstfile.mkdir()  #if exist ,mkdir     
      scrfolder = Path('./file')
      for file in scefolder.rglob('*.txt'):
              shutil.copy(file,dstfile)
      ```
### 批量重命名
      filepath = Path('./filep')
      for index,file in enumerate(filepath.rglob('*.csv')):
               name = 'testdate'+str(index+1)+'.csv'
               file.name(name)


### 数据预处理

1. 缺失数据的查找与处理

   - `np.nan(Not-a-Number,缺失数值)`

     float类型,可用于数学计算,但返回nan值

   - `pd.NaT(缺失时间)`

   - `pd.read_csv(filep,na_values=['999','e])`出现999,e自动用NaN代替

   <img src="py-lea.assets/image-20221202163824051.png" alt="image-20221202163824051" style="zoom:50%;" />

   + `df.isna()`:True:有缺失值,False:没有缺失值

     <img src="py-lea.assets/image-20221202164342133.png" alt="image-20221202164342133" style="zoom:50%;" />

     - 判断每列是否存在缺失值：`df.isna().any()`
     - 判断每行是否存在缺失：`df.isna().any(axis = 1)`
     - 判断整个Dataframe中是否存在缺失值df.isna().any().any()
     - 每列缺失个数:`df.isna().sum()`
     - 每行缺失值个数：`df.isna().sum(axis=1)`
     - Dataframe中缺失值总个数:`df.isna().sum().sum()`

   + 删除缺失数据`df.dropna()`

     + 删除包含1个以上缺失值的列：`df.dropna(axis =1)`
     + 保留至少有2个非NaN数据的行：`df.dropna(thresh=2)`
     + 删除所有数据均缺失的行：`df.dropna(how='all')`
     + 指定删除指定列中含有缺失值的行：`df.dropna(subset=['A'，'C'])`
     + 原地代替，将删除后的值更新至变量：`df.dropna(inplace=True)`
       + 等价于`df = df.dropna()`

   + 填充确实数据`df.fillna()`

     + 特定数值：

       `df.fillna(0，inplace=True)`
       `df = df.fillna(0)`

     + 每列分别制定数值
       `values =['A'：0，'B'：1]`

       `df.fillna(value = values)`

     + 前其他数值填充：
       前值：`df.fillna(method='ffill')`
       后值：`df.fillna(method='bfill')`
       平均：`df.fillna(df.mean)`
       最大：`df.fillna(df.max)`

2. 重复数据的查找与处理

   + 查找重复数据`df.duplicated()`:True：有重复值；False:没有重复值
     + 查找指定列重复的数据：`df.duplicated)subset =['A'，'C'])`
   + 删除重复数据`df.drop_duplicates()`
     + 保留第一次出现的重复行，删除后面的重复行：df.drop_duplicates))
       keep = False/'first'/'Last'：删除时是否保留第一项、最后一项
     + 删除指定列相同的数据：`df.drop_duplicates(subset=['A'，'C'])`
     + `inplace=True`：原地替代

   <img src="py-lea.assets/image-20221202170111398.png" alt="image-20221202170111398" style="zoom:50%;" />

   

3. 异常数据的查找与处理

   + df[异常条件]

     + `df[df.A >=2]`：显示所有A列值大于2的
       所有行数据
     + 多个条件时，使用&或|进行连接如：`df[(df.A >= 2)&(df.B > = 1)]`

   + df[异常条件]=替换值

     + df.describe()：返回数据的统计信息

     <img src="py-lea.assets/image-20221202171403859.png" alt="image-20221202171403859" style="zoom:50%;" />

4. 离散化与面元划分`pd.cut()`
   
   + `ages =[18，22，25，27，21，23，37，31，61，45，41，32]`
   
   + `bins =[0，10，18，30，50，100]`
   
     - 划分至5个区间：`(0，10]，(10，18]，(18，30]，(30，50]，(50，100]`
   
   + `cats = pd.cut(ages，bins)`
   
     - right=False：设置为左闭右开													
     - cats.codes获得划分结果：[122222334333]
     - pd.value_counts(cats)：返回面元计数结果
     - labels =[儿童'，'少年'，'青年'，'中年'，'老年]
       <img src="py-lea.assets/image-20221202171902222.png" alt="image-20221202171902222" style="zoom:33%;" />
   
   + `cats = pd.cut(ages, 4, precision = 2)`
   
     + 将数据分成4组，限定小数为2位
     + (61-18)/4：最大值-最小值，除以划分个数，得出的时每个区间的年龄范围，计算结果为10.75，则自动生成)28.75，39.5，50.25，61.0)
     + 不指定面元切分的起始结束值，而是指定面元切分的个数)切成几份)，自动计算面元起始与结束值
   
   + `cats = pd.qcut(ages，[0，0.1，0.5，0.9，1.0])`
   
     + 将数据按照自定义分位数)0-1之间的数值，包括端点)
   
     + cats = pd.qcut(ages，4)
   
       - 将数据按照四分位数进行切割:
   
         等频划分：pd.qcut(ages，4)
         等宽划分：pd.cut(ages，4)
   
     + cats.codes：获得划分结果
       pd.value_counts(cats)：返回面元计数结果




## 爬虫

### 1. 爬虫
1 获取网页内容:网址发送请求,返回整个网页书库
2 解析网页内容:提取数据
3 保存数据


Request(获取)+Beautiful Soup(解析)
Biopython库(Entrez模块),pymed库
利用第三方库直接下载PDF
调用接口实现自动英译汉

Selenium(获取)+Beautiful Soup(解析)
jiba等库进行自然语言分析获取领域热词

爬取生信数据
Biopython处理多种生物信息学问题
pysam处理基因序列工具

### Robots 协议

### 2. 爬虫常用库
1. Urllib库

+ Python内置的HTTP请求库
+ 一系列用于操作URL的功能

2. Requests库

+ 模拟浏览器操作
+ 下载网页内容

3. Selenium库

+ 模拟人自动与网站交互
+ 支持所有主流浏览器

常用解析库

4. re库
   + Python内置正则表达式模块
   + 解析速度快
5. beautifulsoup库
   + 结构化网页数据
   + 轻松获取网页内容
6. lxml库
   + 轻松处理XML和HTML文件
   + 支持XPATH解析房室,解析效率高

常用的数据存储库、爬虫框架

		7. pymysql库
		8. pymongo库
		9. Scrapy爬虫框架
	   + 爬取网站数据
	   + 提取结构数据

## 3 .HTML CSS JS

![image-20221103194823744](py-lea.assets/image-20221103194823744.png)

### Tag标签

- `<head>`:存放网页得元信息,不显示在网页中
- `<body>`存放网页得具体内容

```html
<html>

<head>
<title> 我的第一个HTML文件</title>

<body>
<p>元素得内容显示</p>
</body>
</head>
```

- 标题:`<h1>~<h6>`
- 段落:`<p>`
- 链接:`<a>` `<a href=http://baidu.com/>`
- 图片:`<img>` `<img src="logo.png"/>`	



<img src="py-lea.assets/image-20221103200509937.png" alt="image-20221103200509937" style="zoom:50%;" />

## 4. HTTP得请求和响应

<img src="py-lea.assets/image-20221103200705648.png" alt="image-20221103200705648" style="zoom:33%;" />

![image-20221103200846462](py-lea.assets/image-20221103200846462.png)

1. Get请求:从指定得资源请求数据(从服务器获得数据)

   + 不带参数得Get请求:Http:www.baidu.com
   + 带参数得Get请求: http://baidu.com/s?wd=python (参数(key=value格式),多个参数之间使用&连接)

2. Post请求:向置顶得资源请求数据(向服务器上传递数据)

   ![image-20221103201335629](py-lea.assets/image-20221103201335629.png)

+ 响应报文
  + 状态行(response line),响应头部(request header),响应正文3部分组成
  + 状态码(status-code):200(成功),404,403...



## Requests库获取网页源代码

+  `request.get() `    获取网页的数据

  > + Get请求(不带参数):
  >
  >   `request.get('http://www.baidu.com')`
  >
  > + Get请求(带参数):
  >
  >   `request.get('http://www.baidu.com',params={'key1':'value1'})`

+ `request.post()`向网页提交POST请求

  >  ```python
  > data = {
  > 'key1':'value1',
  > 'key2':'value2',
  > 'arr':['one','two']
  > }
  > requests.post('https://www.baidu.com',data=data)
  >  ```

+ Get请求中使用params接收参数,Post请求中使用data接收参数

+ Get请求或Post请求都是可以携带参数,参数通常写成字典的形式

 ```python
import requests
# 1. 无参数的get请求
response=requests.get('http://www.baidu.com/')
response.raise_for_status()
response.encoding=response.apparent_encoding
print(response.text)
#2. 有参数的get请求
url = 'http://www.baidu.com/s'
response = requests.get(url,params={'wd':'python'})
response.raise_for_status()
response.encoding=response.apparent_encoding
file = open('test.html','w',encoding='utf-8')
file.write(response.text)
file.close()
#3. Post请求
data = {'dxy':'python','key2':'value2'}
post = requests.post('http://httpbin.org/post', data=data)
post.raise_for_status()
post.encoding=post.apparent_encoding
file = open('test1.html','w',encoding='utf-8')
file.write(post.text)
file.close()

 ```

![image-20221103230713307](py-lea.assets/image-20221103230713307.png)



### Selenium模拟浏览器操作

![image-20221103233156363](py-lea.assets/image-20221103233156363.png)

![image-20221103233405906](py-lea.assets/image-20221103233405906.png)

<img src="py-lea.assets/image-20221103233505391.png" alt="image-20221103233505391" style="zoom:67%;" />

+ 等待页面加载

  > 使用前导入:	`form selenium.webdriveer.support.ui import WenDriverWait`
  >
  > 创建brower时,设置全局元素等待超时的时间(隐式等待)
  >
  > ```python
  > browser = webdriver.Chrome()
  > browser.implicitly_wait(10)# 表示查找元素时超时时间是10s
  > element = browser.find_element(By.ID,'kw')
  > ```

+ 模拟鼠标操作

  使用webDriver提供的ActionChains类模拟鼠标事件

  - 导入ActionChains类:`from selenium.webdriver import ActionChains`
  - 调用ActionChains()类,将浏览器驱动brower传入:`chains=ActionChains(browser)`

  ActionChains提供的鼠标操作方法:

  - 左击:`chains.click(elem)`
  - 右击:`chains.context_click(elem)`
  - 双击:`chains.double_click(elem)`
  - 鼠标悬停:`chains.move_to_element(elem)`

执行操作:`perform()`,调用其他操作后,都要再次调用这个方法,表示鼠标某个操作

```python
from selenium import webdriver
from selenium.webdriver import ActionChains
browser = webdriver.Chrom()
chains = ActionChains(browser)
browser.get('...')
elem = browser.find_element(By.LINK_TEXT,'...')
chains.click(elem).perform()
```

+ 使用键盘操作

  - 借助key模块

    form selenium.webdriver.common.keys import Keys

  - 常见的键盘操作

    - `element.sendkeys('Python')`

    - `element.sendkeys('Kets.Back_SPACE')`

    - `element.sendkeys('Keys.CONTROL,'c')`

    - `element.clear()`

      ![image-20221104092137613](py-lea.assets/image-20221104092137613.png)

+ 模拟下拉栏操作

  `from selenium.webdriver.support.select import Select`

  - 返回所有选项

    ```python
    pro = Select(browser.find_element(By.ID,'pro'))
    for opt in pro.options:
    	...
    ```

  - (取消)选中某一个选项

    - 通过value属性选中或取消选中:

      `pro.select_by_value("bj")`,`pro.deselect_by_value("bj")`

    - 通过index索引选中或取消选中:

      `pro.select_by_index(0)`,`pro.deselect_by_index(0)`

    - 通过标签文字

      `pro.select_by_visable_text("广东")` ,`pro.deselect_by_visable_text("广东")`

+ 返回所有选项

  `pro=Select(boreser.find_element(By.ID,'pro))`

  `for option in pro.options:...`

+ (取消)选中某一个选项

  + 通过value属性选中或取消选中

    `pro.select_by_value('bj')`  ---`pro.deselect_by_value('bj')`

  + 通过index索引选中或取消选中

    `pro.select_by_index(0)`-----`pro.deselect_by_index(0)`

  + 通过标签文字选中或取消选中

    `pro.select_by_visible_text('广东')`------`pro.deselect_by_visiable_text('广东')`

+ 整个网页截图保存

  `browser.get_screenshot_as_file('./xxx.png')`

+ 指定元素截图并保存:

  ```python
  #找到目标元素
  elem = browser.find_elem(By.ID,'kw')
  #截图获取搜索框元素
  elem.screenshot('kw.png')
  ```

+ 关闭浏览器

  `browser.close()`

+ 关闭所有窗口

  `browser.quit()`

## 提取信息

### 1. 正则表达式

![image-20221107094825326](py-lea.assets/image-20221107094825326.png)

```python
response = requests.get('http://www.baidu.com/')
response.raise_for_status()
response.encoding = response.apparent_encoding
title = re.findall(r'<title>(.*?)</title>', response.text)
print(title[0])

## 结果：百度一下，你就知道
```

### 3. Beautiful Soup

![image-20221107095909268](py-lea.assets/image-20221107095909268.png)

+ 利用Beautiful Soup解析：

  - 适用前导入：`from bs4 import BeautifulSoup`

  - 常见解析流程：

    - **Step1**：获取某个网页的HTML代码，如Request、Selenium

      ```python
      response = request.get('http://baidu.com')
      html = response.text
      ```

    - **Step2**：利用Beautiful Soup解析获得的html代码

      ```python
      soup = BeautifulSoup(html,'html.parser')
      print(soup.prettify())
      ```

       ![image-20221107105204204](py-lea.assets/image-20221107105204204.png)

  - 在BeautifulSoup中搜索单一对象

    - soup.tag_name()：只能获取当前标签下的第一个标签

      - soup.head：匹配`<head><title>The Dormouse's story</title></head>`
      - soup.title：匹配`<title>The Dormouse's story</title>`

    - soup.find('tag_name')：用于查找符合查询条件的第一个标签节点

      - `soup.find('head')`，与`soup.head`同效果，soup.find('title')与soup.title同效果

      - `soup.find('p',attrs{'class':'story'})`

        ![image-20221107110947187](py-lea.assets/image-20221107110947187.png)

    - soup.find_all('tag_name')：查找所有符合田间的标签节点，返回一个列表

      - `soup.find_all('titlr')`：匹配`[<title>The Dormouse's story</title>]`

      - `soup.find_all('a')`：匹配

        `[<a> class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]`
    
    ![image-20221115221251040](py-lea.assets/image-20221115221251040.png)

### xPath库



- 使用时先导入：`from lxml import etree`

- 使用etree对获取的网页源代码进行解析`data = etree.HTML(response.text)`
- 利用XPATH获取指定元素：`elem = data.xpath('元素的XPAT和路径')`

<img src="py-lea.assets/image-20221115221712634.png" alt="image-20221115221712634" style="zoom:50%;" />![image-20221115222237984](py-lea.assets/image-20221115222237984.png)

<img src="py-lea.assets/image-20221115222323148.png" alt="image-20221115222323148" style="zoom:50%;" />

<img src="py-lea.assets/image-20221115222457683.png" alt="image-20221115222457683" style="zoom:50%;" />

- `/html`：匹配html节点

- `/html/head`：匹配html节点下的head节点

- `/html/body/p/b`等价于`//b`

- //：从匹配选择的当前节点选择文档中的节点，而不考虑他们的位置

  - `//*`可以查找所有的节点
  - `//body//a`：匹配body的后代节点种的a节点

- @：获取属性 使用@属性获取某个节点中的属性值：`节点的位置XPATH    /@属性`

  - //a/@href:
    - 匹配`['http://example.com/elsie','http://example.com/lacie','http://example.com/tillie']`
  - `//a/@class`：匹配`['sister','sister','sister']`

- text()：实现文本获取：节点的位置的XPATH   `\text()`

  - `//a[@href='http://example.com/elsie']/text()`：匹配elsie 
  - `//body/text()`：匹配`[''\n','\n\n','\n\n']`。只得到第一层内容
  - `//body//text()`遍历节点中所有的文本内容

  ```python
  a3 = data.xpath('//a[@href="http://example.com/tillie"]/text()')
  print(a3)
  a2_href = data.xpath("//a[@id='link2']/@href")
  print(a2_href)
  
  ```

  

<img src="py-lea.assets/image-20221116134005284.png" alt="image-20221116134005284" style="zoom:67%;" />



## 4. 框架与反爬虫机制

### 1. Scrapy框架

<img src="py-lea.assets/image-20221116142041317.png" alt="image-20221116142041317" style="zoom:50%;" />

- Scrapy安装:conda install -c conda-forge scrapy
- Scrapy的使用:
  - 创建爬虫项目:`scrapy startproject mySpider`
  - 定义需要抓取的数据(items.py)文件
  - 编写提取数据的爬虫(在Spider文件夹内)
  - 执行爬虫并保存数据:`scrapy crawl mySpider -o items.json`

![image-20221116143124625](py-lea.assets/image-20221116143124625.png)

### 2. 反爬虫

- 限制爬虫程序访问服务器资源和获取数据的行为称为反爬虫，常见反爬虫操作：
  - **User-Agent 请求头验证**：服务器端校验请求头中User-Agent值来区分正常用户和爬虫程序
  - **IP地址验证/限制访问频率**：如果单个IP访问超过阔值或访问频率过快，予以封锁
  - **图形验证码**：当系统怀疑当前的请求是来自于机器人或者爬虫之时，将弹出验证码对话框，要求用户填入正确的验证码，方可正常访问

### 3. 应对方法

1. 基于`user-agent`请求头的反爬虫

   + 浏览器在发送请求的时候，会附带一部分浏览器及当前系统环境参数

   + 反爬策略:

     + 将要请求的User-Agent值伪装成一般用户登录网站时使用的User-Agent值
     + 使用selenium模拟使用浏览器

   + 随机生成`user-Agent`添加到header中

     - 借助fask_useragent库:`pip install fake-useragent`
     - 使用前导入:`form fake_useragent import UserAgent`

   + 使用fake_useragent库随机生成User_Agent:

     ```python
     import requests
     form fake_useragent import UserAgent
     header={'useragent':UserAgent().random}
     response = request.get('http://baidu.com',headers=header)
     ```

2. 基于IP/限制访问频率的反爬虫

   + 反爬策略

     - 使用IP代理池
     - 降低访问频率

   + 降低访问频率:

     + 每次访问后设置等待时间

     + 使用`times.sleep()`实现请求间隔

       ```python
       import time
       import random
       time.sleep(random.randint(1.9))
       ```

   + 设置代理访问

     ```python
     proxie = {
       'http': 'http://175.42.129.xxx:9999'
       'http': 'http://175.44.108.xxx:9999'
       ...
     }
     response = request.get(url,proxies=proxies)
     ```

   + 基于图形验证码的反爬虫

     反爬策略

     + 下载或截图验证码，使用图像识别程序进行自动识别使用

     + Selenium实现鼠标的按下、拖动、释放等行为

     + 利用pytesseract识别验证码:对于没有斜线、噪点等干扰元素的验证码，可以用pytesseract库进行识别.Python-tesseract是-个基于google's Tesseract-OCR的独立封装包

       * 先安装Tesseract-OCR并配置环境变量

       * 然后安装 pip install pytesseract

       * 先下载或截图验证码,再识别验证码

         ```python
         import pytesseract
         from PIL import Image
         image = Image.open('./code.png')
         code = pytesseract.image_to_string(image)
         ```

### 4. 小结

![image-20221116145647957](py-lea.assets/image-20221116145647957.png)

## 爬虫数据

+ 三个重要的结构:获取网页内容$\rightarrow$网页解析内容$\rightarrow$保存数据

  按一定的规则,在网页源代码(HTML)提取需要的内容

+ 请求与内容抓取

  - HTTP请求Get请求(带参数,不带参数),post请求
  - Requests库:requests.get(),requests.post()
  - Selenium:驱动浏览器,模拟人类的浏览器操作(访问网页,定位元素,操作元素,关闭浏览器)

+ 解析信息提取

  - BeautifulSoup库:`soup.title`,`soup.find('title')`,`soup.find_all('a',attrs={...})`
  - XPATH库,/,//,nodename,[@attrib='value'],.,..,@attrib,text()

**简单的使用Beautiful,网页复杂多使用XPATH**

![image-20221123163106555](py-lea.assets/image-20221123163106555.png)

 ![image-20221123163424861](py-lea.assets/image-20221123163424861.png)

![image-20221123164522578](py-lea.assets/image-20221123164522578.png)

![image-20221123171425230](py-lea.assets/image-20221123171425230.png)

![image-20221123171556466](py-lea.assets/image-20221123171556466.png)

![image-20221123171821629](py-lea.assets/image-20221123171821629.png)

![image-20221123171903718](py-lea.assets/image-20221123171903718.png)

![image-20221123193707833](py-lea.assets/image-20221123193707833.png)



## 附录

### 从Pubmed上面爬取论文题目,作者,摘要,DOI

```python
# 从Pubmed上面爬取论文题目,作者,摘要,DOI
# 关键词lung cancer
# 爬取前5页的论文信息
# 题目h1下面的a标签
# 作者 class为authors-list的div标签
# 摘要 class为abstract-content selected的div标签
# DOI class为id-link的a标签
from urllib import response
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import pandas as pd

paper_data = pd.DataFrame(columns=['title','authors','doi',"abstract"])

url = 'https://pubmed.ncbi.nlm.nih.gov/'
kw = 'lung cancer'
fmt = 'abstract'
for num in range(1,6):
    response = requests.get(url,
                params={'term':kw,
                        'page':str(num),
                        'format':fmt},
                headers={"User-Agent":UserAgent().random})
    response.raise_for_status() #防止没正确解析出现错误运行
    response.encoding = response.apparent_encoding # 防止乱码

    # print(response.url)
    soup = BeautifulSoup(response.text,'html.parser')

    paper_list = soup.find_all('div',attrs={"class":"results-article"})
    
    title = []

    paper_record = {}
    for paper in paper_list:
        article = paper.article
        titles = article.h1.a.strings
        # strip函数用于删除头尾的空白符,包括\n\t等
        for s in titles:
            title.append(s.strip())
        # print(''.join(title))
        paper_record['title'] = ''.join(title)
        
        ## find author
        authors= []
        if article.find('em',attrs={"class":"empty-authors"}):
            authors.append('No author listed')
        else:
            author_list = article.find_all('a',attrs={'class':'full-name'})
            for author in author_list:
                authors.append(author.string.strip())
        # print(','.join(authors))
        paper_record['authors'] = ''.join(authors)

        # 获取DOI信息
        doi = article.find('span',attrs={"class":"citation-doi"})
        if doi is None:
            paper_record['doi'] = 'No doi'
        #     print(doi)
        else:
        #     print(doi.string.strip())
            paper_record['doi'] = doi.string.strip()

        # 获取摘要信息
        abstract = []
        if article.find_all("em",attrs={"class":"empty-abstract"}):
            print("No abstract")
        else:
            content = article.find("div",attrs={"class":"abstract-content selected"})
            abstracts = content.find_all('p')

            for item in abstracts:
                for sub_content in item.strings:
                    abstract.append(sub_content.strip())
            # print('\n'.join(abstract))
            paper_record['abstract'] = ''.join(abstract)
        paper_data = paper_data.append(paper_record,ignore_index=True)

paper_data.to_excel('./paper.xlsx',index=False)

```

### 从ScienceDrict中选择某个子领域



选题背景与意义



















纸币识别:

+ 面值,几块钱的多少张,计算总价值

