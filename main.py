import os
import pymongo
from colorama import Fore
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def start():
    os.system('cls')
    print(Fore.GREEN +
          "==================================================================================================")
    print("|                                                                                                |")
    print("|                               WELCOME TO EXPLOTARY DATA ANALYSIS SYSTEM                        |")
    print("|                                                                                                |")
    print("|                                     PLEASE SIGN UP TO CONTINUE                                 |")
    print("|                                                                                                |")
    print("|                                                                                                |")
    print("|                               1.PRESS 1 TO SIGNIN                                              |")
    print("|                               2.PRESS 2 TO CREATE ACCOUNT                                      |")
    print("|                                                                                                |")
    print("|                               ENTER YOUR CHOICE BELOW : 👇 👇                                  |")
    print("|                                                                                                |")
    print("|                                                                                                |")
    print("|                                                                                                |")
    print("|                                                                                                |")
    print("|                                                                                                |")
    print("|                                                                                                |")
    print("|                                                                                                |")
    print("==================================================================================================")
    x = input(Fore.CYAN+"                                  YOUR CHOICE: ")
    if (x == '1'):
        signin()
    elif (x == '2'):
        signup()
    else:
        print(Fore.RED+"Wrong Choice Entered! Please Enter The Correct Choice")
        start()


def main(path):
    os.system('cls')
    for i in path:
        if i == "\\":
            i = "/"
    df = pd.read_csv(path)

    print(Fore.GREEN +
          "==================================================================================================")
    print("|                                                                                                |")
    print("|                           WELCOME TO EXPLOTARY DATA ANALYSIS SYSTEM                            |")
    print("|                                                                                                |")
    print("|   PLEASE CHOOSE AN OPTION TO PERFORM THE CORRESPONDING OPERATION ON THE IMPORTED FILE          |")
    print("|                                                                                                |")
    print("|                                                                                                |")
    print("|                     1.PRESS 1 TO SHOW THE FILE                                                 |")
    print("|                     2.PRESS 2 TO SHOW ALL INFORMATION RELATED TO FILE                          |")
    print("|                     3.PRESS 3 TO DESCRIBE THE FILE                                             |")
    print("|                     4.PRESS 4 TO CHECK ALL THE NULL VALUES IN THE FILE                         |")
    print("|                     5.PRESS 5 TO FIND THE SUM OF ALL THE NULL VALUES IN THE FILE               |")
    print("|                     6.PRESS 6 TO FIND THE SUM OF THE SUM OF ALL THE NULL VALUES IN THE FILE    |")
    print("|                     7.PRESS 7 TO FILL THE VALUE IN PLACE OF NULL VALUES IN THE FILE            |")
    print("|                     8.PRESS 8 TO PRINT ALL THE NAME OF THE COLUMNS                             |")
    print("|                     9.PRESS 9 TO  SHOW THE GRAPH Of VARIOUS COLUMNS                            |")
    print("|                                                                                                |")
    print("|                                                                                                |")
    print("|                                                                                                |")
    print("|                               ENTER YOUR CHOICE BELOW : 👇 👇                                  |")
    print("==================================================================================================")
    x = input("                                  YOUR CHOICE: ")
    if x == '1':
        print(df)
        n = input(Fore.CYAN+"Want to Continue press Y to continue and N to exit: ")
        if n == 'Y' or n == 'y':
            main(path)
        else:
            exit()
    elif x == '2':
        print(df.info())
        n = input(Fore.CYAN+"Want to Continue press Y to continue and N to exit: ")
        if n == 'Y' or n == 'y':
            main(path)
        else:
            exit()
    elif x == '3':
        print(df.describe())
        n = input(Fore.CYAN+"Want to Continue press Y to continue and N to exit: ")
        if n == 'Y' or n == 'y':
            main(path)
        else:
            exit()
    elif x == '4':
        print(df.isnull())
        n = input(Fore.CYAN+"Want to Continue press Y to continue and N to exit: ")
        if n == 'Y' or n == 'y':
            main(path)
        else:
            exit()
    elif x == '5':
        print(df.isnull().sum())
        n = input(Fore.CYAN+"Want to Continue press Y to continue and N to exit: ")
        if n == 'Y' or n == 'y':
            main(path)
        else:
            exit()
    elif x == '6':
        print(df.isnull().sum().sum())
        n = input(Fore.CYAN+"Want to Continue press Y to continue and N to exit: ")
        if n == 'Y' or n == 'y':
            main(path)
        else:
            exit()
    elif x == '7':
        print(df.fillna(method="pad", inplace=True))
        n = input(Fore.CYAN+"Want to Continue press Y to continue and N to exit: ")
        if n == 'Y' or n == 'y':
            main(path)
        else:
            exit()
    elif x == '8':
        print(df.columns.to_list())
        n = input(Fore.CYAN+"Want to Continue press Y for Yess and N to exit: ")
        if n == 'Y' or n == 'y':
            main(path)
        else:
            exit()
    elif x == '9':
        colname = input(Fore.CYAN +
                        "Enter the column name of which you want see the Graph: ")
        figure = sns.countplot(x=colname, data=df, color="crimson")
        fig = figure.set_xticklabels(
            figure.get_xticklabels(), rotation=40, ha="right")
        plt.title(Fore.CYAN+"Graph of "+colname+" is plotted Below 👇👇 ")
        plt.tight_layout()
        print(fig)
        print()
        print()
        n = input(Fore.CYAN+"Want to Continue press Y for Yess and N to exit: ")
        if n == 'Y' or n == 'y':
            main(path)
        else:
            exit()
    else:
        print(Fore.RED+"YOU HAVE ENTERED WRONG CHOICE! ")
        n = input(Fore.CYAN+"Want to Continue press Y for Yess and N to exit: ")
        if n == 'Y' or n == 'y':
            main(path)
        else:
            exit()


def signin():
    os.system('cls')
    print(Fore.GREEN +
          "==================================================================================================")
    print("|                                                                                                |")
    print("|                               WELCOME TO EXPLOTARY DATA ANALYSIS SYSTEM                        |")
    print("|                                                                                                |")
    print("|                                     PLEASE SIGN IN TO CONTINUE                                 |")
    print("|                                                                                                |")
    print("|                                                                                                |")
    print("|                                                                                                |")
    print("|                               ENTER YOUR CEREDENTIALS BELOW : 👇 👇                            |")
    print("|                                                                                                |")
    print("|                                                                                                |")
    print("|                                                                                                |")
    print("|                                                                                                |")
    print("|                                                                                                |")
    print("|                                                                                                |")
    print("|                                                                                                |")
    print("==================================================================================================")
    name = input(Fore.CYAN+"                          YOUR NAME: ")
    password = input(Fore.CYAN+"                   ENTER YOUR PASSWORD: ")
    client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
    mydb = client['User']
    userinfo = mydb.userinformation
    username = userinfo.find_one({"Name": name})
    userpassword = userinfo.find_one({"Password": password})
    if (username and userpassword):
        os.system('cls')
        print()
        print(Fore.GREEN+"=============== WELCOME TO EXPOLATRY DATA ANALYSIS SYSTEM ======================")
        print()
        path = input(Fore.CYAN+"ENTER THE PATH OF THE FILE : ")
        main(path)
    else:
        os.system('cls')
        print(Fore.RED+"incorrect username or password")
        cont = input(Fore.CYAN+"enter Y to continue E to exit: ")
        if cont == 'y' or cont == 'Y':

            start()
        else:
            os.system('cls')
            exit()


def signup():
    os.system('cls')
    print(Fore.GREEN +
          "==================================================================================================")
    print("|                                                                                                |")
    print("|                               WELCOME TO EXPLOTARY DATA ANALYSIS SYSTEM                        |")
    print("|                                                                                                |")
    print("|                                    PLEASE SIGN UP TO CONTINUE                                  |")
    print("|                                                                                                |")
    print("|                                                                                                |")
    print("|                                                                                                |")
    print("|                               ENTER YOUR DETAILS BELOW : 👇 👇                                 |")
    print("|                                                                                                |")
    print("|                                                                                                |")
    print("|                                                                                                |")
    print("|                                                                                                |")
    print("|                                                                                                |")
    print("|                                                                                                |")
    print("|                                                                                                |")
    print("==================================================================================================")
    name = input(Fore.CYAN+"                          ENTER YOUR NAME : ")
    mobile = input(Fore.CYAN+"                        ENTER YOUR MOBILE NO : ")
    password = input(Fore.CYAN+"                      ENTER YOUR PASSWORD : ")
    client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')

    mydb = client['User']
    userinfo = mydb.userinformation
    record = {
        "Name": name,
        "Mobile": mobile,
        "Password": password
    }
    result = userinfo.insert_one(record)
    if (result):
        signin()
    else:
        print("error while recording details")


start()
