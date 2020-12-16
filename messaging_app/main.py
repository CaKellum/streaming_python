from os import system as sys
from termcolor import colored


def _write_to_file(msg):
    with open('message.txt', 'w') as write_file:
        write_file.write(msg)
    return write_file


def _encrypt_message(msg, key):
    file = _write_to_file(msg)
    sys_string = 'python ../my_codex/k_obscurus.py --encrypt {} {}'.format(key, file.name)
    msg = sys(sys_string)
    if msg == 0:
        print(colored('success','green'))
    else:
        print(colored('error try again','red'))


def main():
    print('welcome to the encrypted mesaging.\n please enter the message')
    msg = input('message: ')
    key = input('password: ')
    _encrypt_message(msg, key)
    recipient_email = input('email of recipient: ')


if __name__ == '__main__':
    main()
