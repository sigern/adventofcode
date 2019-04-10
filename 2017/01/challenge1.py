#!/usr/bin/env python3

def captcha(in_data):
    lenght = len(in_data)
    data  = in_data + in_data[0]
    sum = 0
    for i in range(lenght):
        if data[i] == data[i+1]:
            sum += int(data[i])
    return sum


if __name__ == '__main__':
    file = open("input.txt", "r")
    in_data = file.readline()
    result = captcha(in_data)
    print(result)
    file.close()