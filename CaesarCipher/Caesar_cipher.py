# 请用Python3执行

def Encryption(location ,plaintext, length):
    if 0 > location or  25 < location:
        print("偏移量不小于 1，或大于26（不然就没意义了）")
        return
    # 字典库正向
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    ALPHABET = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
                'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    # 位移量所有
    if location == 0:
        for i in range(1,26):
            print(f'偏移{i}位: ', end='')
            for j in range(length):
                # 判断如果是空的话旧输入空，如果不是空就继续加密
                if plaintext[j] == ' ':
                    print(' ', end='')
                else:
                    if plaintext[j] in alphabet:
                        index = alphabet.index(plaintext[j])
                        print(alphabet[index + i], end='')
                    else:
                        index = ALPHABET.index(plaintext[j])
                        print(ALPHABET[index + i], end='')
            print('')
    # 位移量1-24
    else:
        for i in range(length):
            # 判断如果是空的话旧输入空，如果不是空就继续加密
            if plaintext[i] == ' ':
                print(' ', end='')
            else:
                if plaintext[i] in alphabet:
                    index = alphabet.index(plaintext[i])
                    print(alphabet[index+location],end='')
                else:
                    index = ALPHABET.index(plaintext[i])
                    print(ALPHABET[index + location], end='')

def Decrypt(location ,plaintext, length):
    if 0 > location or  25 < location:
        print("偏移量不小于 1，或大于26（不然就没意义了）")
        return

    alphabet = ['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a',
                'z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a']

    ALPHABET = ['Z','Y','X','W','V','U','T','S','R','Q','P','O','N','M','L','K','J','I','H','G','F','E','D','C','B','A',
                'Z','Y','X','W','V','U','T','S','R','Q','P','O','N','M','L','K','J','I','H','G','F','E','D','C','B','A']
    if location == 0:
        for i in range(1,26):
            print(f'偏移{i}位: ', end='')
            for j in range(length):
                # 判断如果是空的话旧输入空，如果不是空就继续加密
                if plaintext[j] == ' ':
                    print(' ', end='')
                else:
                    if plaintext[j] in alphabet:
                        index = alphabet.index(plaintext[j])
                        print(alphabet[index + i], end='')
                    else:
                        index = ALPHABET.index(plaintext[j])
                        print(ALPHABET[index + i], end='')
            print('')
    # 位移量1-24
    else:
        for i in range(length):
            # 判断如果是空的话旧输入空，如果不是空就继续加密
            if plaintext[i] == ' ':
                print(' ', end='')
            else:
               if plaintext[i] in alphabet:
                   index = alphabet.index(plaintext[i])
                   print(alphabet[index + location], end='')
               else:
                   index = ALPHABET.index(plaintext[i])
                   print(ALPHABET[index + location], end='')



if __name__ == '__main__':
    string = input("1.加密 2.解密：")
    if string == '1':
        # 位置
        location = int(input("请输入位移（1-25，0=ALL）："))

        # 明文
        plaintext = input("请输入明文：")

        # 明文长度
        length = len(plaintext)

        Encryption(location, plaintext, length)
    elif string == '2':
        # 位置
        location = int(input("请输入位移（1-25，0=ALL）："))

        # 密文
        plaintext = input("请输入密文：")

        # 密文长度
        length = len(plaintext)

        Decrypt(location, plaintext, length)
    else:
        print("请输入 1（加密） 或 2（解密） ")
