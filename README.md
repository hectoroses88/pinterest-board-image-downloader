# pinterest-board-image-downloader
A python script that downloads all images of a pinterest board.
Written in Python 2.7

Dependencies:
  1.  urllib (pip install urllib2)  
  2.  selenium (pip install selenium)
  
Selenium uses firefox to work so it needs firefox installed and geckodriver: https://github.com/mozilla/geckodriver/releases. Download and extract geckodriver.exe file in the same folder with downloadPinterestBoardImages.py.
Also make a folder named 'images' to save the downloaded pinterest pins.

If you want to use another browser such as Chrome, check selenium docs: https://selenium-python.readthedocs.io/installation.html
