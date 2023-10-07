# Project Title   : Password Manager
# Version         : 1.0 2021-2022
# Developed By    : Tashif Ahmad Khan
# Guide           : Sarika Kaushal
# Last Updated On : <2022-02-05>


from pyperclip import copy
import random
import csv

USERNAME = None
quit = ""
forgot_password_questions = ["Q1. What is your favourite animal? ", "Q2. Name of your pet if any ", "Q3. What's your birthplace? ", "Q4. What's your favourite timepass? "]


def decode(INPUT):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u','v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '@', '#', '$', '%', '&', '^', '(', ')','-','_','=', '*', '+','[',']','{','}','|',':',';',"'",'"',',','.','<','>','/','?',',']

    end_text = ""
    shift_amount = -4
    for i in INPUT:
        if i in letters:
            position = letters.index(i)
            new_position = position + shift_amount
            
            if new_position >= 52:
                new_position = new_position - 52
            
            end_text += letters[new_position]

        elif i in numbers:
            position = numbers.index(i)
            new_position = position + shift_amount
            
            if new_position >= 10:
                new_position = new_position - 10
            
            end_text += numbers[new_position]

        elif i in symbols:
            position = symbols.index(i)
            new_position = position + shift_amount

            if new_position >= 30:
                new_position = new_position - 30
            
            end_text += symbols[new_position]

        else:
            end_text += i

    return end_text

def encode(INPUT):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u','v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '@', '#', '$', '%', '&', '^', '(', ')','-','_','=', '*', '+','[',']','{','}','|',':',';',"'",'"',',','.','<','>','/','?',',']

    end_text = ""
    shift_amount = 4
    for i in INPUT:
        if i in letters:
            position = letters.index(i)
            new_position = position + shift_amount
            
            if new_position >= 52:
                new_position = new_position - 52

            end_text += letters[new_position]

        elif i in numbers:
            position = numbers.index(i)
            new_position = position + shift_amount
            
            if new_position >= 10:
                new_position = new_position - 10            
            
            end_text += numbers[new_position]

        elif i in symbols:
            position = symbols.index(i)
            new_position = position + shift_amount
            
            if new_position >= 30:
                new_position = new_position - 30
            
            end_text += symbols[new_position]

        else:
            end_text += i

    return end_text


def sign_up():
    global USERNAME
    try:
        with open("users.csv") as file:
            cR = csv.reader(file)
            f = []
            
            for i in cR:
                f.append(i)
            
            if len(f) > 1:
                with open("users.csv", "r") as fi:
                    cR = csv.reader(fi)
                    next(cR)
                    username_list = []
                    for lists in cR:
                        username_list.append(lists[0])
                    while True:    
                        USERNAME = input("Enter your desired username: ")
                        if USERNAME in username_list:
                            print("Username already taken try another one \n ")
                        else:
                            print("Username successfully set. ")
                            break

                    password = input("Enter your password: ")
                    password = encode(password)

                    name = input("Enter you name: ")
                    for i in forgot_password_questions:
                        print(i)
                    print()
                    print("Pick any 3 questions from the above mentioned.")
                    
                    Ques1 = input("Choose the 1st question: ")
                    Ans1 = input("Answer of the selected question: ")
                    Ans1 = encode(Ans1)
                    if len(Ques1) > 1:
                        Ques1 = Ques1[-1]
                    
                    Ques2 = input("Choose the 2nd question: ")
                    Ans2 = input("Answer of the selected question: ")
                    Ans2 = encode(Ans2)
                    if len(Ques2) > 1:
                        Ques2 = Ques2[-1]

                    Ques3 = input("Choose the 3rd question: ")
                    Ans3 = input("Answer of the selected question: ")
                    Ans3 = encode(Ans3)
                    if len(Ques3) > 1:
                        Ques3 = Ques3[-1]
                    
                    with open(f"{USERNAME}.csv", "w", newline="") as file2:
                        cW = csv.writer(file2)
                        cW.writerow(["SHORTNAME", "URL/UTILITY", "USER ID", "LOCAL PASSWORD"])

                    with open("users.csv", "a", newline="") as f:
                        cW = csv.writer(f)
                        cW.writerow([USERNAME, name, password, [Ques1, Ans1], [Ques2, Ans2], [Ques3, Ans3], f"{USERNAME}.csv"])
            
            elif len(f) == 1:
                USERNAME = input("Enter your desired username: ")
                print("Username successfully set. ")

                password = input("Enter your password: ")
                password = encode(password)

                name = input("Enter you name: ")
                for i in forgot_password_questions:
                    print(i)
                print()
                print("Pick any 3 questions from the above mentioned.")
                
                Ques1 = input("Choose the 1st question: ")
                Ans1 = input("Answer of the selected question: ")
                Ans1 = encode(Ans1)
                if len(Ques1) > 1:
                    Ques1 = Ques1[-1]

                Ques2 = input("Choose the 2nd question: ")
                Ans2 = input("Answer of the selected question: ")
                Ans2 = encode(Ans2)
                if len(Ques2) > 1:
                    Ques2 = Ques1[-1]

                Ques3 = input("Choose the 3rd question: ")
                Ans3 = input("Answer of the selected question: ")
                Ans3 = encode(Ans3)
                if len(Ques3) > 1:
                    Ques3 = Ques3[-1]

                with open(f"{USERNAME}.csv", "w", newline="") as file2:
                    cW = csv.writer(file2)
                    cW.writerow(["SHORTNAME", "URL/UTILITY", "USER ID", "LOCAL PASSWORD"])

                with open("users.csv", "a", newline="") as f:
                    cW = csv.writer(f)
                    cW.writerow([USERNAME, name, password, [Ques1, Ans1], [Ques2, Ans2], [Ques3, Ans3], f"{USERNAME}.csv"])

    except:
        with open("users.csv", "w+", newline="") as file:
            cW = csv.writer(file)
            cW.writerow(["USERNAME", "NAME", "MASTER PASSWORD", "FORGOT Q1 ANS", "FORGOT Q2 ANS", "FORGOT Q3 ANS", "PASSWORD FILE"])
            file.seek(0)
            cR = csv.reader(file)
            f = []
            
            for i in cR:
                f.append(i)
            
            if len(f) > 1:
                with open("users.csv", "r") as fi:
                    cR = csv.reader(fi)
                    next(cR)
                    username_list = []
                    for lists in cR:
                            username_list.append(lists[0])
                    while True:    
                        USERNAME = input("Enter your desired username: ")
                        if USERNAME in username_list:
                            print("Username already taken try another one \n ")
                        else:
                            print("Username successfully set. ")
                            break

                    password = input("Enter your password: ")
                    password = encode(password)

                    name = input("Enter you name: ")
                    for i in forgot_password_questions:
                        print(i)
                    print()
                    print("Pick any 3 questions from the above mentioned.")
                    
                    Ques1 = input("Choose the 1st question: ")
                    Ans1 = input("Answer of the selected question: ")
                    Ans1 = encode(Ans1)
                    if len(Ques1) > 1:
                        Ques1 = Ques1[-1]

                    Ques2 = input("Choose the 2nd question: ")
                    Ans2 = input("Answer of the selected question: ")
                    Ans2 = encode(Ans2)
                    if len(Ques2) > 1:
                        Ques2 = Ques1[-1]

                    Ques3 = input("Choose the 3rd question: ")
                    Ans3 = input("Answer of the selected question: ")
                    Ans3 = encode(Ans3)
                    if len(Ques3) > 1:
                        Ques3 = Ques3[-1]
                    
                    with open(f"{USERNAME}.csv", "w", newline="") as file2:
                        cW = csv.writer(file2)
                        cW.writerow(["SHORTNAME", "URL/UTILITY", "USER ID", "LOCAL PASSWORD"])

                    with open("users.csv", "a", newline="") as f:
                        cW = csv.writer(f)
                        cW.writerow([USERNAME, name, password, [Ques1, Ans1], [Ques2, Ans2], [Ques3, Ans3], f"{USERNAME}.csv"])
            
            elif len(f) == 1:
                USERNAME = input("Enter your desired username: ")
                print("Username successfully set. ")

                password = input("Enter your password: ")
                password = encode(password)

                name = input("Enter you name: ")
                for i in forgot_password_questions:
                    print(i)
                print()
                print("Pick any 3 questions from the above mentioned.")
                
                Ques1 = input("Choose the 1st question: ")
                Ans1 = input("Answer of the selected question: ")
                Ans1 = encode(Ans1)
                if len(Ques1) > 1:
                    Ques1 = Ques1[-1]

                Ques2 = input("Choose the 2nd question: ")
                Ans2 = input("Answer of the selected question: ")
                Ans2 = encode(Ans2)
                if len(Ques2) > 1:
                    Ques2 = Ques2[-1]

                Ques3 = input("Choose the 3rd question: ")
                Ans3 = input("Answer of the selected question: ")
                Ans3 = encode(Ans3)
                if len(Ques3) > 1:
                    Ques3= Ques3[-1]

                with open(f"{USERNAME}.csv", "w", newline="") as file2:
                    cW = csv.writer(file2)
                    cW.writerow(["SHORTNAME", "URL/UTILITY", "USER ID", "LOCAL PASSWORD"])

                with open("users.csv", "a", newline="") as f:
                    cW = csv.writer(f)
                    cW.writerow([USERNAME, name, password, [Ques1, Ans1], [Ques2, Ans2], [Ques3, Ans3], f"{USERNAME}.csv"])


def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u','v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '@', '#', '$', '%', '&', '^', '(', ')','-','_','=', '*', '+','[',']','{','}','|',':',';',"'",'"',',','.','<','>','/','?',',']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password = ""
    
    for l in range(1, nr_letters + 1):
        password += random.choice(letters)
    
    for n in range(1, nr_numbers + 1):
        password += random.choice(numbers)
    
    for s in range(1, nr_symbols + 1):
        password += random.choice(symbols)

    generated_password = list(password)
    random.shuffle(generated_password)
    
    generated_password = "".join(generated_password)
    
    if input("Do you want to copy this password (Y/N): ").lower() == "y":
        copy(generated_password)
    
    return generated_password


def save_password():
    global USERNAME
    web = input("Website/App/Utility: ").lower()
    print("The category of 'Short name' is optional if you don't intend to fill it just press Enter.")
    shortname = input("Short name: ").lower()
    email = input("Local Username: ")
    g_o = input("""
    Do you want to auto-generate strong password (G)
    or
    do you want you enter your own (O):
    """)
    if g_o in "Oo":
        paswrd = input("Password: ")
        paswrd = encode(paswrd)
    
    elif g_o in "Gg":
        paswrd = generate_pass()
        print(f"Generated Password: {paswrd}")
        paswrd = encode(paswrd)
    
    with open(f"{USERNAME}.csv","a", newline="") as cf:
        cw = csv.writer(cf)
        cw.writerow([shortname, web, email, paswrd])


def search():
    print("You can search for passwords (& user id) either by its short name or url. \nEnter any of the 2 categories")
    web = input("Website/App/Utility: ").lower()
    shortname = input("Short name: ").lower()

    with open(f"{USERNAME}.csv") as f:
        cR = csv.reader(f)
        next(cR)
        web_list = []
        shortname_list = []
        for lists in cR:
            shortname_list.append(lists[0])
            web_list.append(lists[1])
    
    if web not in web_list and shortname not in shortname_list:
            print("You haven't saved the credentials for the given utility.")

    else:
        with open(f"{USERNAME}.csv") as f:
            cr = csv.reader(f)
            for data in cr:
                if data[1] == web or data[0] == shortname:
                    print(f"User id: {data[2]}")
                    print(f"Password: {decode(data[3])}")

                    z = input("Do you want to copy the password? [Y/N] ")
                    if z in "Yy":
                        copy(decode(data[3]))
                    else:
                        continue


def update():
    print("You can change passwords (& user id) either by its short name or url. \nEnter any of the 2 categories")
    web = input("Website/App/Utility: ").lower()
    shortname = input("Short name: ").lower()

    archive = []

    with open(f"{USERNAME}.csv") as f:
        cR = csv.reader(f)
        next(cR)
        web_list = []
        shortname_list = []
        for lists in cR:
            shortname_list.append(lists[0])
            web_list.append(lists[1])
    
    if web not in web_list and shortname not in shortname_list:
            print("You haven't saved the credentials for the given utility.")

    else:
        Choice = '''What do you want to change?
        1. User id
        2. Password
        3. Both\n
        '''

        choice = input(Choice)

        if choice == "1":
            new_userid = input("Enter the new user id: ")
            with open(f"{USERNAME}.csv","r") as f:
                cr = csv.reader(f)
                for data in cr:
                    if data[1] == web or data[0] == shortname:
                        archive.append([data[0], data[1], new_userid, data[3]])
                    else:
                        archive.append(data)
        
        elif choice == "2":
            new_password = input("Enter the new password: ")
            with open(f"{USERNAME}.csv","r") as f:
                cr = csv.reader(f)
                for data in cr:
                    if data[1] == web or data[0] == shortname:
                        archive.append([data[0], data[1], data[2], encode(new_password)])
                    else:
                        archive.append(data)
        
        elif choice == "3":
            new_userid = input("Enter the new user id: ")
            new_password = input("Enter the new password: ")
            with open(f"{USERNAME}.csv","r") as f:
                cr = csv.reader(f)
                for data in cr:
                    if data[1] == web or data[0] == shortname:
                        archive.append([data[0], data[1], new_userid, encode(new_password)])
                    else:
                        archive.append(data)
        
    
        with open(f"{USERNAME}.csv","r+", newline="") as f:
            cW = csv.writer(f)
            f.truncate(0)
            f.seek(0)
            cW.writerows(archive)


def delete():
    ch='''
    What is your intention?
    1. Delete credentials of a particular site
    2. Delete all the credentials stored
    3. Nuke your account {if you use this your account would cease to exist}\n
    '''
    archive = []
    
    CH = input(ch)

    if CH == "1":
        with open(f"{USERNAME}.csv") as f:
            cR = csv.reader(f)
            next(cR)
            web_list = []
            shortname_list = []
            for lists in cR:
                shortname_list.append(lists[0])
                web_list.append(lists[1])

        print("You can delete credentials either by its short name or url. \nEnter any of the 2 categories")
        web = input("Website/App/Utility: ").lower()
        shortname = input("Short name: ").lower()
        
        if web not in web_list and shortname not in shortname_list:
            print("You haven't saved the credentials for the given utility.")
        
        else:
            with open(f"{USERNAME}.csv","r+", newline="") as f:
                cr = csv.reader(f)
                cw = csv.writer(f)
                for data in cr:
                    if data[1] == web or data[0] == shortname:
                        continue
                    else:
                        archive.append(data)
                
                f.truncate(0)
                f.seek(0)
                cw.writerows(archive)

    
    elif CH == "2":
        with open(f"{USERNAME}.csv","r+", newline="") as f:
            cW = csv.writer(f)
            f.truncate(0)
            f.seek(0)
            cW.writerow(["SHORTNAME","URL/UTILITY","USER ID","LOCAL PASSWORD"])
    
    elif CH == "3":
        with open("users.csv", "r+", newline="") as f:
            cR = csv.reader(f)
            cW = csv.writer(f)
            for user in cR:
                if user[0] == USERNAME:
                    continue
                else:
                    archive.append(user)

            f.truncate(0)
            f.seek(0)
            cW.writerows(archive)   


def forgot_password():
    list_questions = []
    global USERNAME
    try:
        while True:
            USERNAME = input("Enter your username: ")
            z = ""
            with open("users.csv") as file:
                cR = csv.reader(file)
                next(cR)
                username_list = []
                for lists in cR:
                    username_list.append(lists[0])            

                while True:
                    if USERNAME not in username_list:
                        print("User does not exist")
                        z = input("Try again... \nor Quit by pressing [Q] {continue by entering}...")
                        if z.lower() == "q":
                            break
                        else:
                            USERNAME = input("Enter your username: ")
                    
                    if USERNAME in username_list:
                        break
                    
                file.seek(0)
                if z.lower() != "q":
                    for i in cR:
                        if i[0] == USERNAME:
                            list_questions.extend([i[3], i[4], i[5]])
            
            if z.lower() == "q":
                break

            name = input("Enter your name: ")
            n = ""
            
            with open("users.csv") as f:
                cR = csv.reader(f)
                for i in cR:
                    if i[0] == USERNAME:
                        if i[1] == name:
                            print("Answer the following questions :- ")
                            for i in list_questions:
                                f = int(i[2]) - 1
                                q = "Q. " + forgot_password_questions[f][3::] + "\n"
                                a = input(q)
                                a = encode(a).lower()
                                if a == i[7:-2].lower():
                                    print("Correct answer.")
                                    n = "c"
                                    print()
                                else:
                                    print("Wrong answer.")
                                    n = "w"
                                    print("Request of changing password denied.")
                                    break
                            else:
                                print("You have answered all the questions correctly.")
                                print()
                                print(f"WELCOME BACK {name} !")
                                new_pswd = input("\nenter the new password: ")
                                new_pswd = encode(new_pswd)
                                
                                with open("users.csv", "r+", newline="") as f:
                                    cR = csv.reader(f)
                                    cW = csv.writer(f)
                                    L = []
                                    n = "w"
                                    for user in cR:
                                        if user[0] == USERNAME:
                                            L.append([user[0], user[1], new_pswd, user[3], user[4], user[5], user[6]])
                                        else:
                                            L.append(user)
                                    
                                    f.truncate(0)
                                    f.seek(0)
                                    cW.writerows(L)

                        else:
                            print("Incorrect name. Try Again...")
                            n = "w"

            if n == "w":
                break    
            
                        
    except FileNotFoundError:
        print(f"No data for username - {USERNAME}")
        print("You need to sign up first")
        print()
        print("SIGNING YOU UP...")
        print()
        sign_up()
        while True:
            USERNAME = input("Enter your username: ")
            z = ""
            with open("users.csv") as file:
                cR = csv.reader(file)
                next(cR)
                username_list = []
                for lists in cR:
                    username_list.append(lists[0])            

                while True:
                    if USERNAME not in username_list:
                        print("User does not exist")
                        z = input("Try again... \nor Quit by pressing [Q] {continue by entering}...")
                        if z.lower() == "q":
                            break
                        else:
                            USERNAME = input("Enter your username: ")
                    
                    if USERNAME in username_list:
                        break
                    
                file.seek(0)
                if z.lower() != "q":
                    for i in cR:
                        if i[0] == USERNAME:
                            list_questions.extend([i[3], i[4], i[5]])
            
            if z.lower() == "q":
                break

            name = input("Enter your name: ")
            n = ""
            
            with open("users.csv") as f:
                cR = csv.reader(f)
                for i in cR:
                    if i[0] == USERNAME:
                        if i[1] == name:
                            print("Answer the following questions :- ")
                            for i in list_questions:
                                f = int(i[2]) - 1
                                q = "Q. " + forgot_password_questions[f][3::] + "\n"
                                a = input(q)
                                a = encode(a).lower()
                                
                                if a == i[7:-2].lower():
                                    print("Correct answer.")
                                    n = "c"
                                    print()
                                
                                else:
                                    print("Wrong answer.")
                                    n = "w"
                                    print("Request of changing password denied.")
                                    break
                            else:
                                print("You have answered all the questions correctly.")
                                print()
                                print(f"WELCOME BACK {name} !")
                                new_pswd = input("\nenter the new password: ")
                                
                                with open("users.csv", "r+", newline="") as f:
                                    cR = csv.reader(f)
                                    cW = csv.writer(f)
                                    L = []
                                    n = "w"
                                    for user in cR:
                                        if user[0] == USERNAME:
                                            L.append([user[0], user[1], new_pswd, user[3], user[4], user[5], user[6]])
                                        else:
                                            L.append(user)
                                    
                                    f.truncate(0)
                                    f.seek(0)
                                    cW.writerows(L)

                        else:
                            print("Incorrect name. Try Again...")
                            n = "w"

            if n == "w":
                break    

                          
                
def show_all():
    u = []
    with open(f"{USERNAME}.csv") as f:
        cR = csv.reader(f)
        for i in cR:
            u.append(i)
        
    if len(u) == 1:
        print("No credentials stored... ")
        print()
    
    else:
        with open(f"{USERNAME}.csv") as f:
            cR = csv.reader(f)
            next(cR)
            for data in cR:
                if data[0] == "":
                    shortname = "N/A"
                    print("SHORTNAME:", shortname)
                    print("UTILITY:", data[1])
                    print("USERNAME:", data[2])
                    print("PASSWORD:", decode(data[3]))
                    print()
                
                elif data[1] == "":
                    url = "N/A"
                    print("SHORTNAME:", data[0])
                    print("UTILITY:", url)
                    print("USERNAME:", data[2])
                    print("PASSWORD:", decode(data[3]))
                    print()
                
                else:
                    print("SHORTNAME:", data[0])
                    print("UTILITY:", data[1])
                    print("USERNAME:", data[2])
                    print("PASSWORD:", decode(data[3]))
                    print()



def  sign_in():
    global USERNAME
    global quit
    USERNAME = input("Username: ")
    
    try:
        alpha = ""
        with open("users.csv") as file:
            cR = csv.reader(file)
            next(cR)
            
            username_list = []
            for lists in cR:
                username_list.append(lists[0])

            while USERNAME not in username_list:
                print("User does not exist")
                x ='''
                Try:
                1. Signing up {by pressing 1}
                2. Read your username carefully and try again {by pressing 2}
                3. For going back to the main screen press 3
                '''
                z = input(x)
                if z == "1":
                    sign_up()

                elif z == "2":
                    USERNAME = input("USERNAME: ")

                elif z == "3":
                    break

            while USERNAME in username_list:
                if quit == "yes":
                    break
                
                else:
                    for i in range(5):
                        if alpha == "stop":
                            break
                        else:
                            pswd = input("Enter your Master Password: ")
                            pswd = encode(pswd)

                            with open("users.csv") as f:
                                cr = csv.reader(f)
                                for users in cr:
                                    if users[0] == USERNAME:
                                        if users[2] == pswd:
                                            alpha = "stop"
                                            file =  f"{USERNAME}.csv"
                                            print("You have successfully logged in.")
                                            
                                            option = '''
                                            What would you want to do?
                                            1. Search
                                            2. Add
                                            3. Update
                                            4. Delete
                                            5. Show All
                                            6. Quit
                                            Choose by entering the number corresponding to the action \n
                                            '''
                                            
                                            while True:
                                                ch = input(option)
                                                
                                                if ch == "1":
                                                    search()
                                                
                                                elif ch == "2":
                                                    save_password()
                                                
                                                elif ch == "3":
                                                    update()
                                                
                                                elif ch == "4":
                                                    delete()
                                                
                                                elif ch == "5":
                                                    show_all()
                                                
                                                elif ch == "6":
                                                    quit = "yes"
                                                    break
                                                
                                                else:
                                                    print("Wrong input. ")
                                                    
                                                cho = input("Want to carry out any other operations? [Y/N]")

                                                if cho in "Nn":
                                                    quit = "yes"
                                                    break
                                                
                                                elif cho in "Yy":
                                                    quit = ""
                                                
                                                else:
                                                    print("Wrong input")
                                                    break
                                            break
                                            
                                        
                                        else:
                                            file = None
                                            print("INCORRECT PASSWORD!")
                                            print(f"only {4-i} attempts left")
                                            if i == 0:
                                                CHO = input("Would you like use recovery {forgot password} [Y/N] ")
                                                if CHO in "Yy":
                                                    forgot_password()
                                                else:
                                                    continue 

                    else:                    
                        print("You have exhausted all your attempts. \ngo to the main options and try 'Forgot Password' option.")
                        print()
                        CH = input("You have two options now:\n\
                            Quit (q)\n\
                            (OR)\n\
                            use recovery{forgot password} (f)\n")
                            
                        if CH in "Qq":
                            quit ="yes"
                            break

                        elif CH in "Ff":
                            forgot_password()
            
    except FileNotFoundError:
        print(f"No data for username - {USERNAME}")
        print("You need to sign up first")
        print()
        print("SIGNING YOU UP...")
        print()
        sign_up()

        alpha = ""
        
        with open("users.csv") as file:
            cR = csv.reader(file)
            next(cR)
            
            username_list = []
            for lists in cR:
                username_list.append(lists[0])

            while USERNAME not in username_list:
                print("User does not exist")
                x ='''
                Try:
                1. Signing up {by pressing 1}
                2. Read your username carefully and try again {by pressing 2}
                3. For going back to the main screen press 3
                '''
                z = input(x)
                if z == "1":
                    sign_up()

                elif z == "2":
                    USERNAME = input("USERNAME: ")

                elif z == "3":
                    break

            while USERNAME in username_list:
                if quit == "yes":
                    break
                
                else:
                    for i in range(5):
                        if alpha == "stop":
                            break
                        else:
                            pswd = input("Enter your Master Password: ")

                            with open("users.csv") as f:
                                cr = csv.reader(f)
                                for users in cr:
                                    if users[0] == USERNAME:
                                        if users[2] == pswd:
                                            alpha = "stop"
                                            file =  f"{USERNAME}.csv"
                                            print("You have successfully logged in.")
                                            
                                            option = '''
                                            What would you want to do?
                                            1. Search
                                            2. Add
                                            3. Update
                                            4. Delete
                                            5. Show All
                                            6. Quit
                                            Choose by entering the number corresponding to the action \n
                                            '''
                                            
                                            while True:
                                                ch = input(option)
                                                
                                                if ch == "1":
                                                    search()
                                                
                                                elif ch == "2":
                                                    save_password()
                                                
                                                elif ch == "3":
                                                    update()
                                                
                                                elif ch == "4":
                                                    delete()
                                                
                                                elif ch == "5":
                                                    show_all()
                                                
                                                elif ch == "6":
                                                    quit = "yes"
                                                    break
                                                
                                                else:
                                                    print("Wrong input. ")
                                                    
                                                cho = input("Want to carry out any other operations? [Y/N]")

                                                if cho in "Nn":
                                                    quit = "yes"
                                                    break
                                                
                                                elif cho in "Yy":
                                                    quit = ""
                                                
                                                else:
                                                    print("Wrong input")
                                                    break

                                            break
                                            
                                        
                                        else:
                                            file = None
                                            print("INCORRECT PASSWORD!")
                                            print(f"only {4-i} attempts left")
                                            if i == 0:
                                                CHO = input("Would you like use recovery {forgot password} [Y/N] ")
                                                if CHO in "Yy":
                                                    forgot_password()
                                                else:
                                                    continue                                                     
                    else:                    
                        print("You have exhausted all your attempts. \ngo to the main options and try 'Forgot Password' option.")
                        print()
                        CH = input("You have two options now:\n\
                            Quit (q)\n\
                            (OR)\n\
                            use recovery {forgot password} (f)\n")
                            
                        if CH in "Qq":
                            quit ="yes"
                            break

                        elif CH in "Ff":
                            forgot_password()



    
cH = '''
Welcome!

What do you want to do !?
1. Sign Up
2. Sign In
3. Recover {forgot password}
4. Quit
Choose by entering the number corresponding to the action.
'''               

while True:
    Ch = input(cH)

    if Ch == "1":
        sign_up()

    elif Ch == "2":
        sign_in()

    elif Ch == "3":
        forgot_password()

    elif Ch == "4":
        break

    else:
        print("Incorrect input.")
    
    print()
    terminate = input("Do you want to continue!?[Y/N] ")
    if terminate in "Yy":
        quit = ""
        continue
    
    elif terminate in "Nn":
        break