def shift_alg(chr,shift):
    if chr == 32:
        return 32
    else:
        chr = chr + shift
        return (chr-65)%26+65

def convert(str):
    ascii_arr = []
    encrypted_ascii = []
    encrypted_arr = []
    encrypted_str = ''
    str_arr = list(str)
    for i in range (len(str_arr)):
        ascii_arr.append(ord(str_arr[i]))
        encrypted_ascii.append(shift_alg(ascii_arr[i],shift))
        encrypted_arr.append(chr(encrypted_ascii[i]))
    for i in range (len(encrypted_arr)):
        encrypted_str = encrypted_str + encrypted_arr[i]
    print(encrypted_str)

str = input("Input your string: ")
shift = int(input("Input the number of characters you want to shift: "))
convert(str)