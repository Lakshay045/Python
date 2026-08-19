import pandas as pd

# Sample Dataset
data = {
    "Student_Name": ["Rahul", "Priya", "Aman", "Neha", "Rohit"],
    "Gender": ["Male", "Female", "Male", "Female", "Male"],
    "Hosteller": ["Yes", "No", "Yes", "No", "Yes"],
    "Performance": ["Excellent", "Good", "Average", "Good", "Excellent"],
    "Age": [20, 21, 22, 20, 23],
    "Marks": [88.5, 76.0, 69.5, 81.0, 92.5],
    "Subjects": [5, 6, 5, 6, 7]
}

df = pd.DataFrame(data)

print("\nSample Dataset")
print(df)

print("\nData Types")
print(df.dtypes)

print("\n--------------------------------------")
print("Attribute Types")
print("--------------------------------------")

print("Student_Name : Nominal")
print("Gender       : Binary (Nominal)")
print("Hosteller    : Binary")
print("Performance  : Ordinal")
print("Age          : Numeric (Discrete)")
print("Marks        : Numeric (Continuous)")
print("Subjects     : Numeric (Discrete)")


