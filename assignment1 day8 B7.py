Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = int(input("enter integer number:- "))
if nterms <= 0:
    print("enter valid number")
else:
    print("fibonacci sequence:")
    for i in range(nterms):
        print(recur_fibo(i))