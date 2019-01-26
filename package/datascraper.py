import contextlib
import requests
import bs4
import pandas as pd
import collections
import os


def save_df(data_frame, out_path,out_file_name):
    """
    Save the data frame in a csv file.
    """
    path = os.path.join(out_path, out_file_name)
    data_frame.to_csv(path + '.csv')
        
        

def create_df(soup_table, list_of_column_names):
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
    

def list_of_headers(soup_table):
    """
    Get the names in the header table.
    """
    list_of_cols = []
    for row in soup_table.find_all('th'):
        list_of_cols.append(str(row.find(text=True)))
    return list_of_cols
                        
    
def get_first_table(url):
    """
    Gets the first table in the html doc.
    """
    soup = get_soup(url)
    return soup.table
        

def get_soup(url):
    """
    Turns the html into a soup object.
    """
    raw_html = simple_get(url)
    soup = bs4.BeautifulSoup(raw_html, 'html.parser')
    return soup
    
    
def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with contextlib.closing(requests.get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except requests.exceptions.RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None

        
def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)


def log_error(e):
    """
    It is always a good idea to log errors. 
    This function just prints them, but you can
    make it do anything.
    """
    print(e)