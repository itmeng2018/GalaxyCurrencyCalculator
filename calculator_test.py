from datetime import datetime
from GalaxyCurrencyCalculator import calculator

test_input_path = 'test_input.txt'

with open('correct_result.txt', 'r', encoding='utf-8') as fp:
    correct_result = fp.read()

with open('test_input.txt', 'r', encoding='utf-8') as fp:
    test_input_text = fp.read()

test_result = calculator.main(test_input_path)

try:
    assert test_result == correct_result
    test_conclusion = 'calculator is ok'
except AssertionError:
    test_conclusion = 'calculator not ok'

log_temp = """测试时间: [{}]\n\n测试对象: calculator
\n原例输入: \n{}\n
原例输出: \n{}\n
测试输入: \n{}\n
测试输出: \n{}\n
测试结果: \n{}\n
"""
log = open('test.log', 'w', encoding='utf-8')
log.write(log_temp.format(
    datetime.now(),
    test_input_text,
    correct_result,
    test_input_text,
    test_result,
    test_conclusion
))
log.close()
