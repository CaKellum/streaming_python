from os import system as sys


def _write_to_file(msg):
    with open('message.txt', 'w') as write_file:
        write_file.write(msg)
    return write_file


def _encrypt_message(msg, key):
    file = _write_to_file(message)
    sys_string = 'python ..\my_codex\k_obscurus.py --encrypt {} {}'.format(key, file.name)
    msg = sys(sys_string)
    if msg == 0:
        print('success')
    else:
        print('error try again')


def main():
    print('welcome to the encrypted mesaging.\n please enter the message')
    msg = input('message: ')
    key = input('password: ')
    _encrypt_message(msg, key)
    recipient_email = input('email of recipient: ')


if __name__ == '__main__':
    main()
