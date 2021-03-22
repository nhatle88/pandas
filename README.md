# pandas-tips

### insert a new row for All Buildings selection
df.loc[-1] = ['All']  # adding a row
df.index = df.index + 1  # shifting index
df = df.sort_index()  # sorting by index
