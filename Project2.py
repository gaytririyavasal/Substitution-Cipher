# File: Project2.py
# Student: Gaytri Vasal
# UT EID: grv377
# Course Name: CS303E
# 
# Date Created: 11/2/2021
# Date Last Modified: 11/8/2021
# Description of Program: The following program executes a substitution cipher and allows an user to manipulate and access the value of the key.

import random

# A global constant defining the alphabet. 
LCLETTERS = "abcdefghijklmnopqrstuvwxyz" 

def isLegalKey( key ):
    # A key is legal if it has length 26 and contains all letters.
    # from LCLETTERS.
    return ( len(key) == 26 and all( [ ch in key for ch in LCLETTERS ] ) )

def makeRandomKey():
    # A legal random key is a permutation of LCLETTERS.
    lst = list( LCLETTERS )  # Turn string into list of letters
    random.shuffle( lst )    # Shuffle the list randomly
    return ''.join( lst )    # Assemble them back into a string

def encryptdecrypt(text, original, result):
    #The following function enables the decryption and encryption of text.
    string = ""
    for ch in text:
        if ("a" <= ch <= "z"):
            string += result[original.find(ch)]
        elif ("A" <= ch <= "Z"):
            character = ch.lower()
            string += result[original.find(character)].upper()
        else:
            string += ch
    return string

class SubstitutionCipher:
    def __init__ (self, key = makeRandomKey()):
        #The initialization method creates an instance of the cipher with a key, which defaults to random. If the key is entered by an user, the function must validate that the key is legal.
        if (isLegalKey(key)):
            self.__key = key
        else:
            print("Key entered is not legal")

    def getKey( self ):
        #This method is the getter for the key that has been stored.
        return self.__key

    def setKey( self, newKey ):
        #This method is the setter for the key that has been stored. It also validates the legality of the key.
        if (isLegalKey(newKey)):
            self.__key = newKey
        else:
            print("Key entered is not legal")
        
    def encryptText( self, plaintext ):
        #The following method encrypts the plaintext using the key and returns the encryption.
        return encryptdecrypt(plaintext, LCLETTERS, self.__key)

    def decryptText( self, ciphertext ):
        #This method decrypts the ciphertext using the key and returns the decryption.
        return encryptdecrypt(ciphertext, self.__key, LCLETTERS)

def main():
    #The following function creates an object using the SubstitutionCipher class. Within the loop included in the function, an user can invoke any of the following commands: getKey, changeKey, encrypt, decrypt, or quit.
        
    cipher = SubstitutionCipher()

    while(True):
        userinput = input("Enter a command (getKey, changeKey, encrypt, decrypt, quit): ")
        userinputmodified = userinput.lower() #The input has been lowercased, as case does not matter for the commands.
        if (userinputmodified == "getkey"): #This command is used to show the current key stored in cipher.
            print("  Current cipher key:", cipher.getKey())
        elif (userinputmodified == "quit"): #This command is utilized to exit the loop.
            print("Thanks for visiting!")
            break
        elif (userinputmodified == "changekey"): #This command enables an user to change the key. He/she can then either enter a valid cipher key, "random", or "quit." If none of these are entered, he/she will receive a chance to try again.
            while(True):
                userinputt = (input("  Enter a valid cipher key, 'random' for a random key, or 'quit' to quit: "))
                userinputtmodified = userinputt.lower() #All commands should be case-insensitive, so the user's input has been converted to lowercase letters.
                if (userinputtmodified == "random"): #The random command creates a new random key and stores it.
                    newKey = makeRandomKey()
                    cipher.setKey(newKey)
                    print("    New cipher key:", cipher.getKey())
                    break
                if (userinputtmodified == "quit"): #The quit command does not change the key and leaves the current loop.
                    break
                else:
                    if (isLegalKey(userinputtmodified)): #If the entered key is legal, it should be stored and printed accordingly.
                        cipher.setKey(userinputtmodified)
                        print("    New cipher key:", cipher.getKey())
                        break
                    else:
                        print("    Illegal key entered. Try again!") #If the entered key is not legal, the following error message is printed, and the user can try again.
        elif (userinputmodified == "encrypt"): #After an user types in this command, he/she can enter some text to encrypt. The text is encrypted afterwards, and the encryption is printed at the end.
            text = input("  Enter a text to encrypt: ")
            print("    The encrypted text is:", cipher.encryptText(text))
        elif (userinputmodified == "decrypt"): #After typing this command, an user can enter some text to decrypt. The text is decrypted afterwards, and the decryption is printed at the end.
            text = input("  Enter a text to decrypt: ")
            print("    The decrypted text is:", cipher.decryptText(text))
        else:
            print("  Command not recognized. Try again!") #If an user enters anything besides the specified commands, the following error message will be printed, and the user may try again.
            continue
    
main()
