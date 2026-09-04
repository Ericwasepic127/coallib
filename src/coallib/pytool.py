#!/usr/bin/env python3
# Made by @Ericwasepic127
import os, sys

python = sys.executable

print("=============================================")
print("Program for CodingPython, but can used \non other programs. ")
print("=============================================")
print("If program not works, you may not \nset python on environment\nvariables. ")

while True: 
    print("=============================================")
    print("1. Install module by pip")
    print("2. Upgrade module by pip")
    print("3. Uninstall module by pip")
    print("4. Command prompt")
    print("5. Currently modules list")
    print("6. Exits program")
    print("=============================================")
    try:
        choice = int(input("Selection (1~6): "))
        print("=============================================")
    
    except ValueError:
        print("=============================================")
        print("Enter number only! ")
        continue

    if choice == 1:
        modname = input("Your install module name: ")
        print("=============================================")
        os.system(f"{python} -m pip install {modname}")
    
    elif choice== 2:
        modname = input("Your upgrade module name: ")
        print("=============================================")
        os.system(f"{python} -m pip install --upgrade {modname}")
    
    elif choice == 3:
        modname = input("Your uninstall module name: ")
        print("=============================================")
        os.system(f"{python} -m pip uninstall {modname}")   
    
    elif choice == 4:
        modname = input("Command: ")
        print("=============================================")
        os.system(modname)   
    
    elif choice == 6:
        print("Bye! ")
        print("=============================================")
        break
    
    elif choice== 5:
        print("Available built-in modules:")
        for module in sys.builtin_module_names:
            print(module)
        print("=============================================")
        print("Availble pip modules")
        os.system(f"{python} -m pip list")
    
    else:
        print("Not in range! ")
        continue
    
