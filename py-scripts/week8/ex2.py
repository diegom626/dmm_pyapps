#!/usr/bin/env python
import show_version


model = show_version.show_model('show_version')
os_version = show_version.show_os_version('show_version')
uptime = show_version.show_uptime('show_version')

print 'model: %10s\nos_version: %10s\nuptime: %10s' % (model, os_version, uptime)
