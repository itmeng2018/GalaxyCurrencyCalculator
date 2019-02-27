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
