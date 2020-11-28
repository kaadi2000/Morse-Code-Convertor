import pyperclip
import time

morse_code = ("-.-.--",".--.-.",".-...","-.--.","-.--.-",   #1
"T",".-.-.","-...-","-----",".----",                        #2
"..---","...--","....-",".....","-....",                    #3
"--...","---..","----.",".-","-...",                        #4
"-.-.","-..",".","..-.","--.",                              #5
"....","..",".---","-.-",".-..",                            #6
"--","-.","---",".--.","--.-",                              #7
".-.","...","-","..-","...-",                               #8
".--","-..-","-.--","--..","---...",                        #9
".-..-.",".----.","--..--","E",                             #10
"-..-.","..--..","\\")                                      #11

alphabet_code = ("!","@","&","(",")",                       #1
"-","+","=","0","1"                                         #2
"2","3","4","5","6",                                        #3
"7","8","9","A","B",                                        #4
"C","D","E","F","G",                                        #5
"H","I","J","K","L",                                        #6
"M","N","O","P","Q",                                        #7
"R","S","T","U","V",                                        #8
"W","X","Y","Z",":",                                        #9
"\"","\'",".",",",".",                                      #10
"/","?"," ")                                                #11

def main_menu():
    print("\n1.Encrypt my message\n2.Decrypt my message\n3.Developer Contact\n4.Exit")
    main=input("\nEnter your choice:")
    if main == "1":
        encrypt()
    elif main == "2":
        decrypt()
    elif main == "3":
        developer_contact()
    elif main == "4":
        exit()
    else:
        print("\nInvalid Input! Try Again!\n")
        time.sleep(2.0)
        main_menu()

def encrypt():
    message = input("\nEnter your message:").upper()
    print("")
    encrypt_message = ''
    for i in message:
        try:
            index_morse = alphabet_code.index(i)
            encrypt_message = encrypt_message + morse_code[index_morse] + " "
        except:
            print("\nInvalid characters in input!!\n")
            main_menu()
    print(encrypt_message)
    pyperclip.copy(encrypt_message)
    print("\nYour message has been copied to clipboard!!\n")
    main_menu()

def decrypt():
    message = [str(x) for x in input("\nEnter your message:").split()]
    print("")
    decrypt_message = ''
    for i in message:
        try:
            index_alphabet = morse_code.index(i)
            decrypt_message = decrypt_message + alphabet_code[index_alphabet] + " "
        except:
            print("\nInvalid characters in input!!\n")
            main_menu()
    print(decrypt_message)
    pyperclip.copy(decrypt_message)
    print("\nYour message has been copied to clipboard!!\n")
    main_menu()

def developer_contact():
    print("\nDeveloper Name: Kumar Aditya\nE-mail: aditya.g.2005001@gmail.com\n")
    menu2=input("Press any key for Main Menu:")
    main_menu()

print("\n\nWelcome to the MORSE CODE ENCRYPT AND DECRYPT")
time.sleep(3.0)
main_menu()
