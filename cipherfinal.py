import hashlib

# clue 1------------------------------------------------------------

def clue1(cipher, shift):
    pw1 = ""
    for char in cipher:
        if char.isalpha():
            shifted = ord(char) - shift
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
            pw1 += chr(shifted)
        else:
            pw1 += char
    return pw1

print("ENTER Cipher for CLUE 1:")
cipher_text = input()
pwd1 = clue1(cipher_text, 3)


# clue 2-----------------------------------------------


with open("Rockyou.txt", "r", encoding="utf-8", errors="ignore") as file:
    pwrdlist = file.read().splitlines()
print("ENTER HASH CODE for clue 2:")
z = input()

def check(hsh, pwrd):
    for i in pwrd:
        hpwrd = hashlib.sha256(i.encode()).hexdigest()
        if hpwrd == hsh:
            return i
        
    return None

sol = check(z, pwrdlist)

if not sol:
    print("Hashing algorithm is not in the program")
    exit()
else:
    pwd2=sol
    
# clue 3 -------------------------------------------------

d = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z', '/': ' '
}

def clue3(morse_code):
    words = morse_code.split(' / ')
    decoded_message = ''
    for word in words:
        characters = word.split()
        for char in characters:
            decoded_message += d.get(char, '')
        decoded_message += ' '
    return decoded_message.strip()
print("Enter CLUE 3:")
morse_code = input()
pwd3 = clue3(morse_code)

print ("FINAL DECODED PASSWORD IS:")

finalpassword=pwd1+"_"+pwd2+"_"+pwd3
print(finalpassword)