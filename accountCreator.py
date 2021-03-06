"""This is a program that allows the user to create an infinite number of password protected accounts
   and then log in with either of those to list all the accounts registered during its run. 
   It was envisioned to be an exercise in str or dict value manipulation while working with if-elif-else and while statements. """

import sys, pprint

# placeholder for a dictionary style list of accounts\passwords. 

accounts = {}

""" This menu pops up after user logs in. User can now see all accounts\passwords he has created, or exit the program. 
The option to sign out is also scripted in, and it takes the user back to the welcome screen.""" 

def afterlog():
    print ('You have succesfully logged in, what do you want to do?')
    print('To look at your accounts, type "A". To exit the program, type "E". To sign out, type "L". ')
    endAnswer = input()
    if endAnswer == 'A' or endAnswer == 'a':
        pprint.pprint (accounts)
        afterlog() 
    elif endAnswer == 'E' or endAnswer == 'e':
        print ('This program is succesfully terminated')
        sys.exit()
    elif endAnswer == 'L' or endAnswer == 'l':
        print(username, ' has just signed out.')
        startscreen()
    else:
        print ('Not a valid answer. Please try again.')
        afterlog()

#  When this function is called, user is prompted to create a new account username. The username and the password are added to accounts dictionary.

def registration():
    newAccount = ('')
    newPassword = ('')
    print('To create a new account, type in your username. To go b, type "<".')
    newAccount = input()
    if newAccount == "<":
        print ('\n')
        startscreen()
    elif newAccount.isalnum() == False:
        print ('Please use letters and numbers only.')
        registration()
    elif newAccount in list(accounts.keys()):
        print ('Can\'t create the new account. The account with the same name already exists! Plase try another name.')
        registration()
    else:
        print ('That\'s a valid account name.')
        while newPassword.isalnum() == False or newPassword != "<" or newPassword != "<<":
            print ('Now, type in your password. (to go back type "<". To go back to start screen, type "<<"')
            newPassword = input()
            if newPassword == "<":
                print ('\n')
                registration()
            elif newPassword == "<<":
                print ('\n')
                startscreen()
            elif newPassword.isalnum() == False:
                print('That is not a valid password. Please use letters and numbers only!')
            elif newPassword.isalnum() == True:
                accounts.setdefault(newAccount, newPassword)
                print ('Congratulations. You have created a new account')
                regAnswer = ('')
                while regAnswer != 'Y' or regAnswer != 'y' or regAnswer != 'N' or regAnswer != 'n':
                    print ('Would you like to create another account? Type "Y" for yes and "N" to go back to start screen.') 
                    regAnswer = input()
                    if regAnswer == "Y" or regAnswer == "y":
                        registration()
                    elif regAnswer == "n" or regAnswer == "n":
                        startscreen()
                    else:
                        print ('Not a valid answer. Please tell us. ')

# A log-in menu for the user. Prompts to enter an account name with the correct corresponding password.

def login():
    print ('Log in. What is your username? (Use "<" to go back to startscreen')
    global username
    username = input()
    if username.isalnum() == False:
        if username != '<':
            print ('Please, type in a valid account name, only numbers and letters are allowed.')
            login()
        elif username == '<':
            startscreen()   
    if username.isalnum() == True:
        if username in list(accounts.keys()):
            print ('Ok, ', username, '. Now, tell us your password?' )
            loginpass = input()
            if loginpass == accounts[username]:
                print ('Hello', username + '.')
                afterlog()
            if loginpass != accounts[username]:
                print ('Wrong password. Please try to log in again.') 
                login()
        if username not in list(accounts.keys()):
            print ('That account does not exist. Please try loggin in with an existing account.')
            login ()

#Welcome screen, presents the user with following options: Register a new account, Log in with existing account, Quit the program.

def startscreen(): 
    stAnswer = ('')
    while True:
        print ('Do you want to sign in or log in?')
        print('Type "R" in order to proceed to registration or "L" to log into your account. (or type "Q" to quit)') 
        stAnswer = input()
        if stAnswer == "R" or stAnswer == "r":
            registration()
        elif stAnswer == "L" or stAnswer == "l":
            login()
        elif stAnswer == "Q" or stAnswer =="q":
            print ('You have succesfuly exited the program')
            sys.exit()
            break
        else:
            print ('\nNot a valid answer. Please type "R", "L", or "Q".\n')

#initializes the program

startscreen()
