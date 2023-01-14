import pandas as pd

pd.options.mode.chained_assignment = None

students = pd.read_csv('studentInfo.csv')

is_unique_id_student = students['id_student'].is_unique
print(is_unique_id_student)

number_of_nunique = students['id_student'].nunique()
print(number_of_nunique)

print(students.shape)
print(students['gender'].value_counts())
print(students['age_band'].value_counts())

students['imd_band'].value_counts(dropna=False).sort_index()
print('mean studied_credits', students['studied_credits'].mean())
print('median studied_credits', students['studied_credits'].median())
print('std studied_credits', students['studied_credits'].std())
print(students['studied_credits'].describe())

for col in ['region', 'gender' ,'highest_education', 'imd_band', 'age_band', 'disability', 'final_result']:
    students[col] = students[col].astype('category')

print(students.info())

print(students['final_result'].cat.codes)