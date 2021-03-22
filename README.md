# pandas-tips

### insert a new row for All Buildings selection

<code>df.loc[-1] = ['All']</code>
<code>df.index = df.index + 1</code>
<code>df = df.sort_index()</code>


