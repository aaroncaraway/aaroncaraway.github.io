---
layout: single
title: 'Browser Journal'
---

SEE ALSO:
2019-10-11 daily log

RESOURCES:
[NODE + Python](https://www.quora.com/How-do-I-send-data-from-Node-js-to-Python-and-get-back-JSONN-data-from-Python-to-Node-jss)

NOTES:

Ideal flow of the Browser Journal (unfortunately abbreviated to BJ)
1. USER Goes to page 
2. USER Uploads google history
3. REACT_SITE: Sends google history OG to SERVER
4. NODE_SERVER: Saves gh_OG to AWS_S3, returns 'saved' to SITE & USER
5. NODE_SERVER: Sends gh_OG to python script for cleaning


6. PYTHON_SCRIPT: Cleans gh_OG, saves gh_clean to AWS, returns gh_clean to NODE, to REACT_SITE
  a. filename = get request to /get_filename
  b. data = get request to url/`filename`
  c. cleaned_data = process_data()
  d. post cleaned_data to /cleaned_data

4. SITE: Cleans (and saves) google history CLEAN
5. SITE: Returns link to saved and cleaned history

? USER: Views cleaned history


SIMPLIFIED
1. USER: Uploads word.txt
2. SITE: Sends word.txt to SERVER
3. SERVER: runs python file sends response to SITE
