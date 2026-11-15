import pandas as pd

data = {'name' : ['Anna', 'Bob', 'Charlie', 'David', 'Maria'],
         'grade': ['Senior', 'Middle', 'Senior', 'Senior', "Junior"],
         'salary':[160000, 120000, 200000, 140000, 100000]}
df = pd.DataFrame(data)

filt_use_mask = df[(df["grade"] == "Senior") & (df["salary"] > 150000)]
filt_with_metodth = df[(df["salary"].between(100000, 150000)) & (df['grade'].isin(["Senior", "Junior"]))]

levels = ['Senior', 'Junior']
filt_use_query = df.query("100000 <= salary <= 150000 and grade in @levels")
print(filt_use_query)
