#!/usr/bin/env python
# encoding: utf-8

import sys

_base_dic = ('8', 'a', 'b', 'c', 'd', 'e',
             'u', 'v', '4', 'w', 'x', 'y', 'z', 'A', 'B', '6', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
             'J', 'K', 'L', 'M', '5', '1', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
             'f', 'g', '9', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', '0', 'p', 'q', 'r', 's', 't', '7',
             'Y', 'Z', '3', '2')


def pwd_encode(key, pwd):
    key_length = len(key)
    str_buffer = []
    for i, item in enumerate(pwd):
        p = ord(item)
        k = ord(key[i%key_length])
        str_buffer.append(_base_dic[p%k%len(_base_dic)])
    return ''.join(str_buffer)



if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise Exception('sys.argv error')
    key = sys.argv[1]
    pwd = sys.argv[2]
    print key, pwd
    print pwd_encode(key, pwd)
