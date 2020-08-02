#!/usr/bin/env python
# coding: utf-8

# # Phân tích các yếu tố ảnh hưởng đến kết quả bài thi của học sinh

# In[1]:


#Import các thư viện Numpy, Pandas, Seaborn, Matplotlib
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


#Đặt điểm tối thiểu để qua kỳ thi là 40
passmark = 40


# In[3]:


#Đọc dữ liệu từ file csv
df = pd.read_csv("StudentsPerformance.csv")


# In[4]:


#In ra một vài dòng dữ liệu
df.head()


# In[5]:


#Kích thước của dữ liệu (1000 dòng, 8 cột)
print (df.shape)


# In[6]:


df.describe()


# In[7]:


#Kiểm tra giá trị null trong bảng
df.isnull().sum()


# ## Phân bố của các thuộc tính trong bảng

# ### Giới tính

# In[8]:


sns.catplot(y="gender",  kind="count", height=4, aspect=2, data=df);


# In[9]:


df['gender'].value_counts(normalize=True) * 100


# ### Sắc tộc

# In[10]:


sns.catplot(y="race/ethnicity",  kind="count", height=4, aspect=2, data=df);


# In[11]:


df['race/ethnicity'].value_counts(normalize=True) * 100


# ### Trình độ học vấn của phụ huynh

# In[12]:


sns.catplot(y="parental level of education",  kind="count", height=4, aspect=2, data=df);


# In[13]:


df['parental level of education'].value_counts(normalize=True) * 100


# ### Bữa trưa

# In[14]:


sns.catplot(y="lunch",  kind="count", height=4, aspect=2, data=df);


# In[15]:


df['lunch'].value_counts(normalize=True) * 100


# ### Chuẩn bị trước kiểm tra

# In[16]:


sns.catplot(y="test preparation course",  kind="count", height=4, aspect=2, data=df);


# In[17]:


df['test preparation course'].value_counts(normalize=True) * 100


# ### Ảnh hưởng của các yếu tố đến điểm kiểm tra

# #### Math

# In[18]:


#Phân bố của điểm Math
sns.distplot(df['math score'], bins=20, color='red', kde=False)
plt.grid()


# In[19]:


#Số học sinh qua môn Math
df['Math_PassStatus'] = np.where(df['math score']<passmark, 'Fail', 'Pass')
df.Math_PassStatus.value_counts()


# In[20]:


#Ảnh hưởng của giới tính đến kết quả
sns.catplot(y="gender", x="math score", data=df, height=5, aspect=2, kind='swarm', hue='Math_PassStatus');
plt.grid()


# In[21]:


#Ảnh hưởng của trình độ học vấn cha mẹ đến kết quả
p = sns.countplot(x='parental level of education', data = df, hue='Math_PassStatus', palette='bright');
_ = plt.setp(p.get_xticklabels(), rotation=90) 


# In[22]:


#Ảnh hưởng của sắc tộc đến kết quả
p = sns.countplot(x='race/ethnicity', data = df, hue='Math_PassStatus', palette='bright');
_ = plt.setp(p.get_xticklabels(), rotation=90) 


# In[23]:


#Ảnh hưởng của việc chuẩn bị trước kỳ thi đến kết quả
sns.catplot(x="math score", y="test preparation course", data=df, height=5, aspect=2, kind='swarm', hue='Math_PassStatus');
plt.grid()


# In[24]:


# Ảnh hưởng của bữa trưa đến kết quả
sns.catplot(x="lunch", y="math score", data=df, height=5, aspect=2, kind='swarm', hue='Math_PassStatus');
plt.grid()


# #### Reading

# In[25]:


#Phân bố của điểm Reading
sns.distplot(df['reading score'], bins=20, color='green', kde=False)
plt.grid()


# In[26]:


#Số học sinh qua môn Reading
df['Reading_PassStatus'] = np.where(df['reading score']<passmark, 'F', 'P')
df.Reading_PassStatus.value_counts()


# In[27]:


#Ảnh hưởng của giới tính đến kết quả
sns.catplot(y="gender", x="reading score", data=df, height=5, aspect=2, kind='swarm', hue='Reading_PassStatus');
plt.grid()


# In[28]:


#Ảnh hưởng của trình độ học vấn cha mẹ đến kết quả
p = sns.countplot(x='parental level of education', data = df, hue='Reading_PassStatus', palette='bright')
_ = plt.setp(p.get_xticklabels(), rotation=90) 


# In[29]:


#Ảnh hưởng của sắc tộc đến kết quả
p = sns.countplot(x='race/ethnicity', data = df, hue='Reading_PassStatus', palette='bright');
_ = plt.setp(p.get_xticklabels(), rotation=90) 


# In[30]:


#Ảnh hưởng của việc chuẩn bị trước kỳ thi đến kết quả
sns.catplot(x="test preparation course", y="reading score", data=df, height=5, aspect=2, kind='swarm', hue='Reading_PassStatus');
plt.grid()


# In[31]:


# Ảnh hưởng của bữa trưa đến kết quả
sns.catplot(x="lunch", y="reading score", data=df, height=5, aspect=2, kind='swarm', hue='Reading_PassStatus');
plt.grid()


# #### Writing

# In[32]:


#Phân bố của điểm Writing
sns.distplot(df['writing score'], bins=20, color='purple', kde=False)
plt.grid()


# In[33]:


#Số học sinh qua Writing
df['Writing_PassStatus'] = np.where(df['writing score']<passmark, 'F', 'P')
df.Writing_PassStatus.value_counts()


# In[34]:


#Ảnh hưởng của giới tính đến kết quả
sns.catplot(y="gender", x="writing score", data=df, height=5, aspect=2, kind='swarm', hue='Writing_PassStatus');
plt.grid()


# In[35]:


#Ảnh hưởng của trình độ học vấn cha mẹ đến kết quả
p = sns.countplot(x='parental level of education', data = df, hue='Writing_PassStatus', palette='bright')
_ = plt.setp(p.get_xticklabels(), rotation=90) 


# In[36]:


#Ảnh hưởng của sắc tộc đến kết quả
p = sns.countplot(x='race/ethnicity', data = df, hue='Writing_PassStatus', palette='bright');
_ = plt.setp(p.get_xticklabels(), rotation=90) 


# In[37]:


# Ảnh hưởng của việc chuẩn bị trước kỳ thi đến kết quả
sns.catplot(x="test preparation course", y="writing score", data=df, height=5, aspect=2, kind='swarm', hue='Writing_PassStatus');
plt.grid()


# In[38]:


# Ảnh hưởng của bữa trưa đến kết quả
sns.catplot(x="lunch", y="writing score", data=df, height=5, aspect=2, kind='swarm', hue='Writing_PassStatus');
plt.grid()


# In[39]:


plt.rcParams['figure.figsize'] = (20, 10)
sns.countplot(df['math score'], palette = 'bright')
plt.title('Math Score',fontsize = 20)
plt.show()


# In[ ]:




