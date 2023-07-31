import re

#.除换行符以外的所有字符
def test1():
    text=re.findall("a.b","a?b abx atb")
    print(text) #['a?b', 'atb']

def test1():
    text=re.findall("a.b","a?b abx atb")
    print(text) 



if __name__ == '__main__':
    test1()
