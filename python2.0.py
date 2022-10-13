import keyword
print (keyword.kwlist)

#data types
## these are the five fundamental data types

#1) int
a=10
print(a)
print(type(a))


#a) decimal form (base=10)
d=69
print(type(d))

#b) binary form (base=2)
b=0b1111
print(b)
print(type(b))

#c) octal form (base=8)    [only (0to7) are allowed]
c=0o2345
print(c)

#d) hexal form (base=16)     [only (0to9) ('A'to'f') are allowed]
# value of a=10,b=11, c=12 ,d=13 ,e=14,F=15
h=0xaf43
print(h)
print(type(h))



## BASE CONVERSION

#A) TO binary 
print(bin(15))
print(bin(0o545))
print(bin(0x6345decb))

#B) TO octal
print(oct(19))
print(oct(0b111111))
print(oct(0x452459abcdef))

#c) To hexal
print(hex(1234))
print(hex(0b101010))
print(hex(0o1234567))



#2) float      **[1.2e3=1.2*10^3]
f=209.57
print(type(f))
print(f)

g=1.2e3             
print(g)

#float value can only be represented in "decimal form" value and hence "binary","octal","hexal" forms are not applicable in float data types
#h=0b1.011                                                          
#i=0o123.456                                                       
#j=0x124.57                                                        
#print(type(h,i,j))         {syntax error}

#3) complex
# for real part any form of "float","octal","hexal" is applicable but for imaginary part only "decimal"form is applicable .
x=39+46.9j
print(x)        
print(type(x))

#To print real and imaginary part
print(x.real)    
print(x.imag)     

# for real part "decimal","binary","hexal","octa" any form is applicable
y=0b1111+20j     

#  for imaginary only "decimal" form is appplicable.
#z=15+0b1111j     {syntax error}                                                                                                      
print(y)     

# Arithmetic operations in complex data type
x=10+20j
y=23+334j
print(x+y)
print(x*y)
print(x/y)



#4) bool
b=True
print(b)
print(type(b))

a=20
s=29
c=a>s
d=a<s
print(c,d) 

print(True+True)
print(False+False)


#5) string
s="amartya"
print(s)
print(type(s))
print(s[3])
print(s[0:3])

ss='''amartya
          is a 
          nice guy'''
print(ss)

##case conversion     **[to convert any character of string to uppper\lower case]
s="amartya"
output=s[0].upper()+s[1:]
print(output)

#mathematic operation in string 
# [to use "+" both argument should be string type only] 
s="my"+"dog"
#d="ten"+ 10        
#print(d)        {syntax error}
print(s)

# [to use "*" both argument should be different]
f='pyhton'*3
#g="pyhton"*'tech'      
#print(g)        {syntax error}   
print(f)



