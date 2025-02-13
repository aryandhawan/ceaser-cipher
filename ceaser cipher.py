alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
should_continue=True
while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift=shift%26

  def ceaser(start_text,shift_amount,cipher_direction):
    end_text=''
    for letter in start_text:
      position=alphabet.index(letter)
      if cipher_direction=="decode":
        shift_amount*=-1
      new_position=position+shift_amount

  def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
      position = alphabet.index(letter)
      new_position = position + shift_amount
      cipher_text += alphabet[new_position]
    print(f"The encoded text is {cipher_text}")

  #TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
  def decrypt(cipher_text, shift_amount):
    #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
    #e.g.
    #cipher_text = "mjqqt"
    #shift = 5
    #plain_text = "hello"
    #print output: "The decoded text is hello"
    plain_text = ""
    for letter in cipher_text:
      position = alphabet.index(letter)
      new_position = position - shift_amount  #
      plain_text += alphabet[new_position]
    print(f"The decoded text is {plain_text}")

  if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
  elif direction == "decode":
    decrypt(cipher_text=text, shift_amount=shift)
  result=input("type is 'yes ' if you want to go again. otherwise type 'no'.\n")
  if result=='no':
     should_continue=False
     print('Goodbye')




