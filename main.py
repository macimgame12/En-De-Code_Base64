import base64
import os
from colorama import Fore


def start_main():
        while 1:
                try:
                        print("What would you like to do: \n1. Encode the text (base64) \n2. Decode the text (base64) \n3. Clear console")
                        question = int(input("> "))
                        if question == 1:
                                text = str(input("Text to encode: ").strip())
                                encoded = base64.b64encode(text.encode()).decode()
                                print(f"Result: {encoded}")
                        elif question == 2:
                                text = str(input("Text to decode: ").strip())
                                decoded = base64.b64decode(text.encode()).decode()
                                print(f"Result: {decoded}")
                        else:
                                os.system("cls")
                except (ValueError, KeyboardInterrupt):
                        os.system("cls")
                        print(Fore.RED + "Please, enter correct values (1/2)" + Fore.RESET)
                        continue
                
                    
if __name__ == '__main__':
        start_main()