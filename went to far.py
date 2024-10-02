# DATA and patent MANAGEMENT
print ("R or r for new work , U or u for insertion of data in previous titles")
a= input("what do you want to do :")
EMPLIST  = []
def re():
    desname= input("give a name to the file : ")
    global f
    f= open (desname,'w')
    return (f)   
def th():
    theorybox = input("write your theory further here:")
    EMPLIST.append(theorybox)
def num():
    mathbox =  "mathematical relation used or talked about in the above part : " + input("input your mathematical expression")
    EMPLIST.append(mathbox)
def nxt():
    nt = input(" 1 for providing text box for theory , 2 for providing numerical box , 3 for image box ,4 for ending the report:")
    while nt< '4':
        if nt == "1":
            th()
        elif nt == "2":
            num()
        elif nt == '3':
            imagebox = input("you can give the address to any image or video you want to shaow in your work here : ")
        nt = input(" 1 for providing text box for theory , 2 for providing numerical box , 3 for image box ,4 for ending the report:")
       if nt == "4":
        	biblio=input("bibliography :")
        	print('report has ended, thanks for working with us')
        	EMPLIST.append('report ended')
        	EMPLIST.append(biblio)
def start():
    t = input("Title/name of your project:")
    T = 'TITLE : ' + t
    EMPLIST.append(T)
    print("p for physics, c for chemistry, b for biology, m for mathematics, cs for computer science")
    global s
    s =  input("Subject under which it does come:")
    S = 'CODE OF CONCERNED SUBJECT : ' + s
    EMPLIST.append(S)
    return (S)
def password():
        inp2= int(input("input a password for your work, it will come in handy in future if you would like to   edit any thing in your work : "))
    istring = str(inp2)
    global rpassword
    rpassword = 'PASSWORD : ' + istring
    return rpassword

if a == 'R' or a == 'r':
    start()
    yourname = 'author(s)' + input('name of people who worked in this project : ') + ':'
    EMPLIST.append(yourname)
    re()
    password()
    EMPLIST.append(rpassword)    


    if s == 'p' or s == 'P' or s == 'c' or s == 'C' or s == 'm' or s == 'M':
            q = "ACCOMPLISHMENT MADE BY THE WORK: " + input("question/problem solved by your study or accomplishment made : ")
            imagebox = input("you can give the address to any image or video you want to shaow in your work here : ")
            ideabox = "INTRODUCTION: " + input("your theory's introduction: ")
            m0box = "FINAL MATHEMATICAL RELATION FOUND (if any) : " + input("you can write here if  there is any final matematical relation or derivation which your study suggests ,here  :")
            theorybox = input("write part 1 of details of your theory, you will get a mathbox below for writing any mathematical relation related to this part of thepory :")
            mathbox = "MATHEMATIAL RELATION USED OR TALKED ABOUT IN ABOVE PART : " +input("write any mathematical expression for part 1 of your theory:")
            EMPLIST.append(q)
            EMPLIST.append(imagebox)
            EMPLIST.append(ideabox)
            EMPLIST.append(m0box)  
            EMPLIST.append(theorybox)
            EMPLIST.append(mathbox)            
            nxt()            

    elif s == 'b' or s == 'B':
            q = "ACCOMPLISHMENT MADE BY THE WORK: " + input("accomplishment made by the work : ")            
            ideabox = "INTRODUCTION: " + input("your theory's introduction:")
            imagebox = input("you can give the address to any image you want to shaow in your work here : ")
            m0box = "mathematical relation which can be concluded from this study : " + input("you can write here the any mathematical relation which your work suggests, if any :")
            theorybox = input("write part 1 of details of your theory:")
            mathbox =  "mathematical relation used or talked about in the above part : " + input("write any mathematical expression for part 1 of your theory:")
            EMPLIST.append(q)
            EMPLIST.append(ideabox)
            EMPLIST.append(imagebox)
            EMPLIST.append(m0box)  
            EMPLIST.append(theorybox)
            EMPLIST.append(mathbox)            
            nxt()

    elif s == 'cs' or s == 'CS' or s == 'Cs' or s == 'cS':
            q = "ACCOMPLISHMENT MADE BY THE WORK: " + input("accomplishment made by your study : ")
            imagebox = input("you can give the address to any image you want to shaow in your work here : ")
            ideabox = "INTRODUCTION: " + input("your work's introduction:")
            m0box = "MATHEMATICAL RELATION(s) USED HERE ARE: " + input("you can write here the any mathematical relation which you have used in your work, if any :")
            theorybox = input("you will further get a mathbox for providing mathematical relation used in this part of theory . write part 1 of details of your theory:")
            mathbox = input("write any mathematical expression for part 1 of your theory:")
            EMPLIST.append(q)
            EMPLIST.append(imagebox)
            EMPLIST.append(ideabox)
            EMPLIST.append(m0box)  
            EMPLIST.append(theorybox)
            EMPLIST.append(mathbox)            
            nxt()        
    string1= '\n'.join(EMPLIST)            
    f.writelines(string1)          
    f.close()


if a == 'u' or a == 'U':
    EMPLIST.append("Updated File :")
    e = input("Name of the file you want to edit: ")
    passcode = int(input("password : "))
    passcode1= str(passcode)
    filere = open(e, 'r')    
    lines = filere.readlines()
    p = "PASSWORD : " + passcode1
    string2= '\n'.join(lines)
    if p in string2:        
        print(''.join(lines))
        linenum = int(input('The Serial no. of line you want to update: '))
        k = linenum - 1

        if k >= len(lines):
            ufile = open(e, 'a')
            t1 = int(input("How many lines you want to add: "))
            i = 0
            if i < t1 :           
                txt = input("the desired text you want to append : ") + '\n'
                ufile.write(txt)
                ufile.close()
            file = open(e, 'r')
            print(file.read())

        elif k < len(lines):
            txt = input('The new text you want at desired line: ')
            lines[k] = txt + '\n'
            ufile = open(e, 'w')
            ufile.writelines(lines)
            ufile.close()
            file = open(e, 'r')
            print(file.read())
    else:
    	print("wrong password")
