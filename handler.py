import sys

slow = dict()


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return ("Enter user name")
        except ValueError:
            return ("Give me name and phone please")
        except IndexError:
            return ("enter the correct index")
    return inner

def hello():
    return "How can I help you?"

def good_bye():
    sys.exit()

@input_error
def add(message):
    intex = message.split(' ')
    user_name = intex[0]
    user_number = intex[1]
    if user_name not in slow:
        slow[user_name] = user_number
    return f'User {user_name} successfully added'

@input_error
def change(message):
    intex = message.split(' ')
    user_name = intex[0]
    user_number = intex[1]
    slow[user_name] = user_number
    return f'User {user_name} changed number to {user_number}'

@input_error
def phone(user_name):
    return slow[user_name]

def console_show():
    return slow

CONTROLLER = {'hello': hello,
              'add': add,
              'change': change,
              'phone': phone,
              'show all': console_show,
              'good bye': good_bye,
              'exit': good_bye,
              'close': good_bye,
              }


def main():
    command_console = None
    while True:
        message = input("Enter your message: ")
        if command_console is None:
            if message.lower() in ['add', 'change', 'phone']:
                command_console = CONTROLLER[message.lower()]
                continue
            elif message.lower() in ['hello', 'good bye', 'exit', 'close', 'show all']:
                command_console = CONTROLLER[message.lower()]
                result = command_console()
                command_console = None
                print(result)
                continue
            else:
                print("Enter valid command: hello, good bye, exit, close, add, change, phone, show all")
                continue
        result = command_console(message)
        command_console = None
        print(result)

if __name__ == '__main__':
    main()