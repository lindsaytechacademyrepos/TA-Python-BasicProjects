#3.7.0
#Author: Lindsay Alexander
#Purpose: Training video

def start(nice=0,mean=0,name=""): #this is how you define default values in case a user doesn't provide it
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)

def describe_game(name):
    if name!="":
        print("\nThank you for playing again,{}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name? \n>>> ").capitalize()
            if name != "":
                print("\nWelcome, {}!".format(name))
                print("\nIn this game you will be greeted \nby several different people. \nYou may choose to be nice or mean")
                print("but at the end of the game your fate \nwill be sealed by your actions")
                stop = False #caps again
    return name


def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input("\nA stranger approaches you for a \nconversation. Will you be nice \nor mean? (N/M) \n>>>").lower()
        if pick == "n":
            print ("\nThe stranger walks away smiling...")
            nice = nice + 1
            stop = False
        if pick == "m":
            print ("\nThe stranger glares at you \nmenacingly and storms off...")
            mean = mean + 1
            stop = False
    score(nice,mean,name)

def show_score(nice,mean,name):
    print ("\n{}, your current total: \n{}, Nice and {}, Mean)".format(name,nice,mean))


def score(nice,mean,name):
    if nice > 2:
        win(nice,mean,name)
    if mean > 2:
        lose(nice,mean,name)
    else:
        nice_mean(nice,mean,name)

def win(nice,mean,name):
    print("Nice job {}, you win! Everynoe loves you and you've made lots of friends!".format(name))
    again(nice,mean,name)

def lose(nice,mean,name):
    print("So sad, you lost, {}!".format(name))
    again(nice,mean,name)

def again(nice,mean,name):
    stop = True
    while stop:
        choice = input("Do you want to play again Y/N: \n>>> ").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == "n":
            print("So sorry to see you go")
            stop = False
            quit()
        else:
            print("Enter Y for yes and N for no:\n>>> ")

def reset(nice,mean,name):
    nice = 0
    mean = 0
    #don't reset name because the same player is playing and we don't want to ask them again
    start(nice,mean,name)



    
