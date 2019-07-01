# Spark Introduction

### Spark Overview

* What is spark?
  * A fast and general engine for large-scale data processing
  * Spark distribute calculations among multiple machines

* Spark can run on top of a cluster manager
* Spark scripts are scripts that are written in Python, Java or Scala
* They are called a driver program that is located on the master node (one node)
* But under the hood when you run a driver program Spark knows how to take the
  work and run it on different machines, different CPU's 
* Spark runs on top of different cluster managers (own or yarn on top of a
  hadoop cluster)
* The cluster manager will split up the work and coordinate it among various
  executors so Spark will split up and create multiple executors per machine,
  ideally you want to have 1 executor per cpu core. And it can do all the
  coordiantion using the cluster manager and the driver program to do all the
  work itself to distribute it to all different nodes and give fault-tolerance
  if one of your executors goes down
* It scales horizontally 
* **From a developer view-point it's a simple program running on one computer
  (driver program) that feels like a lot of writing any other script**

![spark](https://spark.apache.org/docs/latest/img/cluster-overview.png)

* Run programs up to 100x faster then Hadoop MapReduce in-memory, or 10x faster
  on disk
* The way it can achive that performance is through DAG Engine (directed acyclic graph) optimizes workflows. If you need to calculate a result it creates a graph of different steps in order to achieve the results you want and it does that in an optimal manner
* It can wait until you asking for and figure out the optimal path to answer
  your question that you want
* Build around one main concept: the Resilient Distributed Dataset (RDD)


### The Reilient Distributed Dataset (RDD)
* Core object that everything is built around in Spark
* Dataset:
  * It's an abstraction for a giant set of data
  * The main thing you need to know as a developer, what you going to do is
    being setting up RDD objects and it's loading them up with big data sets and
    then calling various methods on the RDD objects to distribute that
    processing of that data 
  * You can use RDD object to transform that dataset from one set of data to
    another and perform actions on that dataset to actually get the results you
    want from it

![actions](https://www.alibabacloud.com/forum/attachment/1611/thread/22_621_16f9fe0e5e407f7.jpg)

* RDD's are both distributed and resilient, they can be spread out across an
  entire cluster of computers that may or may not be running locally they can
  also handle the failure of specific executor nodes in your cluster
  automatically and keep going even if one node shutsdown and re-distribute the
  work. You don't need to think about those things, this is what Spark does for
  you (cluster manager).
* The SparkContext
  * Created by your driver program
  * Once you have the SparkContext it is responsible for making RDD's resilient
    and distributed
  * Creates RDD's
  * The Spark shell creates a "sc" object for you
  * If we run a standalone script you need to create the `sc` object by hand and
    initialize it for you
  * The `sc` object gives all the methods to create an RDD
* From a programming standpoint you will be giving the **SparkContext** object.

```py
from pyspark import SparkConf, SparkContext
import collections

conf = SparkConf().setMaster("local").setAppName("RatingsHistogram")
sc = SparkContext(conf = conf)

lines = sc.textFile("file:///SparkCourse/ml-100k/u.data")
ratings = lines.map(lambda x: x.split()[2])
result = ratings.countByValue()

sortedResults = collections.OrderedDict(sorted(result.items()))
for key, value in sortedResults.items():
    print("%s %i" % (key, value))
``` 

* Creation of RDD's
  * nums = parallelize([1,2,3,4]) # take a hardcoded data and makes an RDD object out of it
  * sc.textFile('file..') # you can read a file
  * s3n://, hdfs:// # you can read a data from s3
  * hiveCtx = HiveContext(sc)
  * Can also create from:
    * JDBC
    * Cassandra
    * HBase
    * Elasticsearch
    * JSON, CSV, seq files, boject files etc.

* Transforming RDD's (transform an RDD): 
  * map - one to one relation 
  * flatmap - capability to produce multiple values
  * filter - filters the values from RDD
  * distinct - get unique values in RDD
  * smaple - get a sample for testing on large data set
  * union, intersection, subraact, cartesian - intersection between two RDD's
    and combine them or exclude

* Actions on RDD's (perform an action to get a result of RDD):
  * collect - print all the values 
  * count - count all values in RDD
  * countByValue - how many value occurs in RDD
  * take
  * top
  * reduce - combine alle the values to a key value, to get an aggregation of an
    RDD
  * and more...

* **Lazy Evaluation**: Nothing happens in your driver program until an action is called! Spark is so fast because it construct the DAG if you ask for an action to happen because at that point it knows what actually has to be done to get the results you want and it can compute the most optimal path to make that happen. It's important when you write your driver scripts is that your script isn't actually to do anything until you call one of the action methods. When you call an action it start to farm out your cluster or write it on your own computer whatever you told them to do and start executing that program.

```py
`from pyspark import SparkConf, SparkContext
# importing boilerplate SparkContext is the fundamental starting point to create RDD's and you cant create SparkContext without SparkConf - a configuration
import collections
# to sorting the files and results once we are done

conf = SparkConf().setMaster("local").setAppName("RatingsHistogram")
# it sets the master node as a local machine 
# there are extentions that you can split up upon different CPU's on a single machine
sc.stop()
sc = SparkContext(conf = conf)
# using the configuration object we create our SparkContext

lines = sc.textFile("u.data")
# we are loading the data file and create the RDD
# textFile() methods goes to a local filesystem and loads the file into RDD
# textFile() breaks the file into line by line, so that every line corresponds to a one value in your RDD

ratings = lines.map(lambda x: x.split()[2])
# the lambda functions splits up each line of strings by whitespaces and takes out the 2 element of the list which is the rating for the movie
# the data is immutable which means the original RDD doesn't changes, map function creates a new RDD
# the output / result of the map lambda are just ratings [3,3,1,2,1]
result = ratings.countByValue()
# it counts how many times each unique value in the RDD occurs  
# (3,2)
# (1,2)
# (2,1)
# IMPORTANT: An action returns a plain python object so now we can do regular stuff that we can do it python

sortedResults = collections.OrderedDict(sorted(result.items()))
for key, value in sortedResults.items():
    print ("%s %i" % (key, value))
# this is all python code there is nothing sparkish about it
# 1 2
# 2 1
# 3 2 
``` 
