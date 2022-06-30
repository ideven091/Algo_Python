import re

reg = r'm\w\w'

prog = re.compile(reg)
str = 'cat mat bat rat'
result = prog.search(str)
print(result.group())

str1 = 'This: is the: "Core" Python\'s blockChain_python_code'
print(re.split(r'\W+',str1))