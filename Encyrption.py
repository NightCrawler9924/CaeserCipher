import string
class CaesarCipher:
    def __init__(self, shift=3):  #in ceaser cipher we need to shift by 3
        self.shift = shift
        self.alphabet = string.ascii_lowercase    # Instance attribute

    def encrypt(self, text):
        return self._shift_text(text, self.shift)

    def decrypt(self, text):
        return self._shift_text(text, -self.shift)


    def _shift_text(self, text, shift):
        encrypted_text = ""
        for a in text:
            if a.isalpha():  
                is_upper = a.isupper()
                a = a.lower()  # Converted to lowercase
                new = (self.alphabet.index(a) + shift) % 26  # Shift will always be 3 as defined above
                new_a = self.alphabet[new]  # get the shifted character
                
                if is_upper:
                    encrypted_text +=  new_a.upper() 
                else:
                    encrypted_text += new_a 
            else:
                encrypted_text += a  

        return encrypted_text  # Return the final encrypted text


    def encrypt_file(self, input_file, output_file):
        with open(input_file, 'r') as f:
            s = f.read()
        encrypted_content = self.encrypt(s)
        with open(output_file, 'w') as f:
            f.write(encrypted_content)

    def decrypt_file(self, input_file, output_file):
        with open(input_file, 'r') as f:
            s = f.read()
        decrypted_content = self.decrypt(s)
        with open(output_file, 'w') as f:
            f.write(decrypted_content)

if __name__ == "__main__":
    cipher = CaesarCipher(shift=3)
    text = input("Enter text to encrypt: ")
    encrypted_text = cipher.encrypt(text)
    decrypted_text = cipher.decrypt(encrypted_text)
    cipher = CaesarCipher(shift=3)

cipher.encrypt_file('abc.txt', 'encrypted.txt')

cipher.decrypt_file('abc.txt', 'decrypted.txt')


print(f"\nEncrypted: {encrypted_text}\nDecrypted: {decrypted_text}")
