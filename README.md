It is a simple cryptography project involving a little maths.
The topics involved:
Euler's totent function-https://en.wikipedia.org/wiki/Euler%27s_totient_function
RSA-Algorithm-https://simple.wikipedia.org/wiki/RSA_algorithm

How it works?
Suppose a sender wants to send a message. So he will notify his receiver.

The receiver will choose any two prime numbers. The larger is the prime number larger is the security.
why?
because we are using euler totent function. With that for very large prime numbers choosen the hacker might take 1000's of years to crack your message.

He will be then given multiplication of those two prime numbers selected and a also another number which is a public key.
So he can make this key public. No matter who gets it No other person other than he intends can crack his message.
How?
The logic is that he will not be giving those two prime numbers to anyone and keep ot safe.
In order to find the private key using which the encrypted text can be decrypted without knowing those two large prime numbers and only their multiplication,even a most powerful computer can take 1000's of years.

Now using the value e-public key the sender will encrypt thier message-
how?
formula is pow(A[i],e)%N where A[i] is each character of message string, e is public key and N is multiplication of those large prime numbers.

After receiving the encrypted message it can be decrypted as follows-
we will take euler totent fxn phi(x)= (p-1) * (q-1)
using this phi fxn we will find private key and then use it to decrypt the message.Here some mathematical calculations are involved.

So finding the phi function without which the message cannot be decrypted is near to impossible without knowing those large prime numbers which can be changed everytime by users.


How it is different and more safe then other algorithm?
Here the risk of leak of private key by hacker or someone is nil as it not given to anyone in the process. No-one neither receiver nor sender knows the private key. 
