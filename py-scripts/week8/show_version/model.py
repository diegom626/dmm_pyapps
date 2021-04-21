#!/usr/bin/env python
import re


def show_model(file_):
    f = open('./show_version/%s.txt' % file_, "r")
    file_data = f.read()
    f.close()
    search = re.search(r"Cisco (\d+)(.+) processor", file_data)
    if search:
        return search.group(1)
    else:
        return None
