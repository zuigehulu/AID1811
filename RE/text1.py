import re
import sys

def zhaoduankou(duankou):
    string = ''
    s = len(duankou)
    with open('1.txt') as fr:
        for x in fr:
            if duankou == x[0:s]:
                string += x
                for y in fr:       
                    string += y
                    if y[0:1] != ' ':
                        zhengze(string)
                        break
def zhengze(string):
    pattern = 'address is \S*$'
    regex = re.compile(pattern,flags=re.M)
    l = regex.findall(string)
    print(l)

if __name__ == "__main__":
    duankou = sys.argv[1]
    string = zhaoduankou(duankou)
    
    