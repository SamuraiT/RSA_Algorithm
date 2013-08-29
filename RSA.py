#RSA algorithm
"""
This module provides functions 
which decode ciphers and encode messages

@author Tatsuro YASUKAWA

"""
from random import randint
from math import sqrt

########################## encoding ##############################
def generate_public_key(limit = 30):
	"""
	this function generates a public key by itself
	and returns a public key tuple:(e,n)
	
	"""
	n  = 0
	while n < 122:
		pq = generate_prime(limit)
		p = pq[0]
		q = pq[1]
		n = p * q
	k = LCM( p-1, q-1)
	rem = 0
	d = find_d(k)

	print 'd = ',d,'p = ',p,'q = ',q
	e = find_e(k,d)
	publicKey = (e,n)
	return publicKey

def find_d(k):
	"""
	find d which is coprime to k
	return d
	this function is used only for encoding.
	for decoding, see find_d_from function
	"""
	while True:
		ran = randint(2,k)
		if is_coprime(k,ran):
			d = ran
			return d


def encode(public_key, message):
	"""
	encode message by public key.
	public_key:the type is tuple. and it should be (e,n) 
	message: you want to encode 
	return encoded list of numbers
	"""
	if not isinstance(public_key,tuple):
		print 'assign tuple type public key. it should be this: (e,n) \n  e: int type, n:int type(n = p * q) '
		return ''
	encoded = ''
	encoded_list = []
	e = public_key[0]
	n = public_key[1]
	for letter in message:
		code = ord(letter)
		code = ( code ** e ) % n
		encoded_list.append( str(code).zfill(3)  )
		#encoded  += chr( int( code ) )
	return encoded_list

def find_e(k,d):
	"""
	find e that satisfies this expression:
	ed = 1(mod k)
	e = (k*Q + 1)/ d
	mod: is same as %	
	k: k =  LCM(p -1, q-1) where p and q are different prime number
	d: d is decode number and is coprime to k
	return e
	"""
	Q = 1 #quotient
	while True:
		e = (k*Q + 1) % d
		if e == 0:
			return (k*Q +1)/d
		Q += 1
	
		


def LCM(p,q):
	"""
	find  Least Common multiple of 
	p and q
	return least common multiple (lcm)
	"""
	div = 2
	t = []
	lcm = 1
	while not( p == 1 and q == 1 ):
		if p % div == 0 and q % div == 0:
			p /= div
			q /= div
			t.append(div)
		elif p % div == 0:
			p/= div
			t.append(div)
		elif q % div == 0:
			q /= div
			t.append(div)
		else:
			div += 1
	for num in t:
		lcm *= num
	return lcm
	
def GCD(n,m):
	"""
	find Greatest common divisor
	of n and m
	"""
	if not m >= n:
		temp = m
		m = n
		n = temp
	
	while not n  == 0:
		rem = m % n
		m = n
		n = rem
	return m

def is_coprime(n,m):
	"""
	return True if n and m are coprime,
	False otherwise
	"""
	return GCD(n,m) == 1


def generate_prime(limit = 30):
	"""
	generate a prime number ranging from 2 to limit
	limit: the max of range. you can change this
	
	return a random prime number between 2 and limit

	"""
	pq = []
	while not len(pq) == 2:
		ran =  randint(2,limit)
		if is_prime( ran ):
			if len(pq) ==1:
				if not ran == pq[0]:
					pq.append(ran)
			else:
				pq.append(ran)
	return pq
				

def is_prime(n):
	"""
	return True if n is a prime, 
	False otherwise
	"""
	for i in range(2,n):
		if (n % i ==0 )  and ( n != i):
			return False
	return True

################### decoding ################################
def mod(en,num):
	"""
	calculate this expression:

	code = num^2 (mod n)

	en: is turple which contains e and n
	num: a number you wanna calculate 
	"""
	return (num**en[0])%en[1]


def decode(decode_key,cipher):
	"""
	decode each cipher by decode key.
	decode_key: tuple type: (d,n)
	cipher: a encoded list of numbers 
	return decoded message
	"""
	if not isinstance(decode_key,tuple):
		print 'assign tuple type deocde key. it should be this: (d,n) \n d: int type, n:int type(n = p * q) '
		return ''
	if isinstance(cipher,str):
		cipher = cipher.split()
	#decoded_list = encode( decode_key, cipher )
	message = ''
	for item in cipher:
		code = mod(decode_key, int(item) )
		message += chr( code )
	return message

def private_key( public_key ):
	"""
	find private key (d) from publci key (e)
	public_key: (e,n) 
	"""
	e = public_key[0]
	n = public_key[1]
        d = find_d_from( PFD(n),e )
	return d,n

def decode_auto( public_key, cipher ):
	"""
	decode ciphers automatically by using public key:(e,n)
	and return decoded message
	public_key: (e,n)
	cipher: cipher list(should be like this: ['123','456',....])
		but also, accept string like tis: 123 456 789 ....
	"""
	decode_key = private_key(public_key)
	return decode( decode_key, cipher)
	


def find_d_from(pq,e):
	"""
	find d for decode by calculating this: 
	d = ( k*Q +1 )/ e
	pq:turple of p and q
	e: encoding key
	Q:quotient
	"""
	p = pq[0]
	q = pq[1]
	k = LCM(p-1,q-1)
	d = find_e(k,e)
	return d

def PFD(n):
	"""
	prime factor decomposition
	return prime factor of n
	n: a number 
	"""
	root_n = int ( sqrt(n))
	for q in range(2,root_n):
		rem = n % q
		if rem == 0 and is_prime(q):
			p = n / q
			if is_prime(p):
				return ( p , q )
	raise ValueError,'cannot find primes'



if __name__ == '__main__':
	while True:
		enter = raw_input("what would you like to do? decode or encode? \n (Enter d or e, quit: q ): ")
		#encoding
		if enter == 'e':
			g_or_e  = raw_input('would you like to generate publick key( g ) or you\'d just encode( e ): ')
			if g_or_e == 'g':
				limit = raw_input('Enter the range of prime numbers(p and q): ')
				print
				public_key = generate_public_key( int( limit) )
				print '(e,n) = ',public_key,'\n'
			elif g_or_e == 'e':
				public_key = raw_input('Enter a public_key like this: (e,n) ')
				public_key = eval(public_key)
				if not isinstance(public_key,tuple):
					print 'you have to Enter tuple type: (e,n)'
					break
			message = raw_input('Enter a message you\'d like to encode: ')
			t =  encode(public_key,message)
			print
			print ' '.join(t),'\n'
		#decoding
		elif enter == 'd':
			enter = raw_input("Do you know private key ? (y or n): ")
			if enter == 'y':
				decode_key = eval( raw_input('Enter private key like this: (d,n): ')	 )
				if not isinstance(decode_key,tuple):
					print 'you have to Enter tuple type: (e,n)'
					break
			if enter == 'n':
				public_key = eval(raw_input('Enter public key like this:(e,n): '))
				if not isinstance(public_key,tuple):
					print 'you have to Enter tuple type: (e,n)'
					break
				decode_key = private_key(public_key)
			cipher = raw_input('Enter a cipher: ')
			cipher = cipher.split()
			mes = decode(decode_key, cipher)
			print
			print mes,'\n'
		#quit
		elif enter == 'q':
			print
			print 'good bye'
			break

	


			

		
