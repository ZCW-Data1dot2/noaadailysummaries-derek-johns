from os import listdir
from os.path import isfile, join, splitext
import pandas as pd
import json


def read_json(file_path):
    with open(file_path) as f:
        return json.load(f)


def read_all_json_files(JSON_ROOT):
    all_files = [f for f in listdir(JSON_ROOT) if isfile(join(JSON_ROOT, f))]
    dfs = pd.DataFrame()
    for f in all_files:
        filename, file_ext = splitext(f)
        if file_ext == '.json':
            j = read_json(f'{JSON_ROOT}{f}')
            df = pd.DataFrame(j['results'])
            df['source'] = filename
            dfs = dfs.append(df, ignore_index=True)
    return dfs


