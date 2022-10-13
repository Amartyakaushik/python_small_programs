#import keyword
#print (keyword.kwlist)

#data types
## these are the five fundamental data types

#1) int
#a=10
#print(a)
#print(type(a))


 #a) decimal form (base=10)
#d=69
#print(type(d))

 #b) binary form (base=2)
#b=0b1111
#print(b)
#print(type(b))

 #c) octal form (base=8)    [only (0to7) are allowed]
#c=0o2345
#print(c)

 #d) hexal form (base=16)     [only (0to9) ('A'to'f') are allowed]
# a=10,b=11, c=12 ,d=13 ,e=14,F=15
#h=0xaf43
#print(h)
#print(type(h))



## BASE CONVERSION

 #A) TO binary 
#print(bin(15))
#print(bin(0o545))
#print(bin(0x6345decb))

 #B) TO octal
#print(oct(19))
#print(oct(0b111111))
#print(oct(0x452459abcdef))

 #c) To hexal
#print(hex(1234))
#print(hex(0b101010))
#print(hex(0o1234567))



#2) float
#f=209.57
#print(type(f))
#print(f)
#g=1.2e3             **[1.2e3=1.2*10^3]
#print(g)
#h=0b1.011
#i=0o123.456
#j=0x124.57
#print(type(h))   **float value can only be represented in "decimal form" value and hence "binary","octal","hexal" forms are not applicable in float data types.

#3) complex
#x=39+46.9j
#print(x)         **for real part any form of "float","octal","hexal" is applicable but for imaginary part only "decimal"form is applicable .
#print(type(x))
#print(x.real)    ** To print real part
#print(x.imag)    ** To print imaginary part
#y=0b1111+20j     ** for real part "decimal","binary","hexal","octa" any form is applicable.
#z=15+0b1111j     **syntax error
#print(y,z)      ** for imaginary only "decimal" form is appplicable.

## Arithmetic operations in complex data type
#x=10+20j
#y=23+334j
#print(x+y)
#print(x*y)
#print(x/y)



#4) bool
#b=True
#print(b)
#print(type(b))
#a=20
#s=29
#c=a>s
#d=a<s
#print(c,d) 
#print(True+True)
#print(False+False)


#5) string
#s="amartya"
#print(s)
#print(type(s))
#print(s[3])
#print(s[0:3])
#ss='''amartya
#          is a 
#          nice guy'''
#print(ss)

##case conversion     **[to convert any character of string to uppper\lower case]
#s="amartya"
#output=s[0].upper()+s[1:]

#mathematic operation in string 
#s="my"+"dog"
#d='ten'+10              ** [to use "+" both argument should be string type only]
#f='pyhton'*3
#g="pyhton"*'tech'       **[to use "*" both argument should be different]
#print(s,d,f,g)



#Type casting \type coersion

# i) float to int 
#i=int(10.4545)
#print(i)

##complex to int 
#i=int(10+12j)
#j=int(10.5+13j)
#print(i)                  **complex data types can't be converted into int #syntax error
#print(j)
            
##bool to int 
#i=int(True)
#j=int(False)
#print(i,j)

##str to int
#i=int("12")
#j=int('0b1111')         **syntax error {string must contain "integeral" value and "base 10" only}
#k=int("1323.3")         ** value error     
#print(i,j,k)


# ii) Int To Bool
#f=bool(10)
#g=bool(0)
#h=bool(-12)
#print(f,g,h)

## float To Bool
#f=bool(10.5)
#g=bool(0.0)
#h=bool(0.0005)
#print(f,g,h)

## complex To Bool
#f=bool(10+25j)
#g=bool(0+0j)
#h=bool(0+5j)
#print(f,g,h)

## string To Bool
#f=bool("amar")
#g=bool('True')
#h=bool('False')
#i=bool("None")
#j=bool('')          **{false only in empty string type}
#print(f,g,h,i,j)


#iii) int to float 
#f=float(344)
#g=float(0b1111)
#h=float(0xfaced)
#i=float(0o2346)
#print(f,g,h,i)


## bool to float 
#f=float(True)
#g=float(False)
#print(f,g)

##complex to float
 #syntax error [complex data types can't be converted into float]

 ##string to float
#f=float("10")
#g=float("20.6")       **{string should contain "int" and "float" value only }
#h=float("0xadef")     ** value error
#i=float("0o567")      ** value error
#print(f,g,h,i)
 

## other type to complex

##form 1; complex(x)
#int to complex
#a=complex(10)
#s=complex(0b1111)
#d=complex(0xcdef)
#f=complex(0o4567)
#print(a,s,d,f)

#float to complex
#a=complex(10.5)
#s=complex(0)
#print(a,s)

#bool to complex
#a=complex(True)
#s=complex(False)
#print(a,s)

#string to complex
#a=complex("20")           ** string should contain 'int' of base 10 and 'float' value only
#s=complex("32.4")   
#print(a,s)

##form 2; complex(x,y)
#a=complex(10,20)
#s=complex(10.5,45.34)
#d=complex("10","20")
#f=complex(10,"20")
#print(a,s,d,f)



