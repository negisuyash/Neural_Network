
# coding: utf-8

# In[21]:


from matplotlib import pyplot as plt


# In[2]:


import numpy as np


# In[3]:


data=[[3,1.5,1],
      [2,1,0],
      [4,1.5,1],
      [3,1,0],
      [3.5,.5,1],
      [2,.5,0],
      [5.5,1,1],
      [1,1,0]]
mf=[4.5,1]


# In[9]:





# In[34]:


def sigmoid(x):
    return 1/(1+np.exp(-x))
def sigmoid_p(x):
    return sigmoid(x)*(1-sigmoid(x))


# In[36]:


X=np.linspace(-6,6,100)
plt.plot(X,sigmoid(X),c='r')
plt.plot(X,sigmoid_p(X),c='b')
plt.show()

# In[50]:


#scatter data
plt.axis([0,6,0,6])
plt.grid()
for i in range(len(data)):
    point =data[i]
    color='r'
    if point[2]==0:
        color='b'
    plt.scatter(point[0],point[1],c=color)
    plt.show()


# In[69]:


#training loop
learning_rate=0.01
costs=[]
w1=np.random.randn()
w2=np.random.randn()
b=np.random.randn()


for i in range(10000):
    ri=np.random.randint(len(data))
    point=data[ri]
    
    z=w1*point[0] + w2*point[1] +b
    pred=sigmoid(z)
    target=point[2]
    cost=np.square(pred-target)
    
    
    
    dcost_dz=(2*(pred-target))*(sigmoid_p(z))
    dcost_dw1= dcost_dz *point[0]
    dcost_dw2=dcost_dz*point[2]    
    dcost_db=dcost_dz*1
    w1=w1-learning_rate*dcost_dw1
    w2=w2-learning_rate*dcost_dw2
    b=b-learning_rate*dcost_db
    
    if i%100==0:
        cost_sum=0
        for j in range (len(data)):
            point=data[ri]
            z=point[0]*w1+point[1]*w2+b
            pred=sigmoid(z)
            target=point[2]
            cost_sum +=np.square(pred-target)
        costs.append(cost_sum/len(data))

plt.plot(costs)
    


# In[65]:


#seeing model prediction

for i in range(len(data)):
    point=data[i]
    print(point)
    z=point[0]*w1+point[1]*w2+b
    pred=sigmoid(z)
    print("pred: {}".format(pred))
    if(pred==1):
        print ("large tulip")
    else:
        print ("small tulip")



# In[66]:


z=mf[0]*w1+mf[1]*w2+b
pred=sigmoid(z)
print("predictioin is"+pred)


# import os

# In[70]:





# In[71]:


#import os


# In[75]:


#os.system("say hi")


# In[76]:


#import win32com.client as wincl
#speak = wincl.Dispatch("SAPI.SpVoice")
#speak.Speak("Hello World")

