---
layout: single
title: Express Express on AWS
---

FUN FACT! Apparently, I've done this before!

Using [this](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_nodejs_express.html) guide straight from AWS.

```console
$ mkdir node-express
$ cd node-express
$ git init
```
```console
$ vi .gitignore
```
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
