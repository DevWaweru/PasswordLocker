# PasswordLocker
## Password locker is a simple python app that generates passwords for different user accounts
### May 4th, 2018
#### By **[Richard Waweru](https://github.com/devwaweru)**

## Description
Password Locker is an application that helps users generate and store passwords on their multiple accounts.
The password locker runs on the terminal and uses short codes to navigate through it.
When starting up the application, the user is met with the following shortcodes:

    1. cc - Creates a new account
    2. ss - Sign in
    3. ex - Exit the application

The user will be met with the following commands while signing in:

    1. ad - Add password
    2. vp - View passwords
    3. cp - Copy password to clipboard
    4. lo - Log out

## Specifications
| Behavior            | Input                         | Output                        | 
| ------------------- | ----------------------------- | ----------------------------- |
| Create new account | Type: cc <br>Username: Richi <br>Password: pass | User Richi has been created.<br>Log in to Continue |
| Sign in | Type: ss <br>Username: Richi<br>Password: pass | Welcome Richi! What would you like to do? |
| Add Password | Type: ad <br>Website: mywebsite.com <br>Length of password: 10 | **Generates a password with x length**<br>Your password for mywebsite.com is eyDB58eh49 |
| View list of passwords | Type: vp | Generates a lists of websites and passwords |
| Copy Password to clipboard | Type: cp <br>Enter index: 1 | Password 1 on the list has been copied and is ready for pasting |
| Log Out | Type: lo | **Logs out the user** <br>Goodbye Richi! |
| Exit Application | Type: ex | **Closes the application** <br>Goodbye!! |

## Prerequiites
    - Python 3.6 required

## Set-up and Installation
    - Clone the Repo
    - Install python 3.6
    - Run `python3.6 run.py`

## Known bugs
No known errors if found drop a message on my profile

## Technologies used
    - Python 3.6

## Support and contact details
Contact me on developer.waweru@gmail.com for any comments, reviews or advice.

### License
Copyright (c) **Richard Waweru**
