# 加密 e(x) = (a * x + b) mod m
# 解密 d(x) = a^-1 * (x - b) mod m
# 1/5 * 9 mod 26
# a 和 b 都是质数（素数）
# m = 26字母

# 字典库正向
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', ]
ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']

def Encryption(plaintext, key_1, key_2):
    for i in plaintext:
        if i == ' ':
            print(" ", end='')
        elif i in alphabet:
            index = alphabet.index(i)
            index = (key_1 * index + key_2) % 26
            print(alphabet[int(index)], end='')
        else:
            index = ALPHABET.index(i)
            index = (key_1 * index + key_2) % 26
            print(ALPHABET[int(index)], end='')



def Decrypt(plaintext, key_1, key_2):
    for i in plaintext:
        if i == ' ':
            print(' ', end='')
        elif i in alphabet:
            index = alphabet.index(i)
            index = key_1 * (index - key_2) % 26
            print(alphabet[int(index)], end='')
        else:
            index = ALPHABET.index(i)
            index = key_1 * (index - key_2) % 26
            print(ALPHABET[int(index)], end='')



if __name__ == '__main__':
    string = input("1.加密 2.解密：")
    if string == '1':
        # 明文
        plaintext = input("请输入明文：")
        key_1 = float(input("请输入 Key-1："))
        key_2 = float(input("请输入 Key-2："))
        Encryption(plaintext, key_1, key_2)
    elif string == '2':
        # 密文
        plaintext = input("请输入密文：")
        key_1 = float(input("请输入 Key-1："))
        key_2 = float(input("请输入 Key-2："))
        Decrypt(plaintext, key_1, key_2)
    else:
        print("请输入 1（加密） 或 2（解密） ")

#Fehk hwj tbr cblux
