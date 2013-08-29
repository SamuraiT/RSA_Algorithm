Discription of RSA Algorithm module
==============
RSA is a python module which includes those functions: 
- generating a public-key(e,n) randomly <code> generate_public_key()</code>
- encrypting a message by public-key<code> encode() </code>
- generating a private-key(d,n) by assigning publi-key(e,n) <code>private_key()</code>
- decryptin a message by private-key<code>decode()</code>

There are other functions, including <code>LCM()</code> which stands for Least Common Multiple, <code>GCD()</code> standing for 
Greatest Common Divisor...etc

After clone my RSA Algorithm modlue, write this on terminal:
<code>pydoc -w RSA</code>. you will get *specification*

Example
----------------------
First, Generate public key(e,n)

    >>> from RSA import *
    >>> pk = generate_public_key() 
    d =  7 p =  13 q =  19
    >>> pk  #this is public key
    (31, 247)
write a message here

    >>> message = 'Hello, thank you for seeing my module and code. try to run my code! if you have any questions, comments or  sugesstions,feel free to contact me'
encode the message by public key

    >>> cipher = encode(pk,message)
cipher is a list of encoded message

    >>> cipher
    ['162', '023', '186', '186', '214', '099', '072', '155', '234', '098', '124', '107', '072', '121', '214', '052', '072', '197', '214', '114', '072', '210', '023', '023', '222', '124', '103', '072', '021', '121', '072', '021', '214', '074', '052', '186', '023', '072', '098', '124', '074', '072', '161', '214', '074', '023', '084', '072', '155', '114', '121', '072', '155', '214', '072', '114', '052', '124', '072', '021', '121', '072', '161', '214', '074', '023', '097', '072', '222', '197', '072', '121', '214', '052', '072', '234', '098', '066', '023', '072', '098', '124', '121', '072', '113', '052', '023', '210', '155', '222', '214', '124', '210', '099', '072', '161', '214', '021', '021', '023', '124', '155', '210', '072', '214', '114', '072', '072', '210', '052', '103', '023', '210', '210', '155', '222', '214', '124', '210', '099', '197', '023', '023', '186', '072', '197', '114', '023', '023', '072', '155', '214', '072', '161', '214', '124', '155', '098', '161', '155', '072', '021', '023']
make this cipher as a string

    >>> cipher = ' '.join(cipher)
    >>> cipher
    '162 023 186 186 214 099 072 155 234 098 124 107 072 121 214 052 072 197 214 114 072 210 023 023 222 124 103 072 021 121 072 021 214 074 052 186 023 072 098 124 074 072 161 214 074 023 084 072 155 114 121 072 155 214 072 114 052 124 072 021 121 072 161 214 074 023 097 072 222 197 072 121 214 052 072 234 098 066 023 072 098 124 121 072 113 052 023 210 155 222 214 124 210 099 072 161 214 021 021 023 124 155 210 072 214 114 072 072 210 052 103 023 210 210 155 222 214 124 210 099 197 023 023 186 072 197 114 023 023 072 155 214 072 161 214 124 155 098 161 155 072 021 023'
decode the cipher by generating private-key(d,n) from pk(e,n)

*cipher should be a list or string

    >>> decode_auto(pk,cipher)
    'Hello, thank you for seeing my module and code. try to run my code! if you have any questions, comments or  sugesstions,feel free to contact me'
    

