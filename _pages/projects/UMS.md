---
layout: single
title: "UMS"
permalink: /pages/UMS
tags: UMS
classes: wide
---

## Section 1: Fundamental Ideas Around Microservices

DONE 20200917

## Section 2: A Mini-Microservices App

### 9. App Overview

### 10. Project Setup

1. make project
2. npx cra client
3. mkdir posts
4. npm init -y
5. npm install express cors axios nodemon
6. mkdir comments
7. same as above

### 11. Posts Service Creation

WHAT DO YOU WANT YOUR SERVICE TO DO??

1. make index.js
2. const express = require('express
3.
4. app.get to posts and app.posts.posts
5. app.listen 4000, 90=>
6. posts = {}
7. randomly generate an id

GOAL: Listening on 4000 for posts

### 12. Testing the Posts Service

1. use postman

body

content-type application/json

### 13. Implementing a Comments Service

express
bodyparser
randomBytes
appuse bodyparser.jssn()

comments by post ID

### 14. Quick Comments Test

### 15. Note on the React App

### 16. React Project Setup

1. Delete all files inside src
2. GOAL: "Blog App" display on react app

### 17. Building Post Submission

1. PostCreate
2. Add Boostrap CSS CDN to anywhere inside the head
3. Add event handler

### 18. Handling CORS Errors

### 19. Fetching and Rendering Posts

1. make thing

### 20. Creating Comments

### 21. Displaying Comments

### 22. Completed React App

### 23. Request Minimization Strategies

### 24. An Async Solution

### 25. Common Questions Around Async Events

### 26. Event Bus Overview

### 27. A Basic Event Bus Implementation

1. create new event-bus app
2. install express nodemon axios

### 28. Emitting Events

inside posts
make the post request async
add axios inside it

await axios.post(our endpoint, our event object)

our event object:

type: 'PostCreated', data: {id, title}

### 29. Emitting Comment Creation Events

type CommentCreated
data: {
id: commentId,
content
postId: req.params.id
}

### 30. Receiving Events

### 31. Creating the Data Query Service

GOAL: We want a single service that connects posts and comments!

1. add query
2. i express cors nodemon

GOAL 2:

1. console log inside query from event bus
2. (event bus no more errors)
3. console log inside event bus as a response from query`

### 32. Parsing Incoming Events

### 33. Using the Query Service

### 34. Adding a Simple Feature

### 35. Issues with Comment Filtering

### 36. A Second Approach

### 37. How to Handle Resource Updates

### 38. Creating the Moderation Service

1. make boilerplate
2. on comment submit send to pending and send to moderation
3. on moderation finish, send back to comment
4. comment updates to queryservice

---

1. moderation
2. axios express nodemon
3. index.js
4. require statements
5.

### 39. Adding Comment Moderation

add property ststus: pending
add status to comment creation
add to query status
persist status

### 40. Handling Moderation

### 41. Updating Comment Content

### 42. A Quick Test

### 43. Rendering Comments by Status

### 44. Dealing with Missing Events

### 45. Implementing Event Sync

### 46. Event Syncing in Action

## Section 3: Running Services with Docker

## Section 4: Orchestrating Collections of Services with Kubernetes

## Section 5: Architecture of Multi-Service Apps

## Section 6: Leveraging a Cloud Environment for Development

## Section 7: Response Normalization Strategies

## Section 8: Database Management and Modeling

## Section 9: Authentication Strategies and Options

## Section 10: Testing Isolated Microservices

## Section 11: Integrating a Server-Side-Rendered React App

## Section 12: Code Sharing and Reuse Between Services

## Section 13: Create-Read-Update-Destroy Server Setup

## Section 14: NATS Streaming Server - An Event Bus Implementation

## Section 15: Connecting to NATS in a Node JS World

## Section 16: Managing a NATS Client

## Section 17: Cross-Service Data Replication In Action

## Section 18: Understanding Event Flow

## Section 19: Listening for Events and Handling Concurrency Issues

## Section 20: Worker Services

## Section 21: Handling Payments

## Section 22: Back to the Client

## Section 23: CI/CD

## Section 24: [Appendix A] - Basics of Docker

### 500 -- What is a container?

## Section 25: [Appendix B] - Basics of Typescript

## Section 26: Bonus!
