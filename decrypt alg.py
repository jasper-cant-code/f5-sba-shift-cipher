def shift_alg(chr,shift):
    if chr == 32:
        return 32
    else:
        chr = chr - shift
        return (chr-65)%26+65

def convert(str):
    ascii_arr = []
    decrypted_ascii = []
    decrypted_arr = []
    decrypted_str = ''
    str_arr = list(str)
    for i in range (len(str_arr)):
        ascii_arr.append(ord(str_arr[i]))
        decrypted_ascii.append(shift_alg(ascii_arr[i],shift))
        decrypted_arr.append(chr(decrypted_ascii[i]))
    for i in range (len(decrypted_arr)):
        decrypted_str = decrypted_str + decrypted_arr[i]
    print(decrypted_str)

str = input("Input your string: ")
shift = int(input("Input the number of characters you want to shift: "))
convert(str)