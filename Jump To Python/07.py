# import re

import re


data = """
park 800905-1049118
kim  700905-1059119
"""

'''result = []
for line in data.split("\n"):
    word_result = []
    for word in line.split(" "):
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word = word[:6] + "-" + "*******"
        word_result.append(word)
    result.append(" ".join(word_result))
print("\n".join(result))'''

'''pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******", data))'''
# p = re.compile('ab*')
# import re
# p = re.compile('[a-z]+')
# m = p.match("python")
# print(m)
# m = p.match("3 python")
# print(m)
# m = p.search("python")
# print(m)
# m = p.search("3 python")
# print(m)
# result = p.findall("life is too short")
# print(result)
# result = p.finditer("life is too short")
# print(result)
# for r in result: print(r)
# m = p.search("3 python")
# print(m.group())
# print(m.start())
# print(m.end())
# print(m.span())

# import re
# p = re.compile('[a-z]+')
# m = p.match("python")

# m = re.match('[a-z]+', "python")

# import re
# p = re.compile('a.b')
# m = p.match('a\nb')
# print(m)

# p = re.compile('a.b', re.DOTALL)
# m = p.match('a\nb')
# print(m)

# p = re.compile('[a-z]+', re.I)
# print(p.match('python'))
# print(p.match('Python'))
# print(p.match('PYTHON'))

# import re
# p = re.compile("^python\s\w+", re.MULTILINE)

# data = """python one
# life is too short
# python two
# you need python
# python three"""

# print(p.findall(data))

# import re
# charref = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')
# charref = re.compile(r"""
# &[#]
# (
#     0[0-7]+
#     | [0-9]+
#     |x[0-9a-fA-F]+
# )
# ;
# """, re.VERBOSE)
# import re
# p = re.compile('\\\\section')
# p = re.compile(r'\\section')

# import re
# p = re.compile(r'\Bclass\B')
# print(p.search('no class at all'))
# print(p.search('the declassified algorithm'))
# print(p.search('one subclass is'))

# p = re.compile('(ABC)+')
# m = p.search('ABCABCABC OK?')
# print(m)
# print(m.group())
# p = re.compile(r"(\w+)\s+((\d+)[-]\d+[-]\d+)")
# m = p.search("park 010-1234-1234")
# print(m.group(3))
# p = re.compile(r'(\b\w+)\s+\1')
# print(p.search('Paris in the the spring').group())
# p = re.compile(r"(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)")
# m = p.search("park 010-1234-1234")
# print(m.group("name"))
# p = re.compile(r'(?P<word>\b\w+)\s+(?P=word)')
# print(p.search('Paris in the the spring').group())
# p = re.compile(".+(?=:)")
# m = p.search("http://google.com")
# print(m.group())
# p = re.compile(".*[.](?!bat$|exe$).*$")
# p = re.compile('(blue|white|red)')
# print(p.sub('colour', 'blue socks and red shoes', count=1))
# print(p.subn('colour', 'blue socks and red shoes', count=1))
# p = re.compile(r"(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)")
# print(p.sub("\g<phone> \g<name>", "park 010-1234-1234"))
import re
# def hexrep1(match):
#     value = int(match.group())
#     return hex(value)

# p = re.compile(r'\d+')
# print(p.sub(hexrep1, 'Call 65490 for printing, 49152 for user code.'))
s = '<html><head><title>Title</title>'
print(len(s))
print(re.match('<.*>', s).span())
print(re.match('<.*?>', s).group())