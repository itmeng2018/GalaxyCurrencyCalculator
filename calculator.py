from GalaxyCurrencyCalculator.config import *


class Calculator(object):
    """计算器类"""

    def __init__(self):
        self.word_dic = dict()  # 存储单词查询罗马字符的字典
        self.metal_dic = dict()  # 存储金属查询数量和价钱的字典
        self.output = []  # 存储待输出语句

    @staticmethod
    def roman_to_number(roman_numeral):
        """
        罗马字符转换成十进制数字
        roman_numeral: 罗马数字(str)  "XLII"
        :return: 转换后的十进制数字(int)  42
        """
        if not legal.search(roman_numeral):  # 检测罗马数字是否符合规定
            return print('"%s" is not a valid Roman numerals' % roman_numeral)
        i = 0  # 角标
        number_sum = 0  # 记录结果值
        while i < len(roman_numeral):
            if len(roman_numeral) - 1 == i:  # 处理最后一个元素
                number_sum += base_number[roman_numeral[i]]
                break

            elif base_number[roman_numeral[i]] < base_number[roman_numeral[i + 1]]:  # 后位大于前位
                number_sum += base_number[roman_numeral[i + 1]] - base_number[roman_numeral[i]]
                i += 2  # 跳过后位数的循环

            else:  # 前位大于后位
                number_sum += base_number[roman_numeral[i]]
                i += 1

        return number_sum

    def word_to_roman(self, words):
        """
        把单词语句转换成罗马数字
        :param words: 单词语句(string)  "pish tegj glob glob"
        :return: 转换后的罗马数字(string)   "XLII"
        """
        return ''.join([self.word_dic[word] for word in words.split(' ')])

    def define_word(self, item):
        # 处理语句: 定义单词
        self.word_dic[item[0]] = item[1]  # {单词: 罗马字符}

    def define_metal(self, item):
        # 处理语句: 定义金属
        much = self.roman_to_number(self.word_to_roman(item[0]))
        self.metal_dic[item[1]] = (much, int(item[2]))  # {金属: (数量, 总价)}

    def query_word(self, item):
        # 处理语句: 查询单词的值
        roman_numeral = self.word_to_roman(item)  # 罗马字符
        self.output.append(query_word_string.format(words=item, number=self.roman_to_number(roman_numeral)))

    def query_metal(self, item):
        # 处理语句: 查询金属的值
        new_much = self.roman_to_number(self.word_to_roman(item[0]))  # 提取询问的新数量
        much, price = self.metal_dic[item[1]]  # 定义的原数量和总价
        new_price = price * new_much / much  # 计算新数量的总价
        self.output.append(query_metal_string.format(words=item[0], metal=item[1], number=new_price))

    def text_categorization(self, lines):
        """
        文本分类处理
        :param lines: 行语句列表
        :return:
        """
        # lines = text.splitlines()

        for line in lines:
            if define_word.findall(line):  # 定义单词的值
                self.define_word(define_word.findall(line)[0])

            elif define_metal.findall(line):  # 定义金属的价格
                self.define_metal(define_metal.findall(line)[0])

            elif query_word.findall(line):  # 问组合单词的值
                self.query_word(query_word.findall(line)[0])

            elif query_metal.findall(line):  # 问金属的价格
                self.query_metal(query_metal.findall(line)[0])

            else:
                return '"%s" Not a legal statement' % line


def main(input_text_path):
    """主方法, 对象调用"""
    cal = Calculator()  # 实例化
    # 读取输入文件
    with open(input_text_path, 'r', encoding='utf-8') as fp:
        cal.text_categorization(fp.readlines())  # 调用文本分类处理器

    return '\n'.join(cal.output)  # 返回输出结果
