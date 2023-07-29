#!/usr/bin/env python
# coding: utf-8

# In[5]:


PI= 3.14
radius=float(input("please enter the radius of a circle:"))
area = PI * radius * radius
circumference = 2 * PI *radius
print("the Area of circle with  PI {1} and  radius {0} is {2} ".format(PI , radius ,int(area)))


# In[16]:


length = 10
breadth = float(input("please enter breadth (float value): "))
Area = length * breadth
perimeter = 2 * (length + breadth)
print("the Area of rectangle with breadth {1} and length {0} is {2} ".format(length, breadth,int(Area)))#indexing
area=int(area)
print(type(area))


# In[24]:


PI=3.14
height=float(input("plese enter the height in float value:"))
radius=float(input("please enter the radius of a cone:"))
cone = PI * radius * radius * height
print("volume of the cone ="+str(cone))
print("the volume of cone with height {1} and radius {0} is {2} ".format(height, radius,int(Area)))


# In[26]:


#(p*R*T)\100 simple intrest
p=5000
r=22
t=1
SI=(p*r*t)/100;
print(SI)


# In[28]:


#amount=p(1+r/1oo)time
principle=float(input("the enter value of principle value in float;"))
rate=float(input("the rate of the value in float type;"))
time=float(input("enter the value of time in float;"))
val1=(1 + rate) /100
val2=val1**time
amount=principle * val2
print(amount)


# In[6]:


length = 10
breadth = 7.7
area = length * breadth
perimeter = 2 * (length + breadth)
print(area)
print("the Area of rectangle with breadth {1} and length {0} is {2} ".format(length, breadth,int(area)))#indexing
area=int(area)
print(area)
print(type(area))


# In[7]:


N=int(input("enter the natural number as N:"))
sum1=0
for i in range(1,N+1):
    sum1=sum1+i+i
    print(sum1)
print("the sum of square of first {N} natural number;",sum1)


# In[16]:


N=int(input("enter the cube number as N:"))
sum1=0
for i in range (1,N+1):
    sum1=i**3
    print(sum1)
print("the sum of cube of first {N} natural number;",sum1)
print(N)


# In[5]:


character1=input("enter the character:")
character2=input("enter the character:")
ascii_value1=ord(character1)
ascii_value2=ord(character2)
print("the ascii value of", character1 , "is", ascii_value1,ascii_value2 )
print(type(character1),type(character2))
print(type(ascii_value1),type(ascii_value2))
print(id(character1),id(character2))
print(id(ascii_value1),id(ascii_value2))


# In[ ]:





# In[ ]:




