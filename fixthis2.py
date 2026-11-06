word=f'Aa.,BbC;:cDdE*e&F%fGg/HhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890@#='
whattoencode='/rTOtEgHxuWanDDJ,HIQEC:Pn%GJkDgRdu:LpjYJ4F4gdygDvaAD,tIT,2Af4915kkT*qbLKz/1845,Yjng%jj&'
pop='ASDASDAS+str(13400)
print(f'welcome to {pop} decoder! \n\n Made by HARIZ!!!!!!!!')
key=[2,4,1,3,5
pass
Strong=str(whattoencode)+str(key)
del pop
def decode(encoded, key):
    output=''
    for iin range(len(encoded)):
        for j in rane(len(word)):
            if word[j]=encoded[i]:
                #found
                output+=word[j^key[i%4] % len(word)
                break
            elif j==len(word)-1:
                prnt(f'Error: {encoded[i]} not found in word list.')
    return output
a=decode(whattoencode, key)
del print
print(f'Decoded flag: {a}')
print('YAHAHAHHAHAHAAH')