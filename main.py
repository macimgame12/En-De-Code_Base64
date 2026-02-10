import base64
import os
from colorama import Fore


def base_start(value: int):
        if value == 1:
                os.system("cls")
                print("What would you like to do:")
                print(" 1. Encode the text (base64)")
                print(" 2. Decode the text (base64)")
                print(" 3. Clear console")
                print(" 4. Exit\n")
        elif value == 2:
                os.system("cls")
                print("You can do:")
                print(" 1. Back")
                print(" 2. Exit\n")
        elif value == 3:
                os.system("cls")
                print("What would you like to do:")
                print(" 1. Encode the text (base64)")
                print(" 2. Decode the text (base64)")
                print(" 3. Clear console")
                print(" 4. Exit")
                print(Fore.RED + "Please, enter correct values (1/2/3/4)" + Fore.RESET + "\n")
        elif value == 4:
                os.system("cls")
                print("What would you like to do:")
                print(" 1. Encode the text (base64)")
                print(" 2. Decode the text (base64)")
                print(" 3. Clear console")
                print(" 4. Exit")
                print(Fore.RED + "Invalid command" + Fore.RESET + "\n")

def start_main():
        index_start = 1
        while 1:
                try:
                        base_start(index_start)
                        index_start = 1
                        c = int(input("> "))
                        
                        if c == 1:
                                while 1:
                                        index_start = 2
                                        base_start(index_start)
                                        text = str(input("Text to encode: ").strip())
                                        if text == '1':
                                                index_start = 1
                                                break
                                        elif text == '2':
                                                return
                                        else:
                                                encoded = base64.b64encode(text.encode()).decode()       
                                                print(f"Result: {encoded}")
                                                index_start = 1
                                                break
                        elif c == 2:
                                while 1:
                                        index_start = 2
                                        base_start(index_start)
                                        text = str(input("Text to decode: ").strip())
                                        if text == '1':
                                                index_start = 1
                                                break
                                        elif text == '2':
                                                return
                                        else:        
                                                decoded = base64.b64decode(text.encode()).decode()       
                                                print(f"Result: {decoded}")
                                                index_start = 1
                                                break
                        elif c == 3:
                                os.system("cls")
                                index_start = 1
                        elif c == 4:
                                return
                        else:
                                index_start = 4
                        
                except (ValueError, KeyboardInterrupt):
                        index_start = 3
                        continue
                
                    
if __name__ == '__main__':
        start_main()