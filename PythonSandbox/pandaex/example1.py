"""Author: Massimo D'Errico"""

import pandas as pd
titanic = pd.read_csv('titanic.csv')

#answer to question 1
print('\nanswer to question 1')
survivors = titanic[titanic['Survived']== 1]
print(survivors)

#answer to question 2
print('\nanswer to question 2')
fare_over_10 = titanic[titanic['Fare']>10]
name_age= fare_over_10[['Name']]
print(name_age)

#answer to question 3
print('\nanswer to question 3')
fare_over_10_all = titanic[(titanic['Survived'] == 1) & (titanic['Fare']<= 10)]
print(fare_over_10_all)

#answer to question 4
print('\nanswer to question 4')
female_young = titanic[(titanic['Survived'] == 1) & ((titanic['Sex'] == 'female') | (titanic['Age'] < 18))]
print(female_young[['Name']])

#answer to question 5
print('\nanswer to question 5')
female_count = titanic[titanic['Sex'] == 'female']
print(f"there are :{female_count['Sex'].count()} women ")

#answer to question 6
print('\nanswer to question 6')
fare_class2 = titanic[(titanic['Pclass'] == 2)]
print(f"mean fare of second class : {fare_class2['Fare'].mean()}")

#answer to question 7
print('\nanswer to question 7')
women_class1 = titanic[(titanic['Pclass'] == 1) & (titanic['Sex']== 'female')]
print(f"there are {women_class1['Sex'].count()} women in first class")

#answer to question 8
print('\nanswer to question 8')
survivors_class3 = titanic[ (titanic['Survived'] == 1) & (titanic['Pclass'] == 3)]
print(f"{(survivors_class3['Pclass'].count()/survivors['Pclass'].count())*100}% of survivors are in first class")

#answer to question 9
print('\nanswer to question 9')
male_survivors_class3 = titanic[ (titanic['Survived'] == 1) & (titanic['Pclass'] == 3) & (titanic['Sex']== 'male')]
male_class3 = titanic[ (titanic['Pclass'] == 3) & (titanic['Sex']== 'male')]
print(f"{(male_survivors_class3['Pclass'].count()/male_class3['Pclass'].count())*100}% of males survived in third class")