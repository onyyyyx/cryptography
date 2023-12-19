def crypt():
    alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"*2
    text=input("Text to crypt :\n> ")
    crypted,key="",input("Starting key:\n> ")
    for i in text:
        if i.islower(): crypted+=alpha[alpha.find(i.upper())+key%len(alpha)].lower()
        elif i.isupper(): crypted+=alpha[alpha.find(i.upper())+key%len(alpha)].upper()
        else:
            crypted+=i
            key-=1
        key+=1
    print("\n",crypted)

def decrypt():
    alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"*2
    crypted=input("Text to decrypt:\n> ")
    text,key="",input("Starting key:\n> ")
    for i in text:
        if i.islower(): text+=alpha[alpha.find(i.upper())+key%len(alpha)].lower()
        elif i.isupper(): text+=alpha[alpha.find(i.upper())+key%len(alpha)].upper()
        else:
            text+=i
            key-=1
        key+=1
    print("\n",crypted)
