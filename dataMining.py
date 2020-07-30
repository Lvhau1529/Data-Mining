# Import các thư viện Numpy, Pandas, Seaborn, Matplotlib

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Đặt điểm tối thiểu để qua kỳ thi là 40
passmark = 40
# Đọc dữ liệu từ file csv
df = pd.read_csv("StudentsPerformance.csv")
# In ra một vài dòng dữ liệu
print("In ra một vài dòng dữ liệu")
print(df.head())
# Kích thước của dữ liệu
print("Kích thước của dữ liệu (1000 dòng, 8 cột)")
print(df.shape)
print(df.describe())
# Kiểm tra giá trị null trong bảng
print("Kiểm tra giá trị null trong bảng")
print(df.isnull().sum())
# Phân bố của các thuộc tính trong bảng
# Giới tính
print("Phân bố của các thuộc tính trong bảng")
print("Giới tính")
sns.catplot(y="gender",  kind="count", height=4, aspect=2, data=df)
plt.show()
print(df['gender'].value_counts(normalize=True) * 100)
# Sắc tộc
print("Sắc tộc")
sns.catplot(y="race/ethnicity",  kind="count", height=4, aspect=2, data=df)
plt.show()
print(df['race/ethnicity'].value_counts(normalize=True) * 100)
# Trình độ học vấn của phụ huynh
print("Trình độ học vấn của phụ huynh")
sns.catplot(y="parental level of education",  kind="count", height=4, aspect=2, data=df)
plt.show()
print(df['parental level of education'].value_counts(normalize=True) * 1000)