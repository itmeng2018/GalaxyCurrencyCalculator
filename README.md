## 程序运行说明

1. 新建文本文档, 按行写入待转换内容

   例如: 在`/user/itmeng/Desktop/`下新建文件`input_20190227.txt`, 输入一下内容

   ```
   glob is I
   prok is V
   pish is X
   tegj is L
   glob glob Silver is 34 Credits
   glob prok Gold is 57800 Credits
   pish pish Iron is 3910 Credits
   how much is pish tegj glob glob ?
   how many Credits is glob prok Silver ?
   how many Credits is glob prok Gold ?
   how many Credits is glob prok Iron ?
   ```

2. 在项目目录下新建一个python文件, 调用项目目录下`calculator.py`中的`main`方法, 传入input文件路径

   例如: 新建文件`transfre.py`文件, 写入一下内容:

   ```python
   from GalaxyCurrencyCalculator import calculator
   output = calculator.main('/user/itmeng/Desktop/input_20190227.txt')
   print(output)
   ```

   

## 笔试题说明文档

### 一. 环境:

MacOS 10.14 + Python3.7 + VS code

### 二. 题目:

**Description**：
You decided to give up on earth after the latest financial collapse left 99.99% of the earth's population with 0.01% of the wealth. Luckily, with the scant sum of money that is left in your account, you are able to afford to rent a spaceship, leave earth, and fly all over the galaxy to sell common metals and dirt (which apparently is worth a lot).

Buying and selling over the galaxy requires you to convert numbers and units, and you decided to write a program to help you. The numbers used for intergalactic transactions follows similar convention to the roman numerals and you have painstakingly collected the appropriate translation between them.

Numbers are formed by combining symbols together and adding the values. For example, MMVI is 1000 + 1000 + 5 + 1 = 2006. Generally, symbols are placed in order of value, starting with the largest values. When smaller values precede larger values, the smaller values are subtracted from the larger values, and the result is added to the total. For example MCMXLIV = 1000 + (1000 − 100) + (50 − 10) + (5 − 1) = 1944.

The symbols "I", "X", "C", and "M" can be repeated three times in succession, but no more. (They may appear four times if the third and fourth are separated by a smaller value, such as XXXIX.) "D", "L", and "V" can never be repeated. "I" can be subtracted from "V" and "X" only. "X" can be subtracted from "L" and "C" only. "C" can be subtracted from "D" and "M" only. "V", "L", and "D" can never be subtracted. Only one small-value symbol may be subtracted from any large-value symbol. A number written in Arabic numerals can be broken into digits. For example, 1903 is composed of 1, 9, 0, and 3. To write the Roman numeral, each of the non-zero digits should be treated separately. In the above example, 1,000 = M, 900 = CM, and 3 = III. Therefore, 1903 = MCMIII.

Input to your program consists of lines of text detailing your notes on the conversion between intergalactic units and roman numerals.
You are expected to handle invalid queries appropriately.

### 三. 题意: 

**描述**

数字是由遵循了罗马数字的符号组合在一起和将值加在一起构成的, 例如: MMVI = 1000 + 1000 + 5 + 1 = 2006

符号是从最大值开始按照数值排序, 当比较小的值和比较大的值相对应的时候，比较小的值是从比较大的值中获取的，并且结果被添加到总数中。例如 MCMXLIV = 1000 + (1000 - 100) + (50 - 10) + (5 - 1) = 1944.

“I”，“X”，“C”和“M”这些符号最多可以连续出现三次,   “D”、“L”和“V”永远不能重复。

“I”只能组合“V”和“X”。“X”只能组合“L”和“C”。“C”只能组合“D”和“M”。

任何大值的符号中只能得到一个小值的符号。

用阿拉伯数字写的一个数字可以分解。比如1903是由1,9,0,和3组成。要写罗马数的话，每个非零的数字都应该分开对待。在上边的例子中，1,000= M,900= CM, 3 = lll。所以1903 = MCMII。

### 四. 分析: 

##### 业务需求: 

​	把**罗马数字**转换成**十进制数字**的程序, `Calculator`

##### 规则分析:

| 罗马数字 | 十进制数字 |    次数限制     | 后位数组合限制 |
| :------: | :--------: | :-------------: | :------------: |
|    I     |     1      | 连续重复不大于3 |     IV, IX     |
|    V     |     5      |        1        |    不可倒序    |
|    X     |     10     | 连续重复不大于3 |     XL, XC     |
|    L     |     50     |        1        |    不可倒序    |
|    C     |    100     | 连续重复不大于3 |     CD, CM     |
|    D     |    500     |        1        |    不可倒序    |
|    M     |    1000    | 连续重复不大于3 |    任意组合    |

合法判断正则表达式:

```python
r'^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
```

##### 测试数据分析:  

- INPUT

  ```
  glob is I
  prok is V
  pish is X
  tegj is L
  glob glob Silver is 34 Credits		// II silver = 34	2银 = 34
  glob prok Gold is 57800 Credits		// IV Gold = 57800	4金 = 57800
  pish pish Iron is 3910 Credits		// XX Iron = 3910	20铁 = 3910
  how much is pish tegj glob glob ?	// XLII 是多少?	42
  how many Credits is glob prok Silver ?	// IV银是多少?		68
  how many Credits is glob prok Gold ?	// IV金是多少?		57800
  how many Credits is glob prok Iron ?	// IV铁是多少?		782
  ```

  

- OUTPUT

  ```
  pish tegj glob glob is 42
  glob prok Silver is 68 Credits
  glob prok Gold is 57800 Credits
  glob prok Iron is 782 Credits
  ```

  

- 分析点: 

  > 1. word `is` V   表示定义条件 word = V = 5
  >
  >    ```python
  >    r'(\w+) is ([IVXLCDM])$'		# 正则匹配
  >    ```
  >
  > 2. much Gold `is` many `Credits`  定义多少金需要多少钱
  >
  >    ```python
  >    r'(.*?) (Silver|Gold|Iron) is (\d+) Credits'	# 正则匹配
  >    ```
  >
  > 3. `how much is` word ?  表示询问word的值是多少
  >
  >    ```python
  >    r'(.*?) (Silver|Gold|Iron) is (\d+) Credits'	# 正则匹配
  >    ```
  >
  > 4. `how many Credits` word Gold ?  表示询问5金需要多少钱
  >
  >    ```python
  >    r'^how many Credits is (.*?) (Silver|Gold|Iron)\s?\?$'	 # 正则匹配
  >    ```

### 五. 开发思路

##### 1. 配置文件`config.py`

考虑程序的可扩展性和重构性, 将变动需求提取

```python
import re

# 罗马数字库
base_number = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

# 判断罗马字符是否合法
legal = re.compile(r'^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$')

# 对输入的判断
define_word = re.compile(r'(\w+) is ([IVXLCDM])$')  # 定义单词的值
define_metal = re.compile(r'(.*?) (Silver|Gold|Iron) is (\d+) Credits')  # 定义金属的值
query_word = re.compile(r'^how much is (.*?)\s?\?$')  # 查询组合单词的值
query_metal = re.compile(r'^how many Credits is (.*?) (Silver|Gold|Iron)\s?\?$')  # 查询金属的值

# 输出语句模板
query_word_string = '{words} is {number}'
query_metal_string = '{words} {metal} is {number:.0f} Credits'
```

##### 2. 程序主逻辑`caculator.py`

- 定义`Calculator`类, 初始化以下实例属性:

  |   属性    |             说明             |
  | :-------: | :--------------------------: |
  | word_dic  |  存储单词查询罗马字符的字典  |
  | metal_dic | 存储金属查询数量和价钱的字典 |
  |  output   |        存储待输出语句        |

  

- 定义静态方法`roman_to_number`, 作用把转换好的罗马字符换算成十进制数字, 比如`XLII`转换成`42`

- 定义实例方法:

  |      实例方法       |                            说明                            |
  | :-----------------: | :--------------------------------------------------------: |
  |    word_to_roman    |                  把单词语句转换成罗马数字                  |
  |     define_word     | 处理语句: 定义单词, 把单词和对应的罗马数字存储到`word_dic` |
  |    define_metal     |  处理语句: 定义金属, 把金属和对应的价钱存储到`metal_dic`   |
  |     query_word      |                   处理语句: 查询单词的值                   |
  |     query_metal     |                   处理语句: 查询金属的值                   |
  | text_categorization |       文本解析分类, 对应的语句调用对应的语句处理方法       |

##### 3. 定义调用主方法`main`

- 实例化`Calculator`对象
- 调用文本解析分类方法
- 返回输出结果

### 六. 测试

- 测试文件`calculator_test.py` : 使用assert判断 `原例输出结果` 和 `测试输出结果`, 输出测试日志
- 测试输入内容文件: `test_input.txt`
- 原例输出结果文件: `correct_result.txt`
- 测试日志: `test.log`
- 测试结果: 原例OK
