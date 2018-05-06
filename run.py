#!/usr/bin/env python3.6

from locker import Credentials,UsersData

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
    user.create_account()

def authenticate(username,passkey):
    '''
    Function responsible for signing in
    '''
    return Credentials.authenticate_account(username,passkey)

def my_new_data(user_id,data_id,website,web_key):
    '''
    Function that creates new data for storing password
    '''
    new_data = UsersData(user_id,data_id,website,web_key)
    return new_data

def add_data(data):
    '''
    Function that saves the new data created
    '''
    data.add_password();

def display_data(data,number):
    '''
    Function that displays the user data
    '''
    return UsersData.display_data(data,number)

def data_existing(data):
    '''
    Function that checks if user data exists
    '''
    return UsersData.existing_data(data)

    
def main():
    '''
    Main function
    '''
    my_id=0
    # my_data_id = 0
    entries = []
    print("\n")
    print("       Welcome to password Locker")
    print("-"*40)
    while True:
        print("Type:\n  cc to create new account\n  ss to sign in\n  ex to exit")
        welcome_text = input().lower()
        if welcome_text == "cc":
            print("Create account to continue: \n Enter Username")
            my_username = input()
            print(" Enter password:")
            my_password = input()

            print("\n")
            create_user(new_account(my_id,my_username,my_password))
            my_id+=1
            print(f"User {my_username} has been created. Login to continue..")
            entries.append(0)
            print("-"*20)

        elif welcome_text == "ss".lower():
            print("Enter username and password to continue:")
            print("Username: ")
            my_login = input()
            print("Password: ")
            my_key = input()
            get_result = authenticate(my_login,my_key)
            if get_result == 0:
                print("Invalid username and/or password")
            elif get_result!=0:
                print(f"{get_result.identify} has logged in")
                print(f"Welcome {get_result.user_name}! What would you like to do?")
                while True:
                    print("Type:\n  ad - Add Password\n  vp - View Passwords\n  lo - Log Out")
                    get_input = input().lower()
                    if get_input == "ad":
                        print("Enter Website:")
                        my_website = input()
                        print("Generate password")
                        my_webkey = input()
                        # my_data_id = my_data_id+1
                        my_ident = get_result.identify
                        add_data(my_new_data(my_ident,entries[my_ident],my_website,my_webkey))
                        entries[my_ident]=entries[my_ident]+1
                        print(f"Password on {my_website} has been created")
                        print(f"This is the {entries[my_ident]} entry")

                    elif get_input == "vp":
                        if data_existing(get_result.identify):
                            print("Your passwords are: \n")
                            length = entries[get_result.identify]
                            print(length)
                            data_my=0
                            while data_my < length:
                                get_password = display_data(get_result.identify,data_my)
                                print(f"{get_password.website} ---- {get_password.web_key}")
                                data_my+=1
                        else:
                            print("No data exists on this user")

                    elif get_input == "lo":
                        break
                    
                    else:
                        print("Invalid entry. Enter command again")
                        print("\n"+"-"*40)

        elif welcome_text == "ex".lower():
            break

        else:
            print("\n")
            print("Invalid entry. Enter command again")
            print("\n"+"-"*40)


if __name__ == '__main__':
    main()