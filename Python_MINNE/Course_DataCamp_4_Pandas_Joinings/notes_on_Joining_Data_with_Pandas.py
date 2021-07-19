'''Datacamp course notes
    Joining Data with pandas
    https://learn.datacamp.com/courses/joining-data-with-pandas
    My status: 
'''
#
# Chapter 1
# 
## Inner joint
##########################
# default value how='inner'
##df_merged = df1.merge(df2, on='col_z')
##df_merged = df1.merge(df2, on=['col_x', 'col_y', 'col_z'])
##df_merged = df1.merge(df2, on='col_z', suffixes = ('_df1', '_df2'))
##df_merged = df1.merge(df2, on=['a','z']) \
##                    .merge(df3, on='w', suffixes=('_d12','_d3'))
#
# Chapter 2
# 
## Left joint
##########################
#df_merged = df1.merge(df2, on='id', how='left')
# Count empty values after join
# 1 - merge
#df_merged = df1.merge(df2, on='id', how='left')
# 2 - Count the number of rows in the b column that are missing
#number_of_missing = df_merged['b'].isnull().sum()
# select only the rows where column is null
#null_rows = df_merged[df_merged['col'].isnull()]

# Count the number of genres
# https://campus.datacamp.com/courses/joining-data-with-pandas/merging-tables-with-different-join-types?ex=7
#genre_count = genres_movies.groupby('genre').agg({'id':'count'})
# Plot a bar chart of the genre_count
#genre_count.plot(kind='bar')
#plt.show()

## Right joint
##########################
#df_merged = df1.merge(df2, how='right', left_on='id', right_on='df2_id')

## Outer joint
##########################
#df_merged = df1.merge(df2, on='id', how='outer', suffixes=('_fam', '_com'))

## Merging a table to itself
##########################
#df_merged = df1.merge(df2, left_on='sequel', right_on='id',
#                                 suffixes=('_org','_seq'))

## Merging on indexes
##########################   
#df_merged = df1.merge(df2, on='id', how='left')
## Multilndex datasets
#df_merged = df1.merge(df2, on=['movie_id','cast_id'])
df_merged = df1.merge(df2, left_on='id', left_index=True,
                             right_on='movie_id', right_index=True)

#
# Chapter 3
# 
## Filtering joint
##########################
# Mutating joins: Combines data from two tables based on matching observations in both tables 
# Filter joins: Filter observations from table based on whether or not they match an observation in another table

# Semi-join
# like inner join, but only the columns from the left table are shown
# Step 1 - merge 2 tables with an inner join
# Step 2 - filter : genres['gid'].isin(g_tracks['gid'])
# Step 3 - subset
# Example:
# Merge the non_mus_tck and top_invoices tables on tid
##tracks_invoices = non_mus_tcks.merge(top_invoices, on = 'tid')
# Use .isin() to subset non_mus_tcks to rows with tid in tracks_invoices
##top_tracks = non_mus_tcks[non_mus_tcks['tid'].isin(tracks_invoices['tid'])]
# Group the top_tracks by gid and count the tid rows
##cnt_by_gid = top_tracks.groupby(['gid'], as_index=False).agg({'tid':'count'})
# Merge the genres table to cnt_by_gid on gid and print
##merged = cnt_by_gid.merge(genres, on = 'gid')
##print(merged)

# Anti-join
# return the observations in the left table that do not have a matching observation in the right table
# returns only columns from the left table
# Step 1 - merge 2 tables with left join
# Step 2 - subset
# Step 3 - filter
# Merge employees and top_cust
# Example:
##empl_cust = employees.merge(top_cust, on='srid', 
                                 how='left', indicator=True)
# Select the srid column where _merge is left_only
##srid_list = empl_cust.loc[empl_cust['_merge'] == 'left_only', 'srid']
# Get employees not working with top customers
##print(employees[employees['srid'].isin(srid_list)])

# Concatenate DataFrames together vertically

# using append method

# verifying integrity

# validating merges
