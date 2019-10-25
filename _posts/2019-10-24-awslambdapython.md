---
layout: single
title: 'AWS + LAMBDA + PYTHON + BEAUTIFUL SOUP!!'
---

OH EM GEE THIS IS THE BEST DAY!!
1. Get excited
2. Get even more excited because all of our problems are solved!! UP NEXT, WORLD HUNGER!!
3. Go to docs [here](https://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html) and go to `With a Virtual Environment`

```console
python3 -m venv v-env
source v-env/bin/activate
pip install LIBRARIES
deactivate
cd v-env/lib/python3.7/site-packages  
zip -r9 ${OLDPWD}/function.zip .
cd $OLDPWD
```


RESOURCES
[http from lambda](https://stackoverflow.com/questions/40136746/aws-lambda-sending-http-request)