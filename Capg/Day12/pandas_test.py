# import pandas as pd

# data = {
#     'Name': ['sandeep', 'harish', 'deepu'],
#     'Age': [21, 23, 19],
#     'Place': ["hyd", "knl", "Knl"]
# }

# df = pd.DataFrame(data)
# data1=df[df['Age']>20]
# data2=df.sort_values(by='Place',ascending=False)
# data3=df.groupby('Name')
# data4=df.groupby('Name').size()
# print("DataFrame is:\n", df)
# print(data1)
# print(data2)
# print(data3)

# # import pandas as pd
# # df=pd.read_csv('student-dataset.csv')
# # print(df)
# dataa=df.to_html()
# with open('data_frame.html','w') as file:
#     file.write(df.to_html())
    
#import pandas as pd

# data={
#     'region':['North','saouth','east','west','east','west'],
#     'state':['Delhi','Punjab','tamil nadu','karnataka','telangana','andhra'],
#     'year':[2012,2021,2023,2032,2015,2019],
#     'sales':[750000,89000,45000,84000,452000,63000],
#     "profit":[6200,5200,5300,1000,8000,9000]
# }

# df=pd.DataFrame(data)
# df.set_index(['region','state','year'],inplace=True)
# print(df)

# import pandas as pd

# # data={
# #     'name':['sandeep','deepu','harish'],
# #     'age':[21,19,23],
# #     'dept':['sd','ag','ca'],
# #     'place':['hyd','apeta','knl']
# # }
# df=pd.read_csv("student-dataset.csv")
# # df=pd.DataFrame(data)
# print(df)
# df.to_csv('csv_file.csv',index=False)
# df.set_index(['age'],inplace=True)
# print(df)

import pandas as pd
data = {
    'Region': ['North', 'North', 'South', 'South', 'East', 'East'],
    'State': ['Delhi', 'Punjab', 'Tamil Nadu', 'Karnataka', 'TG', 'Odisha'],
    'Year': [2021, 2022, 2021, 2022, 2021, 2022],
    'Sales': [750000, 820000, 690000, 720000, 670000, 710000],
    'Profit': [95000, 102000, 85000, 91000, 77000, 88000]
}

df=pd.DataFrame(data)
df.set_index(['Region','State','Year'],inplace=True)
print(df)

#advanced data selecting data from a multi=-indexed dataframes
df1=df.loc[('South',"Tamil Nadu",2021),'Sales']
print(df1)

#merging and joining dataframes
df_sales=pd.DataFrame({'State': ['Delhi', 'Tamil Nadu', 'West Bengal'], 'Sales': [1570000, 1410000, 130000]})
print(df_sales)
df_profit=pd.DataFrame({'State': ['Delhi', 'Tamil Nadu', 'West Bengal'], 'Profit': [1580000, 1810000, 195000]})
print(df_profit)
df_merged=pd.merge(df_sales,df_profit,on='State',how='inner')
print(df_merged)

