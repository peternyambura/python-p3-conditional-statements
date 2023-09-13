#!/usr/bin/env python3

def admin_login(username, password):
    if username.ascii_lowercase() == "admin" and password =="1234":
        return "Accsess granted"
    else:
        return "Accsess Denied, Contact Admin for Help"
    pass

def hows_the_weather(temperature):
    if temperature < 40:
        return "It's brisk out there!"
    elif 40 <= temperature <= 65:
        return "It's a little chilly out there!"
    elif temperature >=85:
        return "It's too dang hot out there!"
    else:
        return "Its perfect out there"
    
def fizzbuzz(num):
    # your code here
    pass

def calculator(operation, num1, num2):
    # your code here
    pass
