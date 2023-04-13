import morse

print("\t\t\t\t***********************")

print("\t\t\t\t MORSE CODE TRANSLATOR ")

print("\t\t\t\t***********************")

print("\n")

ch = input("Press 'E' to encrypt and 'D' to decrypt: ")

print("\n")

if ch.lower() == 'e':

    plain_text = input("Enter Text to encrypt: ").upper()

    print("\n")

    # Using the morse library to convert plain text to Morse code

    morse_code = morse.encode(plain_text)

    print("Encrypted Text: ", morse_code)

elif ch.lower() == 'd':

    morse_code = input("Enter morse code to decrypt: ")

    print("\n")

    # Using the morse library to convert Morse code to plain text

    plain_text = morse.decode(morse_code)

    print("Decrypted Text: ", plain_text)

else:

    print("Invalid input!!!")

