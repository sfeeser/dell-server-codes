#!/usr/bin/env python3

import re
import os

def main():

    # Many Dell servers are codes by four variables enumerated here:
    char1 = {
              "C": "Compute optimized hyper-scale server",
              "F": "Rack-based sleds for FX2/FX2s enclosure",
              "M": "Modular Blade server",
             "MX": "Modular Blade server",
              "R": "Rack-mountable",
             "XE": "Extreme performance and storage",
             "XR": "Extreme ruggedness"
            }

    char2 = [
             "NA",
             "1 Socket",
             "1 Socket",
             "1 Socket",
             "2 Sockets",
             "2 Sockets",
             "2 Sockets",
             "2 Sockets",
             "2 or 4 sockets",
             "4 Sockets"
            ]
 
    char3 = [
             "Gen 10",
             "Gen 11",
             "Gen 12",
             "Gen 13",
             "Gen 14",
             "Gen 15",
             "Gen 16",
             "Gen 17",
             "Gen 18",
             "Gen 19"
            ]

    char4 = {
            "0": "Intel",
            "5": "AMD"
            }  

    os.system('clear')
    code = input("Enter a server code: ")

    # This REGEX is a *very* common for parsing input. Look it over.
    pattern = re.compile(r"""
                             (?P<c1>[a-zA_Z]+)
                             (?P<c2>\d)
                             (?P<c3>\d)
                             (?P<c4>\d)
                          """, re.VERBOSE)
    match = pattern.match(code)
    if match:
        # If we get this far, the input matched the REGEX
        code1 = match.group("c1").upper()
        code2 = int(match.group("c2"))
        code3 = int(match.group("c3"))
        code4 = match.group("c4")
    else:
       # Well now, the input was really bad, give helpful info 
       # FIRST ERROR HANDLING OUTPUT STARTS HERE 
       print(f"The first character is the chassis type")
       print(f"---------------------------------------------")
       for key in char1.keys():
           print (f"{key} = {char1[key]}")
   
       print(f"\nThe second character is the socket count")
       print(f"---------------------------------------------")
       i=0
       for item in char2:
           print (f"{i} = {item}")
           i +=1
   
       print(f"\nThe third character is the generation")
       print(f"---------------------------------------------")
       i=0
       for item in char3:
           print (f"{i} = {item}")
           i +=1
   
       print(f"\nThe fourth character is the CPU type")
       print(f"---------------------------------------------")
       for key in char4.keys():
           print (f"{key} = {char4[key]}")
       print(f"---------------------------------------------\n")
       print(f"You entered \"{code}\" which is NOT a dell server code\n")
       print("You must enter a valid code like r450 or mx345\n")
       print("Reference the above and PLEASE TRY AGAIN\n")
       
       exit() # No use continuing. Exit to the command line
       # FIRST ERROR HANDLING ENDS HERE

    print(f"Looking up Dell {code1}{code2}{code3}{code4}") 

    if code1 in char1:
        print(f"  {code1} = {char1[code1]}")
    else:
        #code1 ERROR HANDLING STARTS
        print(f"{code1} is an invalid, valid codes are:")
        for key in char1.keys():
            print (f"    {key} = {char1[key]}")
        #code1 ERROR HANDLING ENDS

    if 1 <= code2 <= 9:
        print(f"  {code2} = {char2[code2]}")
    else:
        #code2 ERROR HANDLING STARTS
        print(f"  {code2} is invalid. Valid CPU socket codes are:")
        i=0
        for item in char2:
            print (f"    {i} = {item}")
            i +=1
        #code2 ERROR HANDLING ENDS    

    if 0 <= code3 <= 9:
       print(f"  {code3} = {char3[code3]}")
    else:
        #code3 ERROR HANDLING STARTS
        print(f"error: {code3} Must be 0 to 9")
        i=0
        for item in char3:
            print (f"{i} = {item}")
            i +=1
        #code3 ERROR HANDLING ENDS

    if code4 in char4:
        print(f"  {code4} = {char4[code4]}")
    else:
        #code4 ERROR HANDLING STARTS
        print(f"  {code4} is invalid, here are valid options:")
        for key in char4.keys():
           print (f"     {key} = {char4[key]}")
        #code4 ERROR HANDLING ENDS

if __name__ == "__main__":
    main()

