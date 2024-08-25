# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 21:33:33 2024

@author: Dell
"""

a = int(input("nhập giờ: "))
b = int(input("nhập phút: "))
c = int(input("nhập giây: "))
tg = a*3600 + b*60 + c
print("tổng số giây là: ", tg)