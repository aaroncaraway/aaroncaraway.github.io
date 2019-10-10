--- 
layout: single
title: 10-10-19
---

# Yesterday, a review:
1. YAY I GOT EVERYTHING WORKING LOCALLY!
2. But wait, not on aws. W T F
3. Panic
4. Panic more.
5. Turn the panic into sheer despair.
6. Break the problem down one by one.


1. Make sure the post request is working (on AWS)
[express docs on post](https://expressjs.com/en/4x/api.html#app.post.method)
2. [Test via curl](https://stackoverflow.com/questions/7172784/how-do-i-post-json-data-with-curl-from-a-terminal-commandline-to-test-spring-res)
3. [Review permissions?](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/nodejs-dynamodb-tutorial.html) I Think this is what fixed everything? However, TBH I am not sure. I'm also not sure if it's a good thing to just... blanket give permissions. I'm actually pretty sure this is a very bad thing. Oh well, learning! If you, reader, have any idea the "correct" way to do this, please PLEASE LMK [via email](mailto:aaroncaraway42@gmail.com)!! So much learning to do!! 
[See "Add Permissions to your Environment's Instances" section](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/nodejs-dynamodb-tutorial.html)
4. [withCredentials: true](https://stackoverflow.com/questions/46074177/node-js-same-request-works-on-localhost-but-not-on-aws-ec2-server) also might be a thing
5. annnnd it also might have just been this blanket permission add [AWSElasticBeanstalkFullAccess](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.managed-policies.html)


# TODO:
1. [USE THE LAMBDAS, LUKE](https://bitbucket.org/blog/deploy-an-express-js-app-to-aws-lambda-using-the-serverless-framework)
2. [Go back to express roots](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Express_Nodejs/skeleton_website)
3. [Express on Heroku](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Express_Nodejs/deployment)
4. [Understand the words on this page -- wtf is non-proxy integration](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-create-api-step-by-step.html)
5. [Maybe go back to these roots, too](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/getting-started-nodejs.html)
6. [this looks like a fun adventure!](https://aws.amazon.com/developer/)
7. Maybe play around with [php + aws](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/php-hawordpress-tutorial.html)

# RESOURCES:
[AWS Elastic Beanstalk docs](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_nodejs.resources.html)
[Dude's github](https://github.com/khelif96/React-S3-fileuploads/blob/master/backend/app.js)
[...from the original medium article](https://medium.com/@khelif96/uploading-files-from-a-react-app-to-aws-s3-the-right-way-541dd6be689)
