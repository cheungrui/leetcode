import os
"""
用途:在题目开头补上若干个0使其开头数字为4个
"""
def countStartnum(s):
    count = 0
    for i in s:
        if i in "1234567890":
            count += 1
        else:
            break
    return count
leetcode_name = os.listdir('.')
for filename in leetcode_name:
    if os.path.isfile('.'+filename):
        if filename[0] in "0123456789":
        count = countStartnum(filename)
            new_name = '0'*(4-count) + filename
            os.rename(filename, new_name)