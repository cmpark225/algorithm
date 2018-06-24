# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = input()
k=input()

import ast
from collections import deque
metrix = ast.literal_eval(user_input)
size = len(metrix)

first_values =[]
last_values = []
for item in metrix[1:-1]:
		first_values.append(item[0])
		last_values.append(item[-1])

rotate_line = deque(metrix[0])
rotate_line += last_values
rotate_line += metrix[-1][::-1] 
rotate_line += first_values[::-1]

rotate_line.rotate(int(k))

offset = int((len(rotate_line)-(size*2))/2)

rotate_result = list(rotate_line)

last_values = rotate_result[size:size+offset]
first_values = rotate_result[::-1][:offset]
last_line = rotate_result[size+offset:-offset]

result = []
result.append(rotate_result[:size])

index = 0
for item in metrix[1:-1]:
				tmp = [first_values[index]]
				tmp += item[1:-1]
				tmp.append(last_values[index])
				result.append(tmp)
				index += 1

result.append(last_line[::-1])

print (str(result).replace(' ', ''))



