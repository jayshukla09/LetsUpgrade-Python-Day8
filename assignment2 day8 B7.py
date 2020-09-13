Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> file = open("binary file.txt","r")

try:
    file.read("binary file.txt")
except:
    print("there was an error")
finally:
    file.close()
print("thanks")

file = open("binary file.txt","r")

try:
    file.write("65")
except Exception as e:
    print("there was an error")
    print("error was -", e)
finally:
    file.close()
print("thanks")
