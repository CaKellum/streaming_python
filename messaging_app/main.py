from os import system as sys

def main():
    print("welcome to the encrypted mesaging.\n please enter the message")
    message = prompt("message: ")
    key = prompt("password: ")
    file = _write_to_file(message)
    sys_string = 'python k_obscurus.py --encrypt {} {}'.format(key, file.name)
    msg = sys(sys_string)
    if msg == 0:
        print("success")
    else:
        print("error try again")


if __name__ == '__main__':
    main()
