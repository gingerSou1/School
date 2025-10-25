"""
_filename: "glover_pw_generator.py
_course name: "SDEV300 6382"
_author: "Corey Glover"
_copyright: "None"
_credits: ["Corey Glover"]
_license: "GPL"
_version: "1.0.0"
_maintainer: "Corey Glover"
_email: "corey.j.glover@student.umgc.edu"
_description: ""
"""
import hashlib


# input a message to encode
repeat_loop = 'y'
while repeat_loop == 'y':
    repeat_loop = str(input("Do you want to enter a "
                            "password? y/n").lower())
    if repeat_loop in ['yes', 'y']:
        print('Enter a message to encode:')
        message = input()
        # encode it to bytes using UTF-8 encoding
        message = message.encode()
        # hash with MD5 (very weak)
        print("This password is in MD5: ")
        print(hashlib.md5(message).hexdigest())
        # Lets try a stronger SHA-2 family
        print("This password is SHA-256: ")
        print(hashlib.sha256(message).hexdigest())
        print("This password is SHA-512: ")
        print(hashlib.sha512(message).hexdigest())
    else:
        break
