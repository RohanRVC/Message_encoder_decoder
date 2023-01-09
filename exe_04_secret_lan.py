import random as r

def Random_chose_words():
    alpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","y","z"]
    a=r.choice(alpha)
    for i in range(2):
        b=r.choice(alpha)
        a=a+b
    return a

def encode_message(words):

    lis=words.split(" ")   
    new_lis=[]
    for i in range(len(lis)):
        aa=lis[i]
        a=aa.lower()

        if len(a)>=3:
            removed_value=a[0]
            new_word=a.replace(a[0],"",1)+removed_value
            
            new= Random_chose_words() +new_word + Random_chose_words()
            new_lis.append(new)
        elif len(a)==1 or len(a)==2:
        
            removed_value=a[0]
            
            new_word=a.replace(a[0],"",1)+removed_value
            new=new_word 
            new_lis.append(new)
        else:
            pass
    return " ".join(new_lis)


def decode_message(text):
    lis=text.split(" ")
    decode_text=[]

    for i in range(len(lis)):
        aa=lis[i]

        if len(aa)>=3:

            word=aa[3:-3]
            last_word=word[-1]
            wordss=last_word+word
            decode_text.append(wordss[:-1])
        elif len(aa)==2:
            last_word=aa[-1]
            wordss=last_word+aa[0]
            decode_text.append(wordss)
        elif len(aa)==1:
            decode_text.append(aa)
            pass
    return " ".join(decode_text)

message="Hi there , this is an encoded message ! "

text=encode_message(message)
print(text)

final_message=decode_message(text)

print(final_message)

# aaa="Rohan"
# print(aaa[2:-2])


# print('🐔'<'🥚')