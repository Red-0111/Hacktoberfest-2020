import pandas as pd
dict={'Name':['Silvi','Shreya','Shaina','Shan'],'Roll No':[72,70,45,29],'Eng_Marks':[96,67,89,74],'Maths_Marks':[99,88,77,67],'science_Marks':[54,87,65,45]}
df=pd.DataFrame(dict)
column_list = list(df)
column_list.remove("Roll No")
df["sum"] = df[column_list].sum(axis=1)
print(df)
