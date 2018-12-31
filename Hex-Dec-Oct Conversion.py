#!/usr/bin/python
# Author : Surya Tadivaka
print ("Python Program - Convert Octal to Binary/Decimal/Hexa")

while True:
    print("Enter 'x' for exit.")
    octal = input("Enter number in Octal Format: ")
    if octal == 'x':
        break
    else:
        dec = str(int(octal, 8))
        decm = int(dec)
        print(octal, "in Binary =", bin(decm), "\n")
        print(octal, "in Decimal =", dec, "\n")
        print(octal, "in Hexadecimal =", hex(decm), "\n")
        break

print ("Python Program - Convert Decimal to Binary/Octal/Hexa")

while True:
    dec = input("Enter number in Decimal Format: ")
    if dec == 'x':
        break
    else:
        decimal = int(dec)
        print(decimal, "in Binary =", bin(decimal), "\n")
        print(decimal, "in Octal =", oct(decimal), "\n")
        print(decimal, "in Hexadecimal =", hex(decimal), "\n")
        break

print ("Python program - Convert Hexadecimal to Binary/Decimal/Octal")

while True:
    hexdec = input("Enter number in Hexadecimal Format: ")
    if hexdec == 'x':
        break
    else:
        dec = int(hexdec, 16)
        print(hexdec, "in Binary =", bin(dec), "\n")
        print(hexdec, "in  Decimal =", str(dec), "\n")
        print(hexdec, "in Octal =", oct(dec), "\n")
        break