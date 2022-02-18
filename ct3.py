#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st
st.header ("currency converter/18.feb.2022")
st.write ("tzs to usd")
tzs=st.slider("tzs")
st.write("in usd is",tzs*0.00043)

st.write("usd to tzs")
usd=st.slider("usd")
st.write("in tzs is",usd*2313)


# In[ ]:




