---
layout: single
permalink: /browser-journal/
title: 'How to Stalk Yourself'
---

## IN SHORT: 

1. Download history
2. Run script
3. Interact via CRA

## IN MEDIUM: 

1. Download your google search history here
2. Run this python script to clean it up
3. Create a teeny CRA for easy viewing

## IN CODE:

FORK ME HERE

```console
$ npx create-react-app browser-journal
$ cd browser-journal
$ yarn start
```

## IN LONG: 

So this one day I was hanging out in my kitchen (pretends to start this entry like every cooking blog ever when really we just want the freaking recipe, see IN CODE section above for this plz thx)

And we went down [this distracted rabbit hole](https://malcoded.com/posts/react-file-upload/) which was surprisingly fun because dude who wrote is great at explaining...
... Complete with [drag and drop](https://malcoded.com/posts/react-dropzone/)

But that was [a distraction](https://vimeo.com/347152004) from what I really wanted to do which is GET EVERYTHING ON AWS.

## PROJECT GET IT ON AWS

That took us to [this](https://www.reddit.com/r/aws/comments/ai9z34/simple_react_s3_example/) reddit thread
Which took us [here](https://aws-amplify.github.io/docs/js/storage) but then I realized learning another package isn't really what I want to be doing...

Then we found [this](https://www.koan.co/blog/uploading-images-to-s3-from-a-react-spa)
And [this](https://medium.com/@khelif96/uploading-files-from-a-react-app-to-aws-s3-the-right-way-541dd6be689)

But then I got overwhelmed and had to bike and shower and meditate and now we're back at it again with a slightly fresher brain.

I WISH I WAS LESS DISTRACTED doot doot doot!!

## FILE UPLOADS
[Using this tutorial](https://medium.com/@khelif96/uploading-files-from-a-react-app-to-aws-s3-the-right-way-541dd6be689)

Two apps going right now -- 
(1) FRONTEND: the react app that works with a json file  `browser-journal`
(2) BACKEND: the express server on aws that is in progress `node-express`

