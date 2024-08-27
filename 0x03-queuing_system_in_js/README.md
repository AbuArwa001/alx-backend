# 0x03. Queuing System in JS

## Overview
This project involves creating and managing a queuing system using Redis and Node.js. You will learn to perform basic Redis operations, use Kue for queuing, and build an Express application that interacts with a Redis server.

## Resources
- [Redis Quick Start](https://redis.io/topics/quickstart)
- [Redis Client Interface](https://redis.io/commands)
- [Redis Client for Node.js](https://www.npmjs.com/package/redis)
- [Kue Documentation (Deprecated but still used)](https://github.com/Automattic/kue)

## Learning Objectives
By the end of this project, you should be able to:
- Run a Redis server on your machine.
- Perform simple operations using the Redis client.
- Use a Redis client with Node.js for basic operations.
- Store hash values in Redis.
- Handle async operations with Redis.
- Implement a queuing system using Kue.
- Build a basic Express app interacting with a Redis server.
- Build an Express app interacting with both a Redis server and a queue.

## Requirements
- All code should run on Ubuntu 18.04, Node 12.x, and Redis 5.0.7.
- All files should end with a new line.
- A `README.md` file at the root of the project directory is mandatory.
- Your code should use the `.js` extension.

## Project Setup
1. **Install Redis:**
    ```bash
    $ wget http://download.redis.io/releases/redis-6.0.10.tar.gz
    $ tar xzf redis-6.0.10.tar.gz
    $ cd redis-6.0.10
    $ make
    $ src/redis-server &
    ```

2. **Redis Client Installation:**
    Install the Node.js Redis client:
    ```bash
    $ npm install redis
    ```

3. **Create Required Files:**
    - `package.json`
    - `.babelrc`
  
    **Note:** Remember to run `$ npm install` after setting up `package.json`.

## Tasks

### 0. Install a Redis Instance
- Compile and start the Redis server.
- Set and get key-value pairs using the Redis CLI.

### 1. Node Redis Client
- Create a script `0-redis_client.js` that connects to the Redis server.
- Log connection success or failure messages.

### 2. Node Redis Client and Basic Operations
- Create a script `1-redis_op.js` to set and get key-value pairs in Redis using callbacks.

### 3. Node Redis Client and Async Operations
- Modify the previous script (`2-redis_op_async.js`) to use Promises and async/await.

### 4. Node Redis Client and Advanced Operations
- Store and retrieve hash values in Redis using a script `4-redis_advanced_op.js`.

### 5. Node Redis Client Publisher and Subscriber
- Create `5-subscriber.js` and `5-publisher.js` scripts to implement a basic publish/subscribe system in Redis.

### 6. Create the Job Creator
- Create a script `6-job_creator.js` using Kue to create and manage jobs in a queue.

### 7. Create the Job Processor
- Create a script `6-job_processor.js` to process jobs from the queue created in the previous task.

## How to Run
- Ensure Redis is running on your local machine.
- Use `npm run dev <script_name.js>` to execute the scripts.

## Repository Structure
