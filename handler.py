def input_error(func):
    def inner(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except KeyError:
            return ("Enter user name")
        except ValueError:
            return ("Give me name and phone please")
        except IndexError:
            return ("enter the correct index")
        except:
            return ("wrong command")
        return func
    return inner

@input_error
def main(slow = dict()):
    messenge=input("Enter your message: ")
    messenge=str(messenge).lower()
    intex = str(messenge).split(" ")
    if intex[0] == "hello":
        print("How can I help you?")
        main(slow)
    elif intex[0] == "add":
        slow[intex[1]] = [intex[2]]
        main(slow)
    elif intex[0] == "change":
        slow[intex[1]].append(intex[2])
        main(slow)
    elif intex[0]=="phone":
        for key,value in slow.items():
            if key==intex[1]:
                print(value)
                main(slow)
    elif messenge== "show all":
        print(slow)
        main(slow)
    if messenge=="good bye" or intex[0]=="close" or intex[0]=="exit":
        return "Good bye!"
    else:
        print("wrong command")
        main(slow)
main()