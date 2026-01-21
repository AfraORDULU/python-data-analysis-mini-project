import pandas as pd

#Örnek verimiz
data = {
    "Name": ["Ali", "Ayşe", "Mehmet", "Zeynep", "Can"],
    "Age": [23, 21, 25, 22, 24],
    "Department": ["IT", "IT", "HR", "Finance", "IT"],
    "Salary": [12000, 11000, 10000, 10500, 13000]
}

df = pd.DataFrame(data)

#Temel analizlerimiz
print("İlk 5 Satır:")
print(df.head())

print("\nDepartmanlara Göre Ortalama Maaş:")
print(df.groupby("Department")["Salary"].mean())

print("\nYaşı 23'ten büyük olanlar:")
print(df[df["Age"] > 23])
