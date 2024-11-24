print("R or r for new work, U or u for insertion of data in previous titles")
a = input("What do you want to do: ")
EMPLIST = []

def re():
    desname = input("Give a name to the file: ")
    global f
    f = open(desname, 'w')
    return f

def thb():
    th = input("Write your theory further here: ")
    EMPLIST.append(th)

def num():
    mat = "Mathematical relation used or talked about in the above part: " + input("Input your mathematical expression: ")
    EMPLIST.append(mat)
def extra(nt):
    if nt == "1":
        thb()
    elif nt == "2":
        num()
    elif nt == "3":
        im = input("Provide the address to any image or video you want to show in your work here: ")
        EMPLIST.append(im)
    elif nt == "4":
        biblio = input("Bibliography: ")
        print('Report has ended, thanks for working with us.')
        EMPLIST.append('Report ended')
        EMPLIST.append(biblio)

def nxt():
    while True:
        nt = input("1 for entering any theory, 2 for numerical relation, 3 for entering image link, 4 to end the report: ")
        if nt in ["1", "2", "3", "4"]:
            extra(nt)
            if nt == "4":
                break 
        else:
            print("Invalid input, try again.")

def start():
    t = input("Title/name of your project: ")
    T = 'TITLE: ' + t
    EMPLIST.append(T)
    print("p for physics, c for chemistry, b for biology, m for mathematics, cs for computer science")
    global s
    s = input("Subject under which it falls: ")
    S = 'CODE OF CONCERNED SUBJECT: ' + s
    EMPLIST.append(S)

def password():
    
    inp2 = int(input("Input a password for your work (numerical only): "))
    global rpassword
    rpassword = 'PASSWORD: ' + str(inp2)
    return rpassword

if a.lower() == 'r':
    start()
    yourname = 'Author(s): ' + input('Name of people who worked on this project: ') + ':'
    EMPLIST.append(yourname)
    re()
    password()
    EMPLIST.append(rpassword)

    q = "ACCOMPLISHMENT MADE BY THE WORK: " + input("Question/problem solved by your study or accomplishment made: ")
    im = "image : " +  input("Provide the address to any image or video you want to show in your work here: ")
    idb = "introduction : " +  "INTRODUCTION: " + input("Provide your theory's introduction: ")
    fm = m0box = "FINAL MATHEMATICAL RELATION FOUND (if any): " + input("Provide any final mathematical relation or derivation your study suggests, if any: ")
    th = "theory : " + input("Write part 1 of details of your theory: ")
    mat = "MATHEMATICAL RELATION USED OR TALKED ABOUT IN ABOVE PART: " + input("Provide any mathematical expression for part 1 of your theory: ")

    EMPLIST.append(q)
    EMPLIST.append(im)
    EMPLIST.append(idb)
    EMPLIST.append(fm)
    EMPLIST.append(th)
    EMPLIST.append(mat)

    nxt()
    string1 = '\n'.join(EMPLIST)
    f.writelines(string1)
    f.close()

elif a.lower() == 'u':
    e = input("Name of the file you want to edit: ")
    passcode = int(input("Password: "))
    passcode1 = str(passcode)
    try:
        with open(e, 'r') as filere:
            lines = filere.readlines()
        p = "PASSWORD: " + passcode1
        if p in ''.join(lines):
            print("content of desired file is : ")
            print(''.join(lines))
            linenum = int(input('The Serial no. of line you want to update: '))
            if linenum <= len(lines):
                lines[linenum - 1] = input('The new text you want at desired line: ') + '\n'
                with open(e, 'w') as ufile:
                    filere.writelines(lines)

            elif linenum > len(lines):

                with open(e, 'a') as ufile:
                    t1 = int(input("How many lines do you want to add? "))
                    for _ in range(t1):
                        txt = input("Enter the text you want to append: ") + '\n'
                        ufile.write(txt)
                print("New lines added successfully.")

            else:
                print("Invalid line number.")
        
        else:
            print("Wrong password.")
    except FileNotFoundError:
        print("File not found.")
else:
    print("Only R and U are valid inputs. Restart the program to continue.")
