# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

total_count = raw_input()
able_list = raw_input().split()

print sum([int(i) for i in able_list]) - int(total_count) +1
