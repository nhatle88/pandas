# pandas

### 1. Insert a new row in top of a dataframe 

```python
df.loc[-1] = ['All']
df.index = df.index + 1
df = df.sort_index()
```

### 2. Group rows by a column into a list
Group by 1 column, 1 other column into a list
```python
df = df.groupby('column_1')['column_2'].agg(list).reset_index()
```
Group by many columns, 1 column into a list
```python
df = df.groupby(['column_1','column_2'])['column_3'].agg(list).reset_index()
```
Group by 1 column, other columns into lists
```python
In [5]: df = pd.DataFrame( {'a':['A','A','B','B','B','C'], 'b':[1,2,5,5,4,6],'c'
   ...: :[3,3,3,4,4,4]})

In [6]: df
Out[6]: 
   a  b  c
0  A  1  3
1  A  2  3
2  B  5  3
3  B  5  4
4  B  4  4
5  C  6  4

In [7]: df.groupby('a').agg(lambda x: list(x))
Out[7]: 
           b          c
a                      
A     [1, 2]     [3, 3]
B  [5, 5, 4]  [3, 4, 4]
C        [6]        [4]
```

### 3. Select only colummns
```python
df[['column_1','column_2']]
```
