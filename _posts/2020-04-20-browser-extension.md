---
layout: single
title: 'dailylog 4-20-20'
tags: chromeextensions
---

## GET SHARE IDS

```Javascript
var buttons = document.getElementsByClassName('share');
```

## ADD NEW BUTTON ELEMENTS

```Javascript
for(const b of buttons){
    var b_id = b.getAttribute('data-pa-attr-listing_id')
    var new_href= "/listing/share?post_id=" + b_id
    var new_button = document.createElement('button')
    new_button.setAttribute('class', 'PCshare')
    new_button.setAttribute('data-ajax-method', 'post')
    new_button.setAttribute('data-ajax', 'true')
    new_button.setAttribute('href', new_href)
    document.body.appendChild(new_button)
    
    }

```

## CLICK THOSE ELEMENTS

```Javascript
for (const nb of new_buttons){nb.click()}

```