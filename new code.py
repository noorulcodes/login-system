def register():
    db = open("loginsys.txt", "r")
    a = input("Create your username in format __@__.__: ")
    d = []
    for line in db:
        x = line.split(",")
        d.append(x[0])

    if a in d:
        print("Try Again with different username")
        register()

    elif a.count('@') != 1 and a.count('.') != 1:
        print("enter username in proper format")
        register()

    elif ((a.index('@')) - (a.index('.'))) == 1:
        print("Please provide _@_._ format")
        register()

    elif a[0] in range(0, 9):
        print("Start with characters only")
        register()

    elif (a[0] == '@' or a[0] == '$' or a[0] == '_' or a[0] == '%' or a[0] == '!' or a[0] == '#' or a[0] == '*' or a[
        0] == '&'):
        print("Start with only characters")
        register()

    else:
        print("Username created")

    b = input("Create your password with atleast one capital letter one integer and one special character: ")
    s = False

    if len(b) < 5 and len(b) > 16:
        print("Create Password with length between 5 an 16, Try Again")
        register()

    if len(b) > 5 and len(b) < 16:
        l, u, p, d = 0, 0, 0, 0
        for i in b:
            if i.isdigit():
                d += 1
            if i.islower():
                l += 1
            if i.isupper():
                u += 1
            if (i == '@' or i == '$' or i == '_' or i == '%' or i == '!' or i == '#' or i == '*' or i == '&'):
                p += 1
            if (l >= 1 and u >= 1 and p >= 1 and d >= 1 and l + p + u + d == len(b)):
                s = True

    if s:
        c = input("Confirm Password: ")
        while (c != b):
            print("Password not match, Try Again")
            c = input("Try Again: ")

    else:
        print("Try again")
        register()

    file = open("loginsys.txt", "a")
    file.write(a + "," + b + "\n")
    file.close()
    login()

def login():
    X=input("Enter your username to login: ")
    X = X.strip()
    db = open("loginsys.txt", "r")
    d = []
    for line in db:
        x = line.split(",")
        d.append(x[0])

    if X in d:
        Y=input("Please Enter your password: ")
        Y=Y.strip()
        file1=open("loginsys.txt","r").readlines()
        for x in file1:
            x=x.strip()
            info=x.split(",")
            if X==info[0] and Y==info[1]:
                print("Welcome in the digital world")
            else:
                F = input("Forgot Password [Y/N] : ")

                if F == "N":
                    print("try")
                    login()

                if F == "Y":
                    b = input("Create your new password with atleast one capital letter one integer and one special character: ")
                    s = False

                    if len(b) < 5 and len(b) > 16:
                        print("Create Password with length between 5 an 16, Try Again")
                        register()

                    if len(b) > 5 and len(b) < 16:
                        l, u, p, d = 0, 0, 0, 0
                        for i in b:
                            if i.isdigit():
                                d += 1
                            if i.islower():
                                l += 1
                            if i.isupper():
                                u += 1
                            if (
                                    i == '@' or i == '$' or i == '_' or i == '%' or i == '!' or i == '#' or i == '*' or i == '&'):
                                p += 1
                            if (l >= 1 and u >= 1 and p >= 1 and d >= 1 and l + p + u + d == len(b)):
                                s = True

                    if s:
                        c = input("Confirm Password: ")
                        while (c != b):
                            print("Password not match, Try Again")
                            c = input("Try Again: ")

                    else:
                        print("Sorry,Try again to login")
                        login()

                    file = open("access_register.txt", "w")
                    file.write(X + "," + b + "\n")
                    file.close()

    else:
        print("Unregister user you need to register first")
        register()

def welcome():
    print("WELCOME")
    print("login and register")
    W=input("press L for Login, R for Register: ")
    if W=="L":
        login()
    elif W=="R":
        register()
    else:
        print("Enter in proper manner only please")
        welcome()
welcome()
