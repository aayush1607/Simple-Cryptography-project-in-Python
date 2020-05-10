#taking input message in string form from the shyam.
msg=input('enter the message: ')
s=' ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.,!@#$%^&*()=-+_*/{}?'
x=[]
d=[]
#comparing the msg with string s and converting it's each character into number form and storing it in a list-d.

for j in range(len(msg)):
     if msg[j] in s:
          q=s.index(msg[j])
          d.append(q)
#taking values of public key and N from ram:
e=int(input('enter the public key: '))
n=int(input('enter N: '))
#printing decryted text-chiper text-C
print('The decryted text of message is: ',end=' ')
for i in d:
     print((i**e)%n,end=' ')
