# chech whether the cahr is lower,upper,number using function 
# (hello-hfllp)write function to convert vowel char into nrxt char

def code_decode(word):
    secret= ""
    for k in range(len(word)):
        if word[k] in ['a' , 'e' , 'i' ,'o', 'u']:
            secret+=chr(ord(word[k])+1)
        else:
            secret+=word[k]
    print(secret)
code_decode("hello")
code_decode("michel jackson")