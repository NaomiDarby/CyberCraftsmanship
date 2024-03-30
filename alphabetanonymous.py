letters = 'abcdefghijklmnopqrstuvwxyz'

      
def encrypt(plaintext, key):
    ciphertext = ''
    for letter in plaintext:
       letter = letter.lower()
       if not letter == ' ':
          index = letters.find(letter)
          if index == -1:
             ciphertext += letter
          else:
             new_index = index + key
             if new_index >= 26:
                new_index -= 26
             ciphertext += letters[new_index]     
    return ciphertext          

def decrypt(ciphertext, key):
    plaintext = ' '
    for letter in ciphertext:
       letter = letter.lower()
       if not letter == ' ':
          index = letters.find(letter)
          if index == -1:
             plaintext += letter
          else:
             new_index = index - key
             if new_index > 0:
                new_index -= 26
             plaintext += letters[new_index]     
    return plaintext              
                   


print()
print(' **Alphabet Anynomoyous**  ')
print()

print('Would you like to encrypt or decrypt?')
user_input = input ('e/d: ').lower()
print()

if user_input == 'e': 
    print ('Encryption selected')
    print()
    key = int(input('Please enter key (1-26): ')) 
    text = input('Please enter text you wish to encrypt: ')
    ciphertext = encrypt(text, key)
    print(f'Encrypted Message: {ciphertext}')


elif user_input == 'd': 
    print ('Decryption selected')
    print()
    key = int(input('Please enter key (1-26): ')) 
    text = input('Please enter text you wish to decrypt: ')
    plaintext = decrypt(text, key)
    print(f'Decrypted Message: {plaintext}')