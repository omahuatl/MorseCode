"""
12 de septiembre 2021
MorseCode main
Test the MorseCode converter
"""
from art import morse_legend
from morse_code import MorseCode

machine_mc= MorseCode()

print("Welcome to Morse Code translator")
#print(art)
print(morse_legend)
print(" 0 - dits")
print(" 1 - dash")
message=input("Give the message to be sent...:")
morse=machine_mc.to_morse_code(message)
print(" 0 - dits")
print(" 1 - dash")
print(f"Your meesage in morse_code...:\n {morse}")




