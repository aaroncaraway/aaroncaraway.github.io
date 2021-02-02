---
layout: single
permalink: /starting/
title: 'Starting from the Bottom'
---

ESLINT + PRETTIER + HEROKU

[From myself](https://aaroncaraway.github.io/dailylog-11-27-20/)

When using AWS from a new user, don't forget to [create a new access key](https://help.bittitan.com/hc/en-us/articles/115008255268-How-do-I-find-my-AWS-Access-Key-and-Secret-Access-Key-)

```console
$ pip3 install --upgrade pip
$ pip3 install jupyter
```

Need for BrowserJournal

```console
$ pip3 install pytz
```

OMG DO NOT FORGET THE NEED FOR A LINTER, YO
Also the big key (after installing Prettier and ESLint)

```javascript
"editor.formatOnSave": true
```

read more [here](https://hackernoon.com/write-beautiful-and-consistent-javascript-code-using-eslint-prettier-and-vscode-760837fdef89)

# HOW TO START ANY PROJECT

1. [Secure your env var, yo](https://medium.com/codait/environment-variables-or-keeping-your-secrets-secret-in-a-node-js-app-99019dfff716)
   aka KEEP YOUR SECRETS SECRET (still not totally sure I'm doing this right!?)

PROTIP: Any time you change your .env file, you MUST restart the server
PROTIP 2: All Create React Apps need `REACT_APP_` as a prefix to env variables

[More about env var](https://medium.com/@trekinbami/using-environment-variables-in-react-6b0a99d83cf5)
[Even more about it](https://create-react-app.dev/docs/adding-custom-environment-variables)

(search terms for self environment variables process.env process.ENV)
