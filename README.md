# pandas-tips

### 1. Insert a new row for All selection

```python
df.loc[-1] = ['All']
df.index = df.index + 1
df = df.sort_index()
```

### 2. Group rows by a column into a list
```python
df = df.groupby('column_1')['column_2'].apply(list).reset_index(name='lists')
```
