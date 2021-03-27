df_grouped_date =  df.groupby('date')['is_active'].sum().reset_index() # sum of all actives on a date
df_grouped_date['cumsum'] = df_grouped_date['is_active'].cumsum() # accumulate the actives

date_min = df_grouped_date['date'].min()
date_max = df_grouped_date['date'].max()
date_rng = pd.date_range(start=date_min, end=date_max, freq='d')
    
df_active = pd.DataFrame(date_rng, columns=['date'])
df_active['date'] = df_active['date'].dt.date
df_result = pd.merge(df_active, df_grouped_date, how='left', on=['date'])
df_result['cumsum'] = df_result['cumsum'].ffill().astype(int) # replace NaNs with the value just above it.
 
