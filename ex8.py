#!/usr/bin/env python
# -*- coding: utf-8 -*-

string = "Thuật toán chuỗi"
formatter = "{} {} {} {}"

print(formatter.format(string, 1, 2, 3))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
	"Try your",
	"Own text here",
	"Maybe a poem",
	"Or a song about fear."))

u = "Thuật toán"
#uu = u.decode('utf-8')
#s = uu.encode('cp1250')
print (u)