from collections import OrderedDict

ordinary_dictionary = {}
ordinary_dictionary['a'] = 1
ordinary_dictionary['b'] = 2
ordinary_dictionary['c'] = 3
ordinary_dictionary['d'] = 4
ordinary_dictionary['e'] = 5

print ordinary_dictionary

ordered_dictionary = OrderedDict()
ordered_dictionary['a'] = 1
ordered_dictionary['b'] = 2
ordered_dictionary['c'] = 3
ordered_dictionary['d'] = 4
ordered_dictionary['e'] = 5

print ordered_dictionary
 
d = OrderedDict()
for _ in range(int(raw_input())):
    item, space, quantity = list(raw_input().rpartition(' '))
    d[item] = d.get(item, 0) + int(quantity)
for item, quantity in d.items():
    print item, quantity
			
	