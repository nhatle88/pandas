# pandas-tips

# insert a new row for All Buildings selection
df_building.loc[-1] = ['Tất cả']  # adding a row
df_building.index = df_building.index + 1  # shifting index
df_building = df_building.sort_index()  # sorting by index
