---
layout: single
title: 'AWS EC2 PYTHON PARTY'
---


1. THE GOOD: I got my python summarizer live on heroku. 
2. THE BAD: I really want it on AWS
3. THE GOOD: I've gotten better at AWS!
4. THE BAD: But apparently not good enough...

--
## DOING THE THING:
1. THE GOOD: Got a flask app up and running!
2. THE BAD: It broke when I transfered my original summarizer app
3. THE GOOD: I fixed this by changing `app.py` to `application.py` (no joke)
4. THE BAD: It still doesn't make external requests...
5. THE GOOD: I fixed this by removing all security!! HELP ME.
6. THE BAD: I still cannot download the NLTK accoutrements I need for my summarizer (like sentence tokenizer)
7. THE GOOD: Apparently I can just ssh into my EB instance and download these right there!
8. THE BAD: This is not as easy as it sounds (because I did my ssh permissionvia the terminal originally and just got a pub file)

[SSH INTO INSTANCE](https://www.youtube.com/watch?v=j09C-YHX5Uc)

9. THE GOOD: Figured out how to make an instance and SSH into it!
10. THE BAD: It is somehow running PYTHON 2.7 HOW.


```console
sudo yum install python36
python3 -m pip install --user --upgrade pip
python3 -m pip install --user virtualenv

python3 -m virtualenv virt
source virt/bin/activate
pip3 install flask
```

