#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import re
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""

"""Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
def read_urls(filename):
    myfile = open(filename, 'r')
    contents = myfile.readlines()
    urls= []
    for s in contents:
        url = s
        pattern = '/edu.*.jpg'
        match = re.search(pattern, url)
        if match:
            urls.append('http://code.google.com' + match.group())
            
            
    return urls

            
        
  
"""Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
def download_images(img_urls, dest_dir):
    counter = 1
    filenames = []
    for i in img_urls:
        pat = r'puzzle/.*.jpg'
        match = re.search(pat, i)
        filename = match.group()
        filenames.append(filename[7:])
        urllib.request.urlretrieve(i, dest_dir+filename[7:])
        print ("Downloading...")
        counter +=1
    
    print ("Completed")
    return filenames
        
        
  

def main():
  myurls = read_urls("./animal_code.google.com")
  files = download_images(myurls, "./DownloadedImages/")
  html_file = open("./DownloadedImages/image.html", 'w')
  files.sort()
  html_file.write("<verbatim><html><body>")
  for i in files:
      html_file.write("<img src=./"+i+">")
  html_file.write("</body></html>")
  

if __name__ == '__main__':
  main()
