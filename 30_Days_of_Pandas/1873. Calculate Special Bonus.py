import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees[(employees['employee_id'] % 2 != 0) & (employees['name'].str.contains('^[^M]', regex = True))]['salary']
    # (employees['name'].str.startswith('M'))    # Another Alternative for second filter
    # (employees['name'].str[0] != 'M')          # Another Alternative for second filter
    employees['bonus'] = employees['bonus'].fillna(0)
    return employees[['employee_id', 'bonus']].sort_values(by = ['employee_id'])