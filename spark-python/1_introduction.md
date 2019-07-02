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
  * union, intersection, subtract, cartesian - intersection between two RDD's
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
#### Key/value RDD
* We can put key/value pairs into RDD (more structured data) and treat it sort
  of like a database
* For example: number of firends by age
* Key is age, value is number of friends
* Instead of just a list of ages or a list of # of friends, we can store (age,
  # frieds), (age, # frieds)
* Nothing special in Python really
* If you store a (key, value) item than it's a key/value RDD
* Just map pairs of data into the RDD for example

```py
totalsByAge = rdd.map(lambda x: (x, 1))
```
* It's also to have a complex value (lambda x: (x, [1,2,3,4]))
* `reduceByKeys(): combine values witht the same key using some function
  `rdd.reduceBykey(lambda x, y: x + y) adds them up
* `groupByKey()` groups values with the same key
* `sortByKey()` sorts RDD by key values
* `keys(), values()` creates an RDD of just the keys, or just the values
* It's like a giant key value store (database), therefore you can do SQL-style
  joins on two key/value RDD'S
* `join, rightOuterJoin, leftOuterJoin, cogroup, subtractBykey`
* If your transformation doesn't affect the keys use `mapValues()` and
  `flatMapValues()` since it's more efficient

* Input Data: ID, name, age, number of friends

```
0,Will,33,385
1,Jean-Luc,33,2
2,Hugh,55,221
3,Deanna,40,465
4,Quarck,68,21
``` 

* The task is to figure out the average number of friends by age

```py
def parseLine(line):
  fields = line.split(',')
  age = int(fields[2]) # convert to int, to make arithmetic calculations later
  numFriends = int(fields[3])
  return (age, numFriends) # transforming into key/value RDD

lines = sc.textFile('fakefrinds.csv')
rdd = lines.map(parseLine)
# Output key/value pairs of (age, numFriends)
# 33,385
# 33,2
# 55,221
# 40,465
# 68,21

totalsByAge = rdd.mapValues(lambda x: (x, 1).reduceByKey(lambda x, y: (x[0] +
y[0], x[1] + y[1]))

# rdd.mapValues(lambda x: (x, 1))
# (33, 385) => (33, (385, 1))
# (33, 2) => (33, (2, 1))
# (55, 221) => (55, (221, 1))
# reduceByKey(lambda x,y: (x[0] + y[0], x[1] + y[1]))
# Adds up all values for each unique key!
# (33, (387, 2))

averagesByAge = totalsByAge.mapValues(lambda x: x[0] / x[1])
# (33, (387, 2)) => (33, 193.5)
results = averagesByAge.collect()
for result in results:
  print(result)
sc.stop() # use sc.stop() to close the context on the local machine
```
* In the example above we have a compex type as a value `(33, (385, 1))`

* Nothing happens in Spark until the first action is called, the first action
  here is `reduceByKey()`

* The other actions `collect()`. 

* Spark goes and figure out the optimal way to compute before the action is
  called (DAG), that's why spark is so fast.

#### Filtering RDD's
* Strip information from an RDD and create a smaller RDD
* Just takes a functin that returns a boolean
* For example, we want to filter out entries that don't have `TMIN` in the first
  item of a list of data:

```py
minTemps = parsedLines.filter(lambda x: 'TMIN' in x[1])
``` 

* Input data snippet:

* weatherStation id, date, obeservation type, temperatur
```csv
ITE001,1800101,TMAX,-75,,,E,
ITE001,1800101,TMIN,-148,,,E,
GM00018,1800101,PRCP,0,,,E,
EZE00018,1800101,TMAX,-86,,,E,
EZE00018,1800101,TMIN,-135,,,E
``` 

```py
def parseLine(line):
  fileds = line.split(',')
  stationID = fields[0],
  entryType = fields[2]
  temperature = float(fields[3]) * 0.1 * (9.0 / 5.0) + 32.0 # fahrenheit
  converion
  return (stationID, entryType, temperature) # composite value out of primitive
  values - complex data type

line = sc.textFile('1800.csv')
parsedLines = lines.map(parseLine)
minTemps = parsedLines.filter(lambda x: 'TMIN' in x[1])
stationTemps = minTemps.map(lambda x: (x[0], x[2])) # stripping out the TMIN
value
minTemps = stationTemps.reduceByKeys(lambda x, y: min(x,y)) # combine the x and
y value and take the min value
results = minTemps.collect()
for result in results:
  print(result[0] + "\{:.2f}F".format(result[1]))
``` 

#### flatMap() Count Words (map vs. flatMap)

* map() transforms each element of an RDD into one new element. There is always
  one to one relationship, map has to obey some laws such as identity,
  composition.

```py
lines = sc.textFile('redfox.txt') 
# The quick red 
# fox jumped 
# over the lazy 
# brown dogs
rageCaps = lines.mpa(lambda x: x.upper()) 
# THE QUICK RED 
# FOX JUMPED
# OVER THE LAZY 
# BROWN DOGS
``` 

* flatMap() can create many new elements from each one 
* When you use flatMap() you can end up with an RDD that has more elements that
  you started with

```py
lines = sc.textFile('redfox.txt') 
# The quick red 
# fox jumped 
# over the lazy 
# brown dogs 
words = lines.flatMap(lambda x: x.split()) 
# The
# quick
# red
# fox
# jumped
# over
# the 
# lazy
# brown
# dogs
``` 

* In the example above it splits a line into multiple lines and output multiple
  results. It returns a list of words and each item will become an entry of it's
  own on the RDD. The `words` RDD end's up containing each individual word.
  Where we started with 4 items in the original RDD one for each line, now it
  has more elements

```py
from pyspark import SparkConf, SparkContext


conf = SparkConf().setMaster('local').setAppName('Book')
sc.stop()
sc = SparkContext(conf = conf)

input = sc.textFile('Book.txt') 
# load up a text one line at the time, it's broken out into one paragraph per line

words = input.flatMap(lambda x: x.split())
# will take every individual line of text, breaks the line based on the
whitespace into individual words
wordCounts = words.countByValue()
# countByValue() is a way to get how many times each unique value occurs
# for every whitespace separated word in the book, we get how many times that
word occurs

for word, count in wordCounts.items():
    cleanWord = word.encode('ascii', 'ignore')
    if (cleanWord):
        print(cleanWord, count)

sc.stop()
``` 

* Text normalization: 
  * Problem: word variants with different capitalization, punctuation, etc.
  * There are fancy natural language processing toolkits like NLTK, but we'll
    keep it simple, and use a `regular expression`

```py
import re
from pyspark import SparkConf, SparkContext


conf = SparkConf().setMaster('local').setAppName('Book')
sc.stop()
sc = SparkContext(conf = conf)

def normalizeWords(text):
    return re.compile(r'\W+', re.UNICODE).split(text.lower())

input = sc.textFile('Book.txt')
words = input.flatMap(normalizeWords)
wordCounts = words.countByValue()

for word, count in wordCounts.items():
    cleanWord = word.encode('ascii', 'ignore')
    if (cleanWord):
        print(cleanWord, count)

sc.stop()
```
* Sorting the results
  * We cloud sort what countByValue() returns, but let's use RDD's to keep it
    scalable
  * First, do countByValue() the 'hard way':
  * This is an example below what `countByValue()` actually does under the hood
  * By doing this we can make our code scalable instead store values as a python
    variable (data structure) we use the Spark code to make it scalable. In the
    example above we store the result of `countByValue()` in a python data
    structure, because `countByValue()` is an action.

```py
wordCounts = words.map(lambda x: (x, 1)).reduceByKey(lambda x, y: x + y)
```
* Convert each word to a key/value pair with a value of 1
* Then count them all up with `reduceByKey()`

* Flip the (word, count) pairt to (count, word)
* Then use sortByKey() to sort by count (not that count is our new key)

```py
wordCountsSorted = wordCounts.map(lambda (x, y): (y, x)).sortByKeys()
```
