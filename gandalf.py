#!/usr/bin/env python
# encoding: utf-8

import sys

_base_dic = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e',
             'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
             'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
             'Y', 'Z')


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
