---
layout: single
title: 10-9-19
---
# Things I did today:
* Wrapped up HW1 for DS self
* Tried to regain my bearings with my project(s)
* eb list
* eb deploy
* Trying to successfully post to my ec2 server lololol
* Going to try curl via [this](http://tmont.com/blargh/2014/1/uploading-to-s3-in-bash)
* 1:38pm OMG YAY THAT WORKED!!! POST IS WORKING
* NEXT STEPS: Make my axios request work, too. 

```console
file=/path/to/file/to/upload.tar.gz
bucket=your-bucket
resource="/${bucket}/${file}"
contentType="application/x-compressed-tar"
dateValue=`date -R`
stringToSign="PUT\n\n${contentType}\n${dateValue}\n${resource}"
s3Key=xxxxxxxxxxxxxxxxxxxx
s3Secret=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
signature=`echo -en ${stringToSign} | openssl sha1 -hmac ${s3Secret} -binary | base64`
curl -X PUT -T "${file}" \
  -H "Host: ${bucket}.s3.amazonaws.com" \
  -H "Date: ${dateValue}" \
  -H "Content-Type: ${contentType}" \
  -H "Authorization: AWS ${s3Key}:${signature}" \
  https://${bucket}.s3.amazonaws.com/${file}
```
* 1:47p OMG OMG OMG WORKING YES. YES WORKING. Issue: the environment variable (I SO CAREFULLY SET AND SQUIRRELED AWAY) was a capital B and I was calling it with a lowercase b. Kids, don't try this at home.
* 2:03 now struggling to get the file sent to my actual server instead of my local machine
* 2:35 despairing -- googling isn't helping

# REFERENCES: 
* [this tutorial](https://medium.com/@khelif96/uploading-files-from-a-react-app-to-aws-s3-the-right-way-541dd6be689)
* [this aws tutorial](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_nodejs_express.html)

* [Known issues with axios + node + formData](https://stackoverflow.com/questions/43013858/how-to-post-a-file-from-a-form-with-axios)

* [How to handle frontend and backend deploy](https://stackoverflow.com/questions/41250087/how-to-deploy-a-react-nodejs-express-application-to-aws/41250688#41250688)
* [Part 2](https://stackoverflow.com/questions/41247687/how-to-deploy-separated-frontend-and-backend)

