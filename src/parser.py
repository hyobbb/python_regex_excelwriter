import re
import pandas as pd

def openFile(path: str) -> pd.DataFrame:
    return pd.read_excel(path, engine='openpyxl')


def replace(line: str) -> str:
    return re.sub('(?<=[0-9])개', 'EA', line)
    