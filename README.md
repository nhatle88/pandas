# pandas-tips

### insert a new row for All Buildings selection

<code>df.loc[-1] = ['All']</code></br>
<code>df.index = df.index + 1</code></br>
<code>df = df.sort_index()</code></br>

