# pandas-tips

### 1. Insert a new row in top of a dataframe 

```python
df.loc[-1] = ['All']
df.index = df.index + 1
df = df.sort_index()
```

### 2. Group rows by a column into a list
1 column
```python
df = df.groupby('column_1')['column_2'].apply(list).reset_index(name='lists')
```
Many columns
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
