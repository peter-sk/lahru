#!/usr/bin/env python
import netifaces as ni
for i in ni.interfaces():
    print(i,"-->",ni.ifaddresses(i))

