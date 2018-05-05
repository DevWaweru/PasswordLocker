#!/usr/bin/env python3.6

from locker import Credentials

def new_account(id,user_name,password):
    '''
    Function to creating new account
    '''
    new_user = Credentials(id,user_name,password)
    return new_user
def create_user(user):
    '''
    Function that saves the user's credentials
    '''
def main():
    '''
    Main function
    '''
    my_id=0
    print("Hello, Welcome to password Locker.")
    while True:
        print("Type:\n  cc to create new account\n  ss to sign in\n  ex to exit")
        welcome_text = input().lower()
        if welcome_text == "cc":
            print("Create account to continue: \n Enter Username")
            my_username = input()
            print(" Enter password:")
            my_password = input()
            my_id+=1

            print("\n")
            create_user(new_account(my_id,my_username,my_password))
            print(f"User {my_username} has been created. Login to continue..")
            print("-"*20)
        elif welcome_text == "ex".lower():
            break


if __name__ == '__main__':
    main()