# number checker program

# imports
import requests
import tkinter as tk
from tkinter import messagebox

# defining the check number function
def check_phone_number():
    """ Callback function to vaildate phone number via the api"""
    phone_number = phone_entry.get()
    if not phone_number:
        messagebox.showwarning("Input Error", "Please enter a phone number :)")
        return
    
    # try to send a api request and then handle the response
    try:
        # api endpoint/ set up the headders, url, and data
        
    print(" code has gotten to here sucessfully")