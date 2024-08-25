# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 21:30:42 2024

@author: Dell
"""
N = int(input("Nhập số nguyên dương có hai chữ số: "))
if 10 <= N <= 99:
    tong = (N//10) + (N%10)
    print("Tổng các chữ số của N là: ", tong)