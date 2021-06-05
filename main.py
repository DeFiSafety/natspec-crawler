import glob
import pandas as pd
from natspec import score
import sys

basepath = sys.argv[1]
mydict = {}

for filename in glob.iglob(basepath + '**/*.sol', recursive=True):
    test = filename[filename.find('contracts/')+10:]
    mydict[test] = score(filename)

df = pd.DataFrame.from_dict(mydict, orient='index', columns=['Score'])
print(df.to_markdown())

avg_score=df['Score'].sum() / (len(df.dropna()) * 100)
print(f'\nAverage score: {int(avg_score*100)}%')
