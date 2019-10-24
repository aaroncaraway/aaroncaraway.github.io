---
layout: single
title: 'AWS S3 + AWS Lambda = <3'
---

Following along with new best friend, [this dude](https://www.youtube.com/watch?v=V1nJ7ZJ_o44&list=PLD_RqipW0-9s-u1HXTglYV8Aam-5P3XLi&index=3)

## The setup

1. IAM > Roles > Create Role
    * Select `lambda`
    * Search `AWSLambdaExecute` in policies 
        -- This provides log access and s3 read/write access
    * Skip tags
    * Review: `lambda-s3-role` for name, all else same

2. S3 > Create Bucket 
    * unique name
    * click create on left side

3. Lambda > Create Function
    * Author from scratch
    * Create descriptive name like `putUserDataFromS3`
    * Make sure node.js 8 + selected
    * Choose existing role > select role we just created `lambda-s3-role`
    * Create Function

## The function

1. Create Trigger for S3
    * Designer > add trigger > s3
    * Configure Trigger
        -- bucket we just created
        -- event type: change to put (to only trigger when we upload)
        -- suffix (limit to just `.json`)
    * Add

2. Function Code

```javascript
const AWS = require('aws-sdk');
const s3 = new AWS.S3();

exports.handler = async (event) => {
    const { name } = event.Records[0].s3.bucket;
    const { key } = event.Records[0].s3.object;
    
    const params = {
        Bucket: name,
        Key: key
    }
    
    try {
        const data = await s3.getObject(params).promise();
        const usersStr = data.Body.toString();
        const userJSON = JSON.parse(usersStr);
        console.log(`Users ::: ${usersStr}`);
    } catch (err) {
        console.log(err)
    }
};
```

3. Test by uploading to bucket!
    * Go to bucket and upload json file
    * Go back to lambda page > Monitoring > Cloud watch
    * Click event, observe!

## Adding to the DB

1. Create Users Table (we did this in link-to-pt1)
    * Get the ARN 
    `Amazon Resource Name (ARN)	arn:aws:dynamodb:us-west-2:386305625872:table/Users`

2. Update IAM Role to have DB write permissions
    * Roles > `lambda-s3-role`
    * Add inline ppliciy
    * add service > dynamo DB
    * add actions `put item`
    * expand resources
    * paste in the ARN.
    * Review policy, give name `DynamoDBWritePolicy`
    * Create Policy

3. Update Lambda
    * Put first entry into data file

```javascript
const AWS = require('aws-sdk');
const s3 = new AWS.S3();
const documentClient = new AWS.DynamoDB.DocumentClient();

exports.handler = async (event) => {
    const { name } = event.Records[0].s3.bucket;
    const { key } = event.Records[0].s3.object;
    
    const getObjectParams = {
        Bucket: name,
        Key: key
    }
    
    try {
        const s3Data = await s3.getObject(getObjectParams).promise();
        const usersStr = s3Data.Body.toString();
        const usersJSON = JSON.parse(usersStr);
        console.log(`Users ::: ${usersStr}`);
        
        const { id, firstname, lastname } = usersJSON[0];
        
        const putParams = {
            TableName: "Users",
            Item: {
                id: id,
                firstname: firstname,
                lastname: lastname
            }
        }
        
        const putItemData = await documentClient.put(putParams).promise()
        console.log(putItemData);
        
    } catch (err) {
        console.log(err)
    }
};
```

4. Test!
    * Delete users.json and reupload 







