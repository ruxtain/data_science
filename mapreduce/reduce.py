#!/usr/bin/python3

"""reduce"""

import sys
current_word = None
current_count = 0
word = None

for line in sys.stdin:
    line = line.strip()
    # 解析来自 map 的输出
    word, count = line.split('\t', 1)
    # 处理异常值，个数不是数字的忽略
    try:
        count = int(count)
    except ValueError:
        continue
    # 这里之所以用这种“游标”方式进行处理，下面会详细解释
    if current_word == word:
        current_count += count
    else:
        if current_word:
            print('%s\t%s' % (current_word, current_count))
        current_count = count
        current_word = word
if current_word == word:
    print ('%s\t%s' % (current_word, current_count))
