---
layout: single
title: 'JS ALGOS & DS: Section 4'
tags: js_algos_and_ds
---


```javascript
// ORIGINAL
function charCount(str){
    var results = {};
    for (var i = 0; i < str.length; i++) {
        var char = str[i];
        if(results[char] > 0){
            results[char]++
        } else {
            results[char] = 1
        }
    }
    return results
}

charCount('pippin')

// REFACTORED ONCE
function refCharCount(str){
    var results = {};
    for (char of str) {
        char = char.toLowerCase()
        if (/[a-z0-9]/.test(char)){
            results[char] = ++results[char] || 1
        }
    }
    return results
}

refCharCount('Hi hello!')

// REFACTORED TWICE
function refCharCount(str){
    var results = {};
    for (char of str) {
        char = char.toLowerCase()
        if (isAlpha(char)){
            results[char] = ++results[char] || 1
        }
    }
    return results
}

function isAlpha(char){
    var code = char.charCodeAt(0);
    if (!(code > 47 && code < 58) && // numeric (0-9)
        !(code > 64 && code < 91) && // upper alpha (A-Z)
        !(code > 96 && code < 123)) { // lower alpha (a-z)
      return false;
    }
    return true;
}
refCharCount('aaaaa!!!')

```