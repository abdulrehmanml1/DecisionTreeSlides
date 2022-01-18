# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 15:51:17 2019

@author: Abdul Rehman
"""

import pandas as pd 

path='C:\\Users\\Abdul Rehman\\Desktop\\weat.csv'

path


df=pd.read_csv(path)


df.columns

#Make List of features
list(df.columns)

#Three Methods to read single coloumn 
df.columns[0]

df.OutLook

df['OutLook']

df[df.columns[0]]

df

#Detecting the shape 
df.shape

row=df.shape[0]

End_label =df.columns[-1]
df[End_label]

#Sepearting Classes from each other 
df.Play.unique()

#Seperate the valiues of no 

Total_No=df[df.Play=='no']
Total_Yes=df[df.Play=='yes']

df[(df['OutLook']=='rainy') & (df.Play=='no')]

#Pehly 5 rows show karwaata 
df.loc[:5]
#Pehly 5 rows show karwaata 
df.head()


df['OutLook'].loc[:5]


#Total Entropy of function
import math as mt 
mt.log2(Total_No)

#From lists make table

names=[input() for i in range(int(input()))]
ages=[int(input() for i in range(int(input())))]

#Making the csv Table but rows and coloumns shoul be same 
name=['Abdullah','asif','danial','kashif','ali']
age=[12,14,15,67,89]

col=['Name','Age']
df=pd.DataFrame(columns=col)
df.Name=name
df.Age=age

path_1='C:\\Users\\Abdul Rehman\\Desktop\\hasan.csv'
df.to_csv(path,index=False)



t_yes.shape [0]

n=t_no.shape[0]
import numpy as np


def Entopy(N,x,y):
    ye=yes/t_rows*np.log2(yes/t_rows)

    no=no/t_rows*np.log2(no/t_rows)

    ent=-ye-no
    return ent


sunn=df[df.Outlook=="Sunny"]

#for unique output 
df.Outlook.unique()


df.columns[-1]


sun[sunn.play=='yes']


#for counting the number of elements 
a=sun[sunn.play=='yes'].shape[0]

b=sun[sunn.play=='no'].shape[0]






    









