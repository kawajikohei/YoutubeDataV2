import pandas as pd

# サンプルデータフレームの作成
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'Gender': ['F', 'M', 'M', 'M']
})
print(df)
# 列を反転する
df2 = df.loc[:, ::-1]
print(df2)
# 行を反転する
df3 = df[::-1]
print(df3)