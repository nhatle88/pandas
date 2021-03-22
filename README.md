# pandas-tips

### insert a new row for All Buildings selection

`df.loc[-1] = ['All']
df.index = df.index + 1
df = df.sort_index()`

