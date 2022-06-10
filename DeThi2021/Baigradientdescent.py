import numpy as np

from math import * 
def derivative(x):
    return (exp(2*x) - 4*exp(x))*(4*exp(2*x) - 8*exp(x)) 
def f(x):
    return (exp(2*x) - 4/(exp(-x)))**2 
def GradientDescent(eta, x0):
    x = [x0]
    for i in range(10000):
        x_new = x[-1] - eta*derivative(x[-1]) 
        if abs(derivative(x_new)) < 1e-3:
            break 
        x.append(x_new)
    return x
x = GradientDescent(.001, 1)
print('Giá trị nhỏ nhất của hàm f(x) là: ', f(x[-1]), 'tại x = ', x[-1])

        