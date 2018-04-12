# heart_rate_databases_introduction
The following is a repository for the BME590 Databases Assignment (which can be found [here](https://github.com/mlp6/Medical-Software-Design/blob/master/Lectures/databases/main.md#mini-projectassignment)). 

The following program contains the functionality to store critical heart rate measurements into a mongodb database. Interactions with the database include two POST methods and three GET methods. The GET methods allow the user to search the database, using an email as a key, for the heartrates entered for the specific user and the times at which the heartrates occurred. There is also an additional GET method that allows the user to obtain the average heartrate over a specific period of time.

The two POST methods allow for the user to add to the database. This includes information like heartrates, the times of heartrates along with the email address to address the heart rates with.

# basic setup instructions
To set up this repository, the mongodb must be first setup to be running.

To do this, run 
```
docker run -v $PWD/db:/data/db -p 27017:27017 mongo
```

either on your local machine (if you have docker installed there) or on a virtual machine you have access to where you can first install docker.

to connect to the mongodb database from the flask server, include the following code in the flask script

```py
connect("mongodb://vcm-3579.vm.duke.edu:27017/heart_rate_app") # open up connection to db``

[![Build Status](https://travis-ci.org/asheu96/heart_rate_databases_introduction.svg?branch=master)](https://travis-ci.org/asheu96/heart_rate_databases_introduction)
