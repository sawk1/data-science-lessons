import pandas as pd 
import numpy as np 

#Задание 1

authors = {
	'authors_id' : [1, 2, 3],
	'authors_name' : ['Тургенев', 'Чехов', 'Островский']
}
authors=pd.DataFrame(authors)

book = {
    'authors_id' : [1, 1, 1, 2, 2, 3, 3],
    'book_title' : ['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'],
    'price' : [450, 300, 350, 500, 450, 370, 290]
}

book=pd.DataFrame(book)

#Задание 2

author_price = pd.merge(authors, book, on='authors_id', how= 'inner')

#Задание 3

author_price.sort_values(by="price", inplace=True, na_position='first')
author_price.iloc[::-1].head(5)

#Задание 4

stat = author_price.groupby("authors_name")
min_stat = pd.DataFrame(stat['price'].min())
max_stat = pd.DataFrame(stat['price'].max())
mean_stat = pd.DataFrame(stat['price'].mean())

authors_stat_col = pd.concat([min_stat,max_stat,mean_stat], axis = 1, ignore_index=True)

authors_stat = {
    'authors_name' : author_price['authors_name'].unique(),
    'min_stat' : min_stat['price'],
    'max_stat' : max_stat['price'],
    'mean_stat' : mean_stat['price']
}
authors_stat = pd.DataFrame(authors_stat)
authors_stat.reset_index(drop=True, inplace=True)

#Задание 5

cover = { 'cover' : ['твердая', 'мягкая', 'мягкая', 'твердая', 'твердая', 'мягкая', 'мягкая']}
cover=pd.DataFrame(cover)
cover
author_price=pd.concat([author_price,cover], axis = 1, ignore_index=False)

book_info = pd.pivot_table(author_price.loc[:,'authors_name':'cover'], index = ['authors_name'], columns = ['cover'], aggfunc=np.sum, fill_value=0)
book_info.to_pickle('book_info.pkl')
book_info2=pd.read_pickle('book_info.pkl')

