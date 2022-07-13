##################################################
#Globale varibales
##################################################
PC1=[57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36, 63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]
PC2=[14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]
shift_table=[ 1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1 ]
E=[32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]
PI=[58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8, 57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3, 61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]
IP_1=[40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31, 38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29, 36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27, 34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25]
P=[16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10, 2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]
S1=[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7, 0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8, 4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0, 15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
S2=[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10, 3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5, 0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15, 13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
S3=[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8, 13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1, 13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7, 1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
S4=[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15, 13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9, 10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4, 3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
S5=[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9, 14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6, 4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14, 11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
S6=[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11, 10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8, 9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6, 4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
S7=[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1, 13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6, 1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2, 6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
S8=[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7, 1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2, 7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8, 2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]

#################################################################
#General function
#################################################################

####################Convertion functions#########################

def convertHexaBinair(k,bits):
    return format(int(k, 16), "0"+str(bits)+"b")

def convertDicimalToBinair(k,bits):
    binNumber=bin(int(k))[2:]
    while len(binNumber) < bits:
        binNumber = '0' + binNumber
    return binNumber

def convertBinairToHexa(k):
    decimal_representation = int(k, 2)
    hexadecimal_string = hex(decimal_representation)
    return hexadecimal_string[2:]

def convertirDecimale(numberstr):
    puissance=len(numberstr)-1
    number=0
    for i in numberstr:
        number=number+int(i)*(2**puissance)
        puissance=puissance-1
    return number

def completWith0(msg):
    if len(msg)%16!=0:
        while len(msg)%16!=0:
            msg =msg+ '0' 
    print(msg)
    return msg

def completWith0Left(msg):
    if len(msg)%16!=0:
        while len(msg)%16!=0:
            msg ='0'+msg  
    return msg


####################Permutation function############################

def permutation_bits(message,convertion_rule):
    convertion_message=''    
    for i in convertion_rule:
        convertion_message=convertion_message + message[i-1]
    return convertion_message

####################Divise message functions########################

def separatemessage(M):
    L=M[:int(len(M)/2)]
    R=M[int(len(M)/2):]
    return L, R


######################################################################
#Apllique S-Box in block 6->4
######################################################################


def SBox(message,s):
    lign=message[0]+message[-1]
    column=message[1:-1]
    return convertDicimalToBinair(s[convertirDecimale(lign)*16+convertirDecimale(column)],4)

def switchS(s):
    match s:
        case "S1":
            return S1
        case "S2":
            return S2
        case "S3":
            return S3
        case "S4":
            return S4
        case "S5":
            return S5
        case "S6":
            return S6
        case "S7":
            return S7
        case "S8":
            return S8


def GlobalSBox(message):
    blocks=[]
    for i in range(1,9):
        blocks.append(message[(i-1)*6:i*6])
    for i in range(1,9):
        blocks[i-1]=SBox(blocks[i-1],switchS("S"+str(i)))
    return "".join(blocks)


######################################################################
#Exponssion E of message M
######################################################################
def expanssionE(MesgRight):
    return permutation_bits(MesgRight,E)


#####################################################################
#Applix XOR between two nubre binaire 
#####################################################################
def XORFunction(n1,n2):
    return '{}'.format(format(int(bin(int(n1,2) ^ int(n2,2))[2:],2),"0"+str(len(n1))+"b"))


#####################################################################
#Generate 16 Keys from One key 
#####################################################################

def decalage(ls):
    ls=ls[1:]+ls[0]
    return ls

def generateKeys_16(k):
    keys_16_genereted={}
    L,R=separatemessage(permutation_bits(k,PC1))
    for i in range(1,17): 
        for j in range(shift_table[i-1]):
            L,R=decalage(L),decalage(R)     
        keys_16_genereted["K"+str(i)]=permutation_bits(L+R,PC2)
    return keys_16_genereted



#####################################################################
# Encryption Function E_XOR_Key_S_P_app()
#####################################################################
def E_XOR_Key_S_P_app(elment,key):
    elment=GlobalSBox(XORFunction(expanssionE(elment),key))
    return permutation_bits(elment,P)


#####################################################################
# DES CHIFFREMENT ALGORITHM 
#####################################################################

def DES(msg,k):
    msg=convertHexaBinair(msg,64)
    k=convertHexaBinair(k,64)
    keys_16_genereted=generateKeys_16(k)
    messgPassePI=permutation_bits(msg,PI)
    L,R=separatemessage(messgPassePI)
    for i in range(1,17):
        temp=R
        R=XORFunction(L,E_XOR_Key_S_P_app(R,keys_16_genereted["K"+str(i)]))
        L=temp
   
    messgPasseIP_1=permutation_bits(R+L,IP_1)
    return convertBinairToHexa(messgPasseIP_1).upper()

#####################################################################
# DES DECHIFFREMENT ALGORITHM 
#####################################################################

def DDES(msg,k):
    msg=convertHexaBinair(msg,64)
    k=convertHexaBinair(k,64)
    keys_16_genereted=generateKeys_16(k)
    messgPassePI=permutation_bits(msg,PI)
    L,R=separatemessage(messgPassePI)
    for i in range(1,17):
        temp=R
        R=XORFunction(L,E_XOR_Key_S_P_app(R,keys_16_genereted["K"+str(17-i)]))
        L=temp
    messgPasseIP_1=permutation_bits(R+L,IP_1)
    messgPasseIP_1=completWith0Left(convertBinairToHexa(messgPasseIP_1).upper())
    return messgPasseIP_1


##############################################################################
#CHIFFRER PAR DES 
##############################################################################
def chiffrerText(message,k):
    GlobalemessageChifree=""
    message=completWith0(message)
    for i in range(int(len(message)/16)):
        GlobalemessageChifree=GlobalemessageChifree+DES(message[16*i:16*(i+1)],k)
    return GlobalemessageChifree


##############################################################################
#DECHIFFRER PAR DES 
##############################################################################
def DechiffrerText(message,k):
    GlobalemessageChifree=""
    message=completWith0(message)
    for i in range(int(len(message)/16)):
        GlobalemessageChifree=GlobalemessageChifree+DDES(message[16*i:16*(i+1)],k)
    return GlobalemessageChifree




##############################################################################
# Exemple D'application
##############################################################################

# message en clair:0123456789ABCDEF 
# cle:133457799BBCDFF1
# message chiffre DES:85E813540F0AB405



