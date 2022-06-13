# RESTapis

Statistics via RESTful APIs
===========================
Using RESTful APIs to calculate statictis (average, sum and standard deviation)
POST, GET, DELETE methods implemented with Python and saved in JSON format.



Environment
===========
Docker 20.10.16
Python 3.8.10


Usage
=====
The Dockerfile builds an image which will launch the RESTful APIs 

In terminal run the following **commands**:

1. **sudo apt-get update** (check for any updates)
2. **sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin** (install Docker Engine)
3. **docker build --file Dockerfile -t ANYTAG .**
4. **docker run -d -p 12000:22 ANYTAG:latest**

