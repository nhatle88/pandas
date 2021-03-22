# pandas-tips

### 1. Insert a new row for All selection

```python
df.loc[-1] = ['All']
df.index = df.index + 1
df = df.sort_index()
```

