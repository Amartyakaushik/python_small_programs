##Type casting \type coersion

#i) float to int 
i=int(10.4545)
print(i)

#complex to int 
#{complex data types can't be converted into int}                  
            
#bool to int 
i=int(True)
j=int(False)
print(i,j)

#str to int
#value error     
i=int("12")
#j=int('0b1111')           #syntax error {string must contain "integeral" value and "base 10" only}        
#k=int("1323.3")        
print(i)



# ii) Int To Bool
f=bool(10)
g=bool(0)
h=bool(-12)
print(f,g,h)

# float To Bool
f=bool(10.5)
g=bool(0.0)
h=bool(0.0005)
print(f,g,h)

# complex To Bool
f=bool(10+25j)
g=bool(0+0j)
h=bool(0+5j)
print(f,g,h)

# string To Bool
f=bool("amar")
g=bool('True')
h=bool('False')
i=bool("None")
j=bool('')        ##false only in empty string type}
print(f,g,h,i,j)



# iii) int to float 
f=float(344)
g=float(0b1111)
h=float(0xfaced)
i=float(0o2346)
print(f,g,h,i)

# bool to float 
f=float(True)
g=float(False)
print(f,g)

##complex to float
# [complex data types can't be converted into float]

##string to float
f=float("10")
g=float("20.6")        # {string should contain "int" and "float" value only }
#h=float("0xadef")      # value error
#i=float("0o567")       # value error
print(f,g,h,i)
 


# other type to complex

#form 1; complex(x)
#int to complex
a=complex(10)
s=complex(0b1111)
d=complex(0xcdef)
f=complex(0o4567)
print(a,s,d,f)

#float to complex
a=complex(10.5)
s=complex(0)
print(a,s)

#bool to complex
a=complex(True)
s=complex(False)
print(a,s)

#string to complex
a=complex("20")            #** string should contain 'int' of base 10 and 'float' value only
s=complex("32.4")   
print(a,s)


#form 2; complex(x,y)
a=complex(10,20)
s=complex(10.5,45.34)
#d=complex("10","20")     # type error {if 1st argument is string then can't take 2nd argument}
#f=complex(10,"20")      # type error {2nd argument should never be string}
print(a,s,d,f)







