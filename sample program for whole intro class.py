#!/usr/bin/env python
# coding: utf-8

# In[2]:


#helloworld programing
print('hello world')


# In[15]:


#varable
a=10
print(a)


# In[4]:


#list of variable and data structure
a=[10,12,14,16,18]
print(a)


# In[13]:


#data types
#int,string,float,compex
#integer
a=12
print(a,type(a))


# In[17]:


#string
a=('hello')
print(a,type(a))


# In[5]:


#integer to string
a=('12')
print(a,type(a))


# In[6]:


#float 
a=10.5
print(a,type(a))


# In[20]:


#boolean program 
#true or false
a=10
b=25
print(a<b,type(a<b))
print(a>b)


# In[103]:


#complex
#j means imaginery part
a=34+22
b=24+7j
print(a+b,type(a+b))
print(b.real)
print(b.imag)
print(a.real,a.imag)


# In[23]:


#operators
#ternary,arithamatic,logic,binary,identity,compereision,membership,assignment
#arithmaric operators
#add,mul,sub,div
#add 
a=10
b=20
c=a+b
print(c)


# In[24]:


#mul
a=10
b=23
c=a*b
print(c)


# In[25]:


#sub
a=56
b=75
c=a-b
print(c)


# In[27]:


#div
a=256.5
b=123
c=a/b
print(c)


# In[44]:


#logical operator
#and,or,not
#and
a=True
b=False
print(a and b)


# In[45]:


#or
a=55
b=99
print(a or b)


# In[43]:


#not
a=True
b=False
print(a or b)


# In[46]:


#binary operators
a=10
print(bin(a))


# In[56]:


#ternary operators
c,d=20,55
minimum=c if c<d else d
print(minimum)
maximum=c if c>d else d
print(maximum)


# In[61]:


#comparision operator
a1=20
a2=35
print(a1>a2)
print(a1<a2)
print(a1==a2)
print(a1>=a2)
print(a1<=a2)


# In[70]:


#identity operator
#is or is not
a=["naruto","uzumaki"]
b=a
print(a is b) 
print(a is not b)
print(type(a),type(b))


# In[77]:


#membership operator
#in,not in'
a=["hinata","sakura"]
string="naruto"
print('a' in string)
print("hinata" in a)
print(string not in 's')
print("hinata" in string)


# In[50]:


#assignment operators
a=30
b=11
print(a > b)
print(a < b)
print(a == b) 
print(a <= b)
print(a>=b)


# In[7]:


#list
value =[ 1,2,3,4,5,6,7,8,9,0]
print(value)


# In[23]:


#tuple
value =["20","25","35","30"]
print(len(value))
b=len(value)
print(b,type(b),type(value))


# In[48]:





# In[83]:


#power operator
pow(2,5)
print(pow(2,5))


# In[87]:


#escape operator
a=(2//5)
print(a,type(a))
print(a)


# In[97]:


#modulus operator
a=-10
b=6
print(a % b )
print(b % a)


# In[2]:


val1 =int(input())
val2 =int(input())
print(val1 + val2)
print(val1)
print(val2)


# In[ ]:





# In[ ]:


#identify function and print function
a=10
b=20
print(id(a),id(b), sep='')
print(a,b,sep='\n')
print(a,b,sep='\t')


# In[126]:


#data type convertion 
#int to float,string,bool
#float to int,string,bool
#string to int, float, bool
#bool to int,float,string

'int to float,string,bool'
x=3
y=float (x)
z=str(x)
a=bool(x)
print(type(x),type(y),(y),sep='\n')
print(type(x),type(z),(z),sep='')
print(type(x),type(a),(a),sep='')


# In[127]:


'float to int,string,bool'
x=3.5
y=str(x)
z=int(x)
a=bool(x)
print(type(x),type(y),(y))
print(type(x),type(z),(z))
print(type(x),type(a),(a))


# In[128]:


'string to float,int,bool'
x=a
y=float(x)
z=int(x)
a=bool(x)
print(type(x),type(y),(y))
print(type(x),type(z),(z))
print(type(x),type(a),(a))


# In[129]:


'bool to float,string,int'
x=True
y=str(x)
z=int(x)
a=float(x)
print(type(x),type(y),(y))
print(type(x),type(z),(z))
print(type(x),type(a),(a))


# In[ ]:




