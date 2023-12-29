import pandas as pd

def count_occurrences(files: pd.DataFrame) -> pd.DataFrame:
    regexp_bull = r' \bbull '
    regexp_bear = r' \bbear '
    bulls = files[files['content'].str.contains(regexp_bull, regex = True)]['content'].count()
    bears = files[files['content'].str.contains(regexp_bear, regex = True)]['content'].count()
    return pd.DataFrame({'word': ['bull', 'bear'], 'count':[bulls, bears]})