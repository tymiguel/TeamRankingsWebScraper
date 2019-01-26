from package import *
import sys
import os


def main(url):
    
    print('Starting scrapper... \n')
    
    # create a soup table
    data_table = datascraper.get_first_table(url) # this will select the table on the site
    print('URL pull complete. \n')

    # select these names of the columns based on the header table
    column_names = datascraper.list_of_headers(data_table)

    # create data frame from the website table
    final_data_frame = datascraper.create_df(soup_table=data_table, list_of_column_names=column_names)
    print('Data Table complete. \n')
    
    # do you want to save the data frame to excel workbook?
    save_decision = input('Do you want to save table to an excel worksheet? (Y/N)' ).upper()
    if save_decision == 'Y':
        path_decision = input('Do you want to use your current directory {}? (Y/N) '.format(os.getcwd()) ).upper()
        if path_decision == 'Y':
            save_dir = os.getcwd()
        else:
            save_dir = input('Please enter the full path of the save location: ')
        save_file = input('Please enter a file name (with no extension): ')
        
        try:
            datascraper.save_df(final_data_frame, save_dir, save_file)
            print('File successfully saved at {}.'.format(save_dir))
        except: 
            print('I don\'t think the file saved, you should double check.')
    
    
if __name__ == '__main__':
    
    try:
        main(sys.argv[1])
    except IndexError as e:
        url = input('Please enter url: ' )
        main(url)

