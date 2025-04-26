def main(op,str,shift):
  input_func(op,str,shift)
  
def initialize():
  global op
  global str
  global shift
  op = ''
  str = ''
  shift = 0

def input_func(op,str,shift):
  op = input("Do you want to encrypt (e) or decrypt (d)? ")
  if op != 'e' and op != 'd':  #Input validation
    print("Invalid input! Please input either Encrypt (e) or Decrypt (d)") 
    input_func(op,shift,str) 
  str = list(input("Input your string: "))
  shift = int(input("Input the number of characters to shift: "))
  if op == 'e':
    encrypt(str,shift)
  if op == 'd':
    decrypt(str,shift)

def shift_alg(char,shift):
    char = ord(char)
    if char == 32:
      return chr(32)
    else:
      char = char + shift
      return chr((char-65)%26+65)

def encrypt(str,shift):
  encrypted_str = ''
  for i in range(len(str)):
    encrypted_str += shift_alg(str[i],shift)
  print(encrypted_str)

def decrypt(str,shift):
  decrypted_str = ''
  for i in range(len(str)):
    decrypted_str += shift_alg(str[i],shift*-1)
  print(decrypted_str)

if __name__ == "__main__":
  initialize()
  main(op,str,shift)