#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv


# In[2]:


s=['sid','sname','city','contact']


# In[3]:


records=[[1,'rudra','chalthan',7632590102],
         [2,'veer','bardoli',9722955429],
         [3,'niraj','surat',9026763218],
         [4,'dhruv','bharuch',5656521478],
         [5,'viraj','surat',693006761]]
p=[]


# In[4]:


for i in range(5):
    sid=int(input("enter student id:"))
    sname=input("enter student name:")
    city=input("enter student city:")
    contact=int(input("enter student contact number:"))
    l=[sid,sname,city,contact]
    p.append(l)


# In[5]:


with open('C:\sqlite3\student.csv','w',newline='') as f:
    file=csv.writer(f)
    file.writerow(s)
    file.writerows(records)
    file.writerows(p)


# In[6]:


with open('C:\sqlite3\student.csv','r',newline='') as read:
    all_record=csv.reader(read)
    for records in all_record:
        print(records)


# In[ ]:




