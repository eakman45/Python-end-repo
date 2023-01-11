#!/usr/bin/env python
# coding: utf-8

# # Soru 1

# 1-Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden oluşabileceği gibi, non-scalar verilerden de oluşabilir.

# In[1]:


def flatten(x):
    
    for i in x:
        if isinstance(i,list): # determine if its type is list or not. It is working until it is not list.
            flatten(i)
        else:
            empty_list.append(i)
    
    

x= [[1,'a',['cat'],2],[[[3]],'dog'],4,5] #given list
empty_list = [] 
flatten(x)
print(empty_list)

        


# Örnek inputlar ve sonuçları:input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

# # Soru 2

# 2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:
# 
# input: [[1, 2], [3, 4], [5, 6, 7]]
# 
# output: [[[7, 6, 5], [4, 3], [2, 1]]

# In[2]:


def reverse_list(l):
    l.reverse()
    for sublist in l:
        if type(sublist) == list:
            reverse_list(sublist)
    return l


# In[3]:


x= [[1, 2], [3, 4], [5, 6, 7]]


# In[4]:


print(reverse_list(x))

