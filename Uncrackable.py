##################################################################################################################################################
#   __    __    _____      __     ______    ________     __________     ______    __    ___   __________    _________    __          _______     #
#  |  |  |  |  |     \    |  |   /   ___\  /   ___  \   /   ____   \   /   ___\  |  |  /  /  /   ____   \  /   ____  \  |  |        |  _____|    #
#  |  |  |  |  |  |\  \   |  |  /   /      |  |___|  |  |   |__|   |  /   /      |  | /  /   |   |__|   |  |  |____| |  |  |        |  |____     #
#  |  |  |  |  |  | \  \  |  | |   |       |   _____/   |  ______  | |   |       |  |/  /    |  ______  |  |  _______/  |  |        |       |    #
#  |  |  |  |  |  |  \  \ |  | |   |       |   __  \    |  |    |  | |   |       |  |\  \    |  |    |  |  |   ____  \  |  |        |  _____|    #
#  |  |__|  |  |  |   \  \|  |  \   \____  |  |  \  \   |  |    |  |  \   \____  |  | \  \   |  |    |  |  |  |____| |  |  |_____   |  |____     #
#   \______/   |__|    \_____|   \______/  |__|   \__\  |__|    |__|   \______/  |__|  \__\  |__|    |__|  \_________/  |________|  |_______|    #
#                                                                                                                                                #
#  This programe is realised by nalili.                                                                     Contact me : nalili0000007@gmail.com #
##################################################################################################################################################
# information:            #
#       Version: V1.0     #
#       Date: 12/31/2019  #
###########################  


import random

def random_number(nomber, dificulty): 
    list_random=[]
    for loop in range(nomber):
        if dificulty==0:
            list_random.append(round(random.uniform(0, 52))) #a,b,c[...]X,Y,Z
        elif dificulty==1:
            list_random.append(round(random.uniform(0, 62))) #a,b,c[...]7,8,9
        elif dificulty==2:
            list_random.append(round(random.uniform(0, 100))) #a,b,c[...]?,;,.  # \ is impossible beacause ("\") is impossible
    return list_random

def change(rn):
    password=[] #Defined password 
    for loop in range(len(list_random)):
        test=rn.pop(0)
        if test>=1 and test<=50: #Optimisation
            if test>=1 and test<=10: #Optisation 
                if test==1:
                    password.append("a")
                elif test==2:
                    password.append("b")
                elif test==3:
                    password.append("c")
                elif test==4:
                    password.append("d")
                elif test==5:
                    password.append("e")
                elif test==6:
                    password.append("f")
                elif test==7:
                    password.append("g")
                elif test==8:
                    password.append("h")
                elif test==9:
                    password.append("i")
                elif test==10:
                    password.append("j")
            elif test>=11 and test<=20: #Opti
                if test==11:
                    password.append("k")
                elif test==12:
                    password.append("l")
                elif test==13:
                    password.append("m")
                elif test==14:
                    password.append("n")
                elif test==15:
                    password.append("o")
                elif test==16:
                    password.append("p")
                elif test==17:
                    password.append("q")
                elif test==18:
                    password.append("r")
                elif test==19:
                    password.append("s")
                elif test==20:
                    password.append("t")
            elif test>=21 and test<=30: #...
                if test==21:
                    password.append("u")
                elif test==22:
                    password.append("v")
                elif test==23:
                    password.append("w")
                elif test==24:
                    password.append("x")
                elif test==25:
                    password.append("y")
                elif test==26:
                    password.append("z")
                elif test==27:
                    password.append("A")
                elif test==28:
                    password.append("B")
                elif test==29:
                    password.append("C")
                elif test==30:
                    password.append("D")
            elif test>=31 and test<=40:
                if test==31:
                    password.append("E")
                elif test==32:
                    password.append("F")
                elif test==33:
                    password.append("G")
                elif test==34:
                    password.append("H")
                elif test==35:
                    password.append("I")
                elif test==36:
                    password.append("J")
                elif test==37:
                    password.append("K")
                elif test==38:
                    password.append("L")
                elif test==39:
                    password.append("M")
                elif test==40:
                    password.append("N")
            elif test>=41 and test<=50:
                if test==41:
                    password.append("O")
                elif test==42:
                    password.append("P")
                elif test==43:
                    password.append("Q")
                elif test==44:
                    password.append("R")
                elif test==45:
                    password.append("S")
                elif test==46:
                    password.append("T")
                elif test==47:
                    password.append("U")
                elif test==48:
                    password.append("V")
                elif test==49:
                    password.append("W")
                elif test==50:
                    password.append("X")
        else: 
            if test>=51 and test<=60:            
                if test==51:
                    password.append("Y")
                elif test==52:
                    password.append("Z")
                elif test==53:
                    password.append("0")
                elif test==54:
                    password.append("1")
                elif test==55:
                    password.append("2")
                elif test==56:
                    password.append("3")
                elif test==57:
                    password.append("4")
                elif test==58:
                    password.append("5")
                elif test==59:
                    password.append("6")
                elif test==60:
                    password.append("7")
            elif test>=61 and test<=70:
                if test==61:
                    password.append("8")
                elif test==62:
                    password.append("9")
                elif test==63:
                    password.append("&")
                elif test==64:
                    password.append("é")
                elif test==65:
                    password.append("\"")
                elif test==66:
                    password.append("#")
                elif test==67:
                    password.append("'")
                elif test==68:
                    password.append("{")
                elif test==69:
                    password.append("[")
                elif test==70:
                    password.append("-")
            elif test>=71 and test<=80:
                if test==71:
                    password.append("|")
                elif test==72:
                    password.append("è")
                elif test==73:
                    password.append("`")
                elif test==74:
                    password.append("_")
                elif test==75:
                    password.append("ç")
                elif test==76:
                    password.append("^")
                elif test==77:
                    password.append("à")
                elif test==78:
                    password.append("@")
                elif test==79:
                    password.append(")")
                elif test==80:
                    password.append("]")
            elif test>=81 and test<=90:
                if test==81:
                    password.append("=")
                elif test==82:
                    password.append("}")
                elif test==83:
                    password.append("¨")
                elif test==84:
                    password.append("$")
                elif test==85:
                    password.append("£")
                elif test==86:
                    password.append("¤")
                elif test==87:
                    password.append("ù")
                elif test==88:
                    password.append("%")
                elif test==89:
                    password.append("*")
                elif test==90:
                    password.append("µ")
            elif test>=91 and test<=100: 
                if test==91:
                    password.append("!")
                elif test==92:
                    password.append("§")
                elif test==93:
                    password.append(":")
                elif test==94:
                    password.append("/")
                elif test==95:
                    password.append(";")
                elif test==96:
                    password.append(".")
                elif test==97:
                    password.append(",")
                elif test==98:
                    password.append("?")
                elif test==99:
                    password.append(">")
                elif test==100:
                    password.append("<")
    return password

def correction(list_letter):
    list_letter0=""
    for loop in range(len(list_letter)):
        x=list_letter.pop(0)
        list_letter0+=x 
    return list_letter0

print("How many characters should your password contain?")
i0=int(input(">>> "))
print("Which security level would you like for your password")
print("0 (Easy) : Only a letters")
print("1 (Medium) : A letters and a numbers")
print("2 (Hard) : A letters, a numbers and specials caracter")
i1=int(input(">>> "))

list_random=random_number(i0, i1)
list_letter=change(list_random)
pw0=correction(list_letter)

print(pw0)
input("Puss ENTER for close the program")