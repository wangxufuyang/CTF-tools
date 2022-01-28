# coding:utf-8
import binascii


# 这放写16进制
s = ''
out = open('2.jpg','wb')
out.wirte(binascii.unhexlify(s))
out.close()
