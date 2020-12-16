# python mycodex -encrypt/-decrypt (key) message_file
from math import pow
from sys import argv
from re import split
import json

def _get_convert(c):
    return ord(c)

def _change_to_octal(dec):
    nums = []
    octval = 0;
    while dec != 0:
        nums.insert(len(nums),dec%8)
        dec = int(dec/8)
    for i in range(len(nums)):
        octval += nums[i] * pow(10,i)
    return octval


def _write_file(message, direction):
    if direction == 0:
        #expecxts a list
        message_dict={}
        message_dict["message"] = message
        with open('message_out.json','w') as message_file:
            json.dump(message_dict,message_file)
    else:
        #expects string as message
        with open('message_in.txt','w') as message_file:
            message_file.write(message)



def _encrypt():
    cipher_text = [];
    message = open(argv[3],'r').read()
    for i in range(len(message)):
        num = _change_to_octal(_get_convert(message[i]))+_get_convert(argv[2][i%len(argv[2])])
        cipher_text.insert(len(cipher_text),(num%len(argv[2]), num%_change_to_octal(128)))
    _write_file(cipher_text,0)


def _decrypt():
    cipher_txt = json.load(open(argv[3]))
    print(cipher_txt["mesage"])


def  main():
    if argv[1] == '--decrypt':
        _decrypt()
    elif argv[1] == '--encrypt':
        _encrypt()
    else:
        print('please use format --enrypt/--decrypt <key> <message_file>')




if __name__ == '__main__':
    main()
