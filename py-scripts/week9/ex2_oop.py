#!/usr/bin/env python

import re


def find_uptime_field(a_pattern, uptime_str):
    '''
    If there is a match return the match group(1)
    Else return 0
    '''

    a_check = re.search(a_pattern, uptime_str)
    if a_check:
        return int(a_check.group(1))
    else:
        return 0


class Uptime(object):
    def __init__(self, str_1):
        self.str_1 = str_1
        print self.str_1

    def uptime_seconds(self):
        total_sec = 0
        list_str = self.str_1.split(',')
        (trash, time) = list_str[0].split('uptime is ')
        list_str[0] = time
        for t in list_str:
            if 'minutes' in t:
                min = int(t.split(' ')[1])
                total_sec += min * 60
            if 'hours' in t:
                hour = int(t.split(' ')[1])
                total_sec += hour * 60 * 60
            if 'days' in t:
                day = int(t.split(' ')[1])
                total_sec += day * 60 * 60 * 24
            if 'weeks' in t:
                week = int(t.split(' ')[0])
                total_sec += week * 60 * 60 * 24 * 7
            if 'years' in t:
                year = int(t.split(' ')[0])
                total_sec += year * 60 * 60 * 24 * 365

        return total_sec


test = Uptime('twb-sf-881 uptime is 6 weeks, 4 days, 2 hours, 25 minutes')

