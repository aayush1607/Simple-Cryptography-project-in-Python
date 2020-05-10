#defining gcd function for further use.
def gcd(a,b): 
    if b==0: 
        return a 
    else: 
        return gcd(b,a%b)

s=[]
x=0
v=' ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.,!@#$%^&*()=-+_*/{}?'
#taking two large prime numbers from ram:
p=int(input('enter p a large prime no. '))
q=int(input('enter q a large prime no. '))
n=p*q
print('N is: ',n)
#taking phi function as f.As p and q are prime numbers f=(p-1)*(q-1): 
f=(p-1)*(q-1)
#finding suitable e as 1<e<f and e should be coprime with f:
for e in range(2,f): 
    if gcd(e,f)== 1: 
        break
print('The public key is: ',e)
#taking the cipher text from ram which is provided by Shyam;
c=input('Enter the cipher text: ')
l=(c.split())
#finding the private key-d.
for i in range(1,10): 
    x = 1 + i*f 
    if x % e == 0: 
        d = int(x/e)
        break
print('private key is: ',d)

w=[]
k=[]
u=''
for i in l:
     m=(int(i)**d)%n
     k.append(m)

for i in k:
     for j in range(len(v)):
          if i==j:
               u=u+v[j]
print(u)
          
