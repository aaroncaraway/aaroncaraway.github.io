---
layout: single
title: Express Express on AWS
---

FUN FACT! Apparently, [I've done this before](http://node-express-env-fml.ttq32xvqem.us-west-2.elasticbeanstalk.com/)!

Using [this](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_nodejs_express.html) guide straight from AWS.

```console
$ mkdir node-express
$ cd node-express
$ git init
```
```console
$ vi .gitignore
```

copy pasta
```
node_modules/
.gitignore
.elasticbeanstalk/
```

YES WE ARE WEST 2 -- do not google this again, Aaron.
```console
$ eb init --platform node.js --region us-west-2
$ eb create --sample node-express-env-NEW-NAME-DUH
$ eb open node-express-env-NEW-NAME-DUH
```

```console
$ mkdir .ebextensions
$ cd .ebextensions/
$ vi nodecommand.config
```
copy pasta
```
option_settings:
  aws:elasticbeanstalk:container:nodejs:
    NodeCommand: "npm start"
```
```console
$ cd ..
$ git add .
$ git commit -m "Definitely not my first express app"
$ eb deploy node-express-env-NEW-NAME-DUH
```

```console
$ cd .ebextensions/
$ vi staticfiles.config
```

copy pasta
```
option_settings:
  aws:elasticbeanstalk:container:nodejs:staticfiles:
    /public: /public
```

```javascript
exports.index = function(req, res) {
 res.render('cat', {title: 'My Cat Log'});
};

exports.add_cat = function(req, res) {
};
```

```console
$ cd ..
$ vi app.js
```

copy pasta
```
var express = require('express');
var path = require('path');
*var cat = require('./routes/cat');*
```

copy pasta
```javascript
var app = express();
*app.get('/cats', cat.index);*
*app.post('/add_cat', cat.add_cat);*
```

```console
$ git add .ebextensions/ app.js
$ git commit -m "Serve stylesheets statically with nginx."
$ cp views/index.jade views/cat.jade
$ git add .
$ git commit -m "Add cats route and template"
$ eb deploy node-express-env-NEW-NAME-DUH
```