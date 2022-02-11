#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st
st.header("celcius to farenheit")
st.write("temp conversion")
c=st.number_input("input the temp in celcius")
st.write("temp in farenheit is",(c*9/5)+32)


# In[3]:


#taking kilometers from user
kilometers=float(input("enter the value in kilometers: "))
conv_factor=0.621371
miles=kilometers*conv_factor
print('%0.2f kilometers is equal to %0.2f miles'%(kilometers,miles))


# In[6]:


import time
from timeit import default_timer as timer
start=time.time()
print(23*2.3)
end=time.time()
print(end-start)


# In[5]:


import time
from timeit import default_timer as timer
start=time.time()
m=(5.96*1024)
print("mass of the earth is",m,"kg")
end=time.time()
print(end-start)


# In[ ]:




