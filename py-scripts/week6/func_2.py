#!/usr/bin/env python

list_1 = ["hola", "como", "estas", "astas"]


def to_dic(a_list):
    new_dict = {}
    for i, v in enumerate(a_list):
        new_dict[i] = v
    return new_dict


test_dict = to_dic(list_1)
print
print "List: %s" % str(list_1)
print "Dict: %s" % str(test_dict)
print
