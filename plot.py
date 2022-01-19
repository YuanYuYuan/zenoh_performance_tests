from glob import glob
import pandas as pd
import os
import plotly.express as px

COLS = ['Peers', 'Time', 'CPU', 'MEM', 'VMEM']
log_dir = './on-meta-3'
total_df = pd.DataFrame(columns=COLS)
lst = []
for log_file in sorted(glob(os.path.join(log_dir, 'log*.txt'))):
    #  print(log_file)
    df = pd.read_csv(
        log_file,
        sep='\\s+',
        skiprows=1
    )
    df.columns = COLS[1:]
    exp_name = int(log_file.split('/')[-1].split('.')[0].split('-')[1])
    df.insert(0, COLS[0], exp_name)
    lst.append(df)
    #  print(df)

total_df = pd.concat(lst, ignore_index=True)
#  total_df.append(df, ignore_index=True)
print(total_df)

fig = px.line(
    total_df,
    x='Time',
    y='MEM',
    color='Peers',
)
fig.show()
    #  print(df)
    #  break
    #  with open(log_file) as f:
    #      for line in f.readlines()[1:]:
    #          time, cpu, mem, _ = line.split()
    #          print(time, mem)
    #      break

