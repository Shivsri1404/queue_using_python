#!/usr/bin/env python
# coding: utf-8

# # using_list

# In[1]:


qu=[]
qu.append(10)
qu.append(20)
qu.append(30)
qu


# In[2]:


qu.pop(0)


# In[3]:


qu.pop(0)


# In[4]:


qu.pop(0)


# In[5]:


qu.pop(0)


# In[7]:


not qu #for empty queue


# In[8]:


qu.insert(0,10)


# In[9]:


qu.insert(0,20)


# In[10]:


qu.insert(0,30)


# In[11]:


qu


# In[12]:


qu.pop()


# In[13]:


qu.pop()


# In[14]:


qu.pop()


# In[15]:


qu.append(10)
qu.append(20)
qu.append(30)


# In[16]:


qu[0]


# In[17]:


qu[-1]


# In[18]:


queue=[]
def enqueue():
    el=input()
    queue.append(el)
    print(queue)
def dequeue():
    if not queue:
        print("queue is empty")
    else:
        queue.pop(0)
    print(queue)
    
while True:
    print("chosse option 1. add 2. remove 3. quit")
    choice=int(input())
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        break
    else:
        print("please chosse correct option")


# # using_modules

# In[19]:


import collections 


# In[24]:


queue=collections.deque()


# In[25]:


queue


# In[26]:


#first_method
queue.appendleft(10)
queue.appendleft(20)
queue.appendleft(30)
queue


# In[27]:


queue.pop()


# In[28]:


queue.pop()
queue.pop()


# In[29]:


#second_method
queue.append(10)
queue.append(20)
queue.append(30)


# In[30]:


queue.popleft()


# In[31]:


queue.popleft()
queue.popleft()


# In[32]:


not queue


# In[33]:


queue.popleft()


# In[1]:


import queue


# In[2]:


q=queue.Queue(3)


# In[3]:


q.put(10)


# In[4]:


q.put_nowait(20)


# In[5]:


q.put(30)


# In[6]:


q


# In[7]:


q.put(40,timeout=1)


# In[8]:


q.get()


# In[9]:


q.get_nowait()


# In[10]:


q.get_nowait()


# In[12]:


not q


# In[13]:


q.get(timeout=1)


# In[14]:


len(q)==0


# # priority_queue

# # using_list

# In[21]:


q=[]


# In[22]:


q.append(10)
q.append(20)
q.append(30)
q.sort()


# In[23]:


q


# In[24]:


q.append(5)
q.sort()


# In[25]:


q


# In[26]:


q.pop(0) #lowest element highest priority 


# In[27]:


q.pop(0)


# In[28]:


q.pop(0)


# In[29]:


q.pop(0)


# # using modules

# In[30]:


import queue


# In[31]:


q=queue.PriorityQueue()


# In[32]:


q.put(10)
q.put(20)
q.put(30)


# In[33]:


q.put(5)
q.put(15)


# In[34]:


q.put(30)


# In[35]:


q.get()


# In[36]:


q.get()


# In[37]:


q.get()


# In[38]:


q.get()


# In[39]:


q.get()


# In[40]:


q.get()


# In[44]:


q=[]


# In[45]:


q.append((1,"alexa"))
q.append((2,"alex"))
q.append((5,"ale"))
q.append((3,"al"))


# In[46]:


q


# In[47]:


q.sort(reverse=True)


# In[48]:


q


# In[49]:


q.pop(0)


# In[50]:


q.pop(0)


# In[51]:


q.pop(0)


# In[52]:


q.pop(0)


# In[ ]:




