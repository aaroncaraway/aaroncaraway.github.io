---
layout: single
title: "How to Save URLS to a Google Sheet"
tags: chrome extensions javascript howto
permalink: /projects/hoarder-helper
classes: wide
---

### PART 1: The Chrome Extension

manifest.json

```javascript
{
  "name": "keeperkdr",
  "version": "0.2",
  "description": "saves url to a google sheet",
  "browser_action": {
    "default_popup": "popup.html"
  },
  "permissions": ["tabs", "https://script.google.com/"],
  "manifest_version": 2
}
```

popup.html

```javascript
<!DOCTYPE html>
<html>
  <body>
    <h2>KLICK TO KEEP</h2>
    <script src="popup.js"></script>
  </body>
</html>
```

popup.js

```javascript
let urlToSave;
chrome.tabs.query({ active: true, lastFocusedWindow: true }, (tabs) => {
  urlToSave = tabs[0].url;

  function getCell() {
    var url =
      "https://script.google.com/macros/s/THE_ID_OF_SPREADSHEET/exec?cell=A1"; //url provided when published
    var x = new XMLHttpRequest();
    x.open("GET", url);
    x.onload = function () {
      console.log(x.response);
    };
    x.send();
  }

  function setCell() {
    var url =
      "https://script.google.com/macros/s/THE_ID_OF_SPREADSHEET/exec?cell=B1&value=" +
      urlToSave; //url provided when published
    var x = new XMLHttpRequest();
    x.open("POST", url);
    x.onload = function () {
      console.log(x.response);
    };
    x.send();
  }

  setCell();
});
```

### PART 2: The App Script

The Apps Script is slightly more involved if only for reasons of permissions. A good SO for this is [here](https://stackoverflow.com/questions/58719628/how-do-i-create-a-user-managed-cloud-platform-project). Before doing anything else

1. Create a new google sheet
2. Take note of the sheet's ID (it's the long long string in the url)
3. Create a Google Cloud Platform Project
4. Give that project auth permissions
5. Give that project Drive permissions
6. Go go script.google.com
7. Add this into the code section

```javascript
function doGet(e) {
  var params = e.parameter;
  var ss = SpreadsheetApp.openById("YOUR--SHEET--ID");
  var sheet = ss.getSheets()[0];
  var cell = sheet.getRange(params.cell.toUpperCase());
  var val = cell.getValue();
  return HtmlService.createHtmlOutput(val);
}
function doPost(e) {
  var params = e.parameter;
  var ss = SpreadsheetApp.openById("YOUR--SHEET--ID");
  var sheet = ss.getSheets()[0];
  var timecell = sheet.getRange("A1");
  var today = new Date();
  var date =
    today.getFullYear() + "-" + (today.getMonth() + 1) + "-" + today.getDate();
  timecell.setValue(date);
  var cell = sheet.getRange(params.cell.toUpperCase());
  cell.setValue(params.value);
  var v = cell.getValue();
  sheet.insertRowBefore(1);
  return HtmlService.createHtmlOutput(v);
}
```

8. Save and click Publish > Deploy as web app. Save that URL because that is what goes in our Chrome Extension! 
   NOTE: We have a SHEET url (which corresponds to the sheet we are adding to) and we have a SCRIPT url (which corresponds to the scripts.google.com script we created to interact as an intermediary between our extension and our sheet)
   ET VIOLA! This should be working now!

### RESOURCES

[reddit](https://www.reddit.com/r/learnjavascript/comments/7g9gdq/chrome_extension_to_write_to_google_sheet/)
[Google Cloud Proudcts and Permissions](https://stackoverflow.com/questions/58719628/how-do-i-create-a-user-managed-cloud-platform-project)
