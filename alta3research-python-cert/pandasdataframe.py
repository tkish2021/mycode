#!/usr/bin/env python3
"""This is the Pandas DataFrame Formatting of tables
   I will create dataframes outputs using the movies data from the labs"""

import pandas as pd

#wget https://static.alta3.com/files/movies.xls

def main():
    # define the name of our xls file
    excel_file = 'movies.xls' #Point to the excel file

    # only the first sheet was read into the DF
    movies = pd.read_excel(excel_file, sheet_name=0, index_col=0)
    print("Print the First 25 movies which is rows 26 with 25movies and 1 header")
    print(movies.head(n=26)) #get headeres Pulls back first 25 movies including 1 header

    #df = pd.DataFrame(movies,columns=['Year'],dtype=float) to select year
    print("movies with Year reformated to float format")
    movdate = pd.DataFrame(movies,columns=['Year'],dtype=float) #We can reformat the year to change it to a float which is messed up but just to prove it you can change the formatting of the data values
    print(movdate)

    print("printing just the IMDB Scores and no other columns")
    imdb =  pd.DataFrame(movies,columns=['IMDB Score']) #Now we select IMDB Score
    print(imdb)
   
    print("Movies Runingtimes and Country")
    #movlength = pd.DataFrame(movies,columns=['Duration'],dtype=float)
    movlengcountry = pd.DataFrame(movies,columns=['Duration','Country']) #Now we select multiple columes to set side by side
    print(movlengcountry)
    
    print("listing of all the header columns note there is inferred index 0")
    headmov =  pd.DataFrame(movies.columns.values) #This is a good way to get what the columns can be selected from
    print(headmov)

if __name__ == "__main__":
    main()
