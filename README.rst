Introduction
-------------

This project was built to scrape tables from the TeamRankings website <https://www.teamrankings.com/>.

Folder Structure
----------------
.. code-block:: text

    TeamRankingsWebScraper/
    ├-package/
    │ └-__init__.py
    │ └-datascraper.py
    ├-MANIFEST.in
    ├-README.rst
    ├-main.py
    └-setup.py


Production
----------

To run this program, call the `main.py` via a python interpreter (or command line), 
give it a TeamRanking URL and the program will fetch the table and convert it to a pandas dataframe. You can save the 
resulting dataframe in a CSV to a location on your computer.

