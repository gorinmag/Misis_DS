import pandas as pd

df = pd.read_csv('task_8.csv')

def find_matches(input_value):
    matches = df[(df['name'].str.contains(input_value, case=False, regex=True)) |
                 (df['date_of_birth'].str.contains(input_value, case=False, regex=True)) |
                 (df['address'].str.contains(input_value, case=False, regex=True))]
    return matches

user_input = input("Введите имя, дату рождения или город: ")

print(find_matches(user_input))