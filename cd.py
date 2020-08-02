# Import the required libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Let us initialize the required values ( we will use them later in the program )
# we will set the minimum marks to 40 to pass in a exam
passmark = 40


# Let us read the data from the csv file
df = pd.read_csv("StudentsPerformance1.csv")


# We will print top few rows to understand about the various data columns
# print(df.head())

#Cách 1
# Peeking into data
# print(df.columns)

# print(df.head())

# print(df.isnull().sum())

# sns.distplot(df['math score'], bins=20, color='orange')
# plt.show()

# sns.catplot(y="gender",  kind="count", height=6, aspect=2, data=df);
# plt.show()

# print(df['gender'].value_counts(normalize=True) * 100)

#
# sns.catplot(x="test preparation course", y="math score", data=df, height=6, aspect=2, kind='swarm', hue='Over');
# plt.show()

# df['Math_PassStatus'] = np.where(df['math score']<passmark, 'Fail', 'Pass')
# print(df.Math_PassStatus.value_counts())

# sns.catplot(y="gender",  kind="count", height=4, aspect=2, data=df);
# plt.show()

# print(df['gender'].value_counts(normalize=True) * 100)


# sns.catplot(y="gender", x="math score", data=df, height=5, aspect=2, kind='swarm', hue='Math_PassStatus');
# plt.show()

# sns.catplot(y="race/ethnicity",  kind="count", height=4, aspect=2, data=df);
# plt.show()

# print(df['race/ethnicity'].value_counts(normalize=True) * 100)

# sns.catplot(y="parental level of education",  kind="count", height=4, aspect=2, data=df);
# plt.show()

# print(df['parental level of education'].value_counts(normalize=True) * 100)

# sns.catplot(y="lunch",  kind="count", height=4, aspect=2, data=df);
# plt.show()

# print(df['lunch'].value_counts(normalize=True) * 100)

# sns.catplot(y="test preparation course",  kind="count", height=4, aspect=2, data=df);
# plt.show()

# print(df['test preparation course'].value_counts(normalize=True) * 100)


#Math

# sns.distplot(df['math score'], bins=20, color='red')
# plt.show()

# df['Math_PassStatus'] = np.where(df['math score']<passmark, 'Fail', 'Pass')
# print(df.Math_PassStatus.value_counts())
#
# df['Math_PassStatus'] = np.where(df['math score']<passmark, 'Fail', 'Pass')
# sns.catplot(y="gender", x="math score", data=df, height=5, aspect=2, kind='swarm', hue='Math_PassStatus');
# plt.show()

# df['Math_PassStatus'] = np.where(df['math score']<passmark, 'Fail', 'Pass')
# p = sns.countplot(x='parental level of education', data = df, hue='Math_PassStatus', palette='bright');
# _ = plt.setp(p.get_xticklabels(), rotation=90)
# plt.show()

# df['Math_PassStatus'] = np.where(df['math score']<passmark, 'Fail', 'Pass')
# p = sns.countplot(x='race/ethnicity', data = df, hue='Math_PassStatus', palette='bright');
# _ = plt.setp(p.get_xticklabels(), rotation=90)
# plt.show()

# df['Math_PassStatus'] = np.where(df['math score']<passmark, 'Fail', 'Pass')
# sns.catplot(x="math score", y="test preparation course", data=df, height=5, aspect=2, kind='swarm', hue='Math_PassStatus');
# plt.show()

# df['Math_PassStatus'] = np.where(df['math score']<passmark, 'Fail', 'Pass')
# sns.catplot(x="lunch", y="math score", data=df, height=5, aspect=2, kind='swarm', hue='Math_PassStatus');
# plt.show()


# Reading

# sns.distplot(df['reading score'], bins=20, color='green')
# plt.show()

# df['Reading_PassStatus'] = np.where(df['reading score']<passmark, 'F', 'P')
# print(df.Reading_PassStatus.value_counts())

# df['Reading_PassStatus'] = np.where(df['reading score']<passmark, 'F', 'P')
# sns.catplot(y="gender", x="reading score", data=df, height=5, aspect=2, kind='swarm', hue='Reading_PassStatus');
# plt.show()

# df['Reading_PassStatus'] = np.where(df['reading score']<passmark, 'F', 'P')
# p = sns.countplot(x='parental level of education', data = df, hue='Reading_PassStatus', palette='bright')
# _ = plt.setp(p.get_xticklabels(), rotation=90)
# plt.show()

# df['Reading_PassStatus'] = np.where(df['reading score']<passmark, 'F', 'P')
# p = sns.countplot(x='race/ethnicity', data = df, hue='Reading_PassStatus', palette='bright');
# _ = plt.setp(p.get_xticklabels(), rotation=90)
# plt.show()

# df['Reading_PassStatus'] = np.where(df['reading score']<passmark, 'F', 'P')
# sns.catplot(x="test preparation course", y="reading score", data=df, height=5, aspect=2, kind='swarm', hue='Reading_PassStatus');
# plt.show()

# df['Reading_PassStatus'] = np.where(df['reading score']<passmark, 'F', 'P')
# sns.catplot(x="lunch", y="reading score", data=df, height=5, aspect=2, kind='swarm', hue='Reading_PassStatus');
# plt.show()


# Writing

# sns.distplot(df['writing score'], bins=20, color='purple')
# plt.show()

# df['Writing_PassStatus'] = np.where(df['writing score']<passmark, 'F', 'P')
# print(df.Writing_PassStatus.value_counts())

# df['Writing_PassStatus'] = np.where(df['writing score']<passmark, 'F', 'P')
# sns.catplot(y="gender", x="writing score", data=df, height=5, aspect=2, kind='swarm', hue='Writing_PassStatus');
# plt.show()

# df['Writing_PassStatus'] = np.where(df['writing score']<passmark, 'F', 'P')
# p = sns.countplot(x='parental level of education', data = df, hue='Writing_PassStatus', palette='bright')
# _ = plt.setp(p.get_xticklabels(), rotation=90)
# plt.show()

# df['Writing_PassStatus'] = np.where(df['writing score']<passmark, 'F', 'P')
# p = sns.countplot(x='race/ethnicity', data = df, hue='Writing_PassStatus', palette='bright');
# _ = plt.setp(p.get_xticklabels(), rotation=90)
# plt.show()

# df['Writing_PassStatus'] = np.where(df['writing score']<passmark, 'F', 'P')
# sns.catplot(x="test preparation course", y="writing score", data=df, height=5, aspect=2, kind='swarm', hue='Writing_PassStatus');
# plt.show()

# df['Writing_PassStatus'] = np.where(df['writing score']<passmark, 'F', 'P')
# sns.catplot(x="lunch", y="writing score", data=df, height=5, aspect=2, kind='swarm', hue='Writing_PassStatus');
# plt.show()




# Cách 2
# Size of data frame
# There are 1000 rows and 8 columns
# Column headers are 'gender', 'race/ethnicity', 'parental level of education', 'lunch', 'test preparation course', 'math score', 'reading score' and 'writing score'
# There is no null columns
# print(df.shape)

# Let us understand about the basic information of the data, like min, max, mean and standard deviation etc.
# print(df.describe())


# Let us check for any missing values
# print(df.isnull().sum())
# As seen above, there are no missing ( null ) values in this dataframe but in real scenarios we need work on
# dataset with a lot of missing values


# Let us explore the Math Score first
# p = sns.countplot(x="math score", data = df, palette="muted")
# _ = plt.setp(p.get_xticklabels(), rotation=90)
# plt.show()


# How many students passed in Math exam ?
# df['Math_PassStatus'] = np.where(df['math score']<passmark, 'F', 'P')
# print(df.Math_PassStatus.value_counts())

# # p = sns.countplot(x="parental level of education", data = df, hue="Math_PassStatus", palette="bright")
# _ = plt.setp(p.get_xticklabels(), rotation=90)
# plt.show()


# Let us explore the Reading score
# sns.countplot(x="reading score", data = df, palette="muted")
# plt.show()


# How many studends passed in reading ?
# readingdf['Reading_PassStatus'] = np.where(df['reading score']<passmark, 'F', 'P')
# print(df.Reading_PassStatus.value_counts())

# # p = sns.countplot(x='parental level of education', data = df, hue='Reading_PassStatus', palette='bright')
# _ = plt.setp(p.get_xticklabels(), rotation=90)
# plt.show()


# Let us explore writing score
# p = sns.countplot(x="writing score", data = df, palette="muted")
# _ = plt.setp(p.get_xticklabels(), rotation=90)
# plt.show()


# How many students passed writing ?
# df['Writing_PassStatus'] = np.where(df['writing score']<passmark, 'F', 'P')
# print(df.Writing_PassStatus.value_counts())

# # p = sns.countplot(x='parental level of education', data = df, hue='Writing_PassStatus', palette='bright')
# _ = plt.setp(p.get_xticklabels(), rotation=90)
# plt.show()


# Iet us check "How many students passed in all the subjects ?"
# # df['OverAll_PassStatus'] = df.apply(lambda x : 'F' if x['Math_PassStatus'] == 'F' or
#     x['Reading_PassStatus'] == 'F' or x['Writing_PassStatus'] == 'F' else 'P', axis =1)
# print(df.OverAll_PassStatus.value_counts())

# # p = sns.countplot(x='parental level of education', data = df, hue='OverAll_PassStatus', palette='bright')
# _ = plt.setp(p.get_xticklabels(), rotation=90)
# plt.show()

# Find the percentage of marks
# # df['Total_Marks'] = df['math score']+df['reading score']+df['writing score']
# df['Percentage'] = df['Total_Marks']/3

# # p = sns.countplot(x="Percentage", data = df, palette="muted")
# _ = plt.setp(p.get_xticklabels(), rotation=0)
# plt.show()


# Let us assign the grades
# Grading
# above 80 = A Grade
# 70 to 80 = B Grade
# 60 to 70 = C Grade
# 50 to 60 = D Grade
# 40 to 50 = E Grade
# below 40 = F Grade ( means Fail )

# # def GetGrade(Percentage, OverAll_PassStatus):
#     if ( OverAll_PassStatus == 'F'):
#         return 'F'
#     if ( Percentage >= 80 ):
#         return 'A'
#     if ( Percentage >= 70):
#         return 'B'
#     if ( Percentage >= 60):
#         return 'C'
#     if ( Percentage >= 50):
#         return 'D'
#     if ( Percentage >= 40):
#         return 'E'
#     else:
#         return 'F'
#
# df['Grade'] = df.apply(lambda x : GetGrade(x['Percentage'], x['OverAll_PassStatus']), axis=1)
#
# print(df.Grade.value_counts())


# we will plot the grades obtained in a order
# # sns.countplot(x="Grade", data = df, order=['A','B','C','D','E','F'],  palette="muted")
# plt.show()

# # p = sns.countplot(x='parental level of education', data = df, hue='Grade', palette='bright')
# _ = plt.setp(p.get_xticklabels(), rotation=90)
# plt.show()