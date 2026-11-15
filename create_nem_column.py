import pandas as pd

df = pd.DataFrame({
    'Product': ['Laptop', 'Mouse', 'Keyboard'],
    'Price': [1000, 20, 50],
    'Quantity': [2, 5, 3]
})

df['Total'] = df['Price'] * df['Quantity']
df['Tax_Rate'] = 0.20
df['Tax_Amount'] = df['Price'] * df['Tax_Rate']
df['Is_Expensive'] = df['Price'] > 100

print(df)
print('----------------\n'*2)
users = pd.DataFrame({
    'First_Name': ['Ivan', 'Anna'],
    'Last_Name': ['Ivanov', 'Karenina']
})

users['Full_Name'] = users['First_Name'] + ' ' + users['Last_Name']

print(users)
