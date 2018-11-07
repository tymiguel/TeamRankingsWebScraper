import contextlib
import requests
import bs4
import pandas as pd
import collections
import os


class DataScrapper:

    @classmethod
    def save_df(cls, data_frame, out_path, out_file_name):
        """
        Save the data frame in a csv file.
        """
        path = os.path.join(out_path, out_file_name)
        data_frame.to_csv(path + '.csv')
        
        
    @classmethod
    def create_df(cls, soup_table, list_of_column_names):
        """
        Recreate the table the from the website.
        """
        # create ordered dict with an empty lists
        dict_of_values = collections.OrderedDict()
        for col_header in list_of_column_names:
            dict_of_values[col_header] = []
        
        # append values from table to the dict
        for row in soup_table.findAll("tr"): # soup.table grabs first table
            cells = row.findAll('td')
            if len(cells) > 1:
                for index in range(len(cells)):
                    if cells[index].find(text=True) == '\n':
                        dict_of_values[list_of_column_names[index]].append(row.findAll('a')[1].find(text=True))
                    else:
                        dict_of_values[list_of_column_names[index]].append(cells[index].find(text=True))
    
        return pd.DataFrame(dict_of_values)
    
    
    @classmethod
    def list_of_headers(cls, soup_table):
        """
        Get the names in the header table.
        """
        list_of_cols = []
        for row in soup_table.find_all('th'):
            list_of_cols.append(str(row.find(text=True)))
        return list_of_cols
                        
    
    @classmethod
    def get_first_table(cls, url):
        """
        Gets the first table in the html doc.
        """
        soup = cls.get_soup(url)
        return soup.table
            
        
    @classmethod
    def get_soup(cls, url):
        """
        Turns the html into a soup object.
        """
        raw_html = cls.simple_get(url)
        soup = bs4.BeautifulSoup(raw_html, 'html.parser')
        return soup
    
    
    @classmethod
    def simple_get(cls, url):
        """
        Attempts to get the content at `url` by making an HTTP GET request.
        If the content-type of response is some kind of HTML/XML, return the
        text content, otherwise return None.
        """
        try:
            with contextlib.closing(requests.get(url, stream=True)) as resp:
                if cls.is_good_response(resp):
                    return resp.content
                else:
                    return None

        except requests.exceptions.RequestException as e:
            cls.log_error('Error during requests to {0} : {1}'.format(url, str(e)))
            return None

        
    @staticmethod
    def is_good_response(resp):
        """
        Returns True if the response seems to be HTML, False otherwise.
        """
        content_type = resp.headers['Content-Type'].lower()
        return (resp.status_code == 200 
                and content_type is not None 
                and content_type.find('html') > -1)

    
    @staticmethod
    def log_error(e):
        """
        It is always a good idea to log errors. 
        This function just prints them, but you can
        make it do anything.
        """
        print(e)
