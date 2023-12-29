import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    rege = r'^[A-Za-z][A-Za-z0-9_.-]*@leetcode[.]com$'
    return users[users['mail'].str.contains(rege, regex = True)]