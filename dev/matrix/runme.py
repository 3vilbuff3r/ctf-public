#!/usr/bin/python3
import numpy
def build_matrix(size):
    zeros = ['0' for i in range(size // 10)]
    ones = ['1' for i in range(size // 10)]
    spaces = [' ' for i in range(size - len(zeros) - len(ones))]
    total = zeros + ones + spaces
    numpy.random.shuffle(total)
    return ''.join(total)

# Keep times between 100 to 500 
times = 300
matrix = build_matrix(5000)
flag = "m365{needle_1n_hayst4ck}"
while True:
    if times == 0:
        print(flag, end='')
    print(matrix, end='')
    times -= 1