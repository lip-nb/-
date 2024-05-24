import csv
import pandas as pd

# 打开CSV文件并读取数据
with open('douban.csv', 'r') as csvfile:
    # 跳过标题行
    next(csvfile)
    # 读取CSV数据
    reader = csv.reader(csvfile, delimiter=',')
    # 创建DataFrame
    df = pd.DataFrame(list(reader), columns=["电影", "已看过"])
    # 选择"已看过"列中值为1的行
    df = df.loc[df["已看过"] != "1"]
    UnWatch = {"电影":"新电影?","已看过":"没看过嘞"}
    df = df.rename(columns=UnWatch,inplace=False)
    Reindex = range(len(df))
    Reindex = pd.Series(Reindex, index=df.index)
    df.rename(Reindex,inplace=True)
    print(df["新电影?"])

#hello ha github 
#push again
'''
did you change
'''