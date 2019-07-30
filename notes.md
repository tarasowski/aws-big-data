# My Notes from the Web or Other Courses

### Amazon Kinesis Analytics Streaming SQL Concepts

* In-Application Streams and Pumps: When you configure application input, you
map a streaming source to an in-application stream that is created. Data flows
from the streaming source into the in-application stream. An in-application
stream works like a table that you can query using SQL statements, but it's
called a stream because it represents continuous data flow

* Timestamps and the ROWTIME Column: In-application streams include a special
column called ROWTIME. It stores a timestamp when Amazon Kinesis Data Analytics
inserts a row in the first in-application stream. 

* Continuous Queries: A query over a stream executes continuoulsy over streaming
data. This continuous execution enables scenarios, such as the ability for
application to continuously query a stream and generate alerts

* Windowed Queries: For a time-based windowed query, you specify the window size
in terms of time. This requires a timestamp column in your in-application stream
that is monotonically increasing (The timestamp for a new row is greater than or
                                  equal to the previous row)
  * Stagger Windows: A query that aggregates data using keyed time-based windows
that open as data arrives. The keys allow for multiple overlapping windows. For
example, VPC Flow logs have a capture window of approximately 10 minutes. But
they can have a capture window of up to 15 minutes if you're aggregating data on
the client. Stagger windows are ideal for aggregating these logs for analysis.
  * Tumbling Windows: A query that aggregates data using distinct time-based
windows that open and close at regular intervals
  * Sliding Windows: A query that aggregates data continuously, using a fixed
time or rowcount interval

### KPL Key Concepts

* A KPL user record is a blog of data that has particular meaning to the user.
examples include a JSON blog prepresenting a UI event on a website, or a log
entry from a web server

* A Kinesis Data Streams record is an instance of the Record data structure
defined by the Kinesis Data Streams service API. It contains a partition key,
sequence number, and a blog of data
  
#### Batching

* Batchins refers to performing a single action on multiple items instead of
repeatedly performing the action on each individual item
* In this context the item is a record and the action is sending it to Kinesis
Data Streams. In a non-batching situation, you would place each record in a
separate Kinesis Data Streams record and make one HTTP request to send it to
Kinesis Data Streams. With batching, each HTTP request can carry multiple
records instead of just one.
* The KPL supports two types of batching:
  * Aggregation - Storing multiple records within a single Kinesis Data Streams
record. Aggregation allows customers to increase the number of records sent per
API call, which effectively increases producer thorughput. Kinesis Data Streams
shards support up to 1,000 Kinesis Data Strems records pe second, or 1MB
throughput.

  * Collection - Using the API operation PutRecords to send multiple Kinesis
Data Streams records to one or more shards in your Kinesis data stream. This
increases throughput compared to using no collection because it reduces the
overhead of making many separate HTTP requests. Collection differs from
aggregation in that it is working with groups of Kinesis Data Streams records.
The Kinesis Data Streams records being collected can still contain multiple
records from the user.

```
record 0 --|
record 1   |        [ Aggregation ]
    ...    |--> Amazon Kinesis record 0 --|
    ...    |                              |
record A --|                              |
                                          |
    ...                   ...             |
                                          |
record K --|                              |
record L   |                              |      [ Collection ]
    ...    |--> Amazon Kinesis record C --|--> PutRecords Request
    ...    |                              |
record S --|                              |
                                          |
    ...                   ...             |
                                          |
record AA--|                              |
record BB  |                              |
    ...    |--> Amazon Kinesis record M --|
    ...    |
record ZZ--|
``` 


# Whizlab Exam Iterations

* Kinesis Analytics which options support collection, processing and playback of
videos on demand?
  * Creation, procesing are managed by Kinesis Video Streams while extraction of
data from media sources is supported by Producer library
  * HTTP live straming HLS or GetMedia API support viewing an Amazon Kinesis
video strea, either for live playback or to view archived video
    * HTTP Live Streaming HLS is an industry-standard HTTP-based media streaming
      communication protocol. You can use HLS to view Kinesis video streams for live
      playback or to view archived video
    * GetMedia API allows building own apps to process Kinesis video streams.
  * Kinesis Video Streams supports live playback or to view archived view
through Kinesis Video Streams console

* AWS ML
  * Amazon ML uses logistic regression algorithm through binary classificatin to
solve the business problem
  * Amazon ML uses Area Under the (Receiver Operating Characteristic) Curve
(AUC) to provide accuracy of the model
  * Cross-validation is a technique for evaluating ML models by training several
ML models on subsets of the available input data to detect overfitting which
eventually fails to generalize the pattern

* PMG Group has a lot of exisitng cusomter. They launched a campaign to sell new
products. Management want to know the top 50 books and their quantity very day
that will be sold
  * Multinominal Regression algorithm addressing Multi-class classification
  * Cross-validation for evaluating ML model sto detect overfitting

* HH is using kinesis analytics to build SQL querying capability ons treaming
and palling to use windowed queries to process the data. What kind of windows
queries need to be used to aggregate data continuously, suing a fixed time or
rowcount interfval for e.g. after 1 minute or after 2000 rows
  * Sliding windows queries


* ML Model Insights
  * When you evaluate ML model, AWS provides metric and a number of insights to
review the predictive accuracy of your model:
    * A prediction accuracy metric to report on the overall success of the model
    * Visualization to help explore the accuracy of your model beyond the
prediction accuracy metric
    * The ability to review the impact of setting a score threshold
    * Alerts on criteria to check the validity of the evaluation

* Recommendation of new products based on the history:
  * AWS ML uses multi-nominal logistic regression algorithm through multi-class
classification to solve the business problem
  * Cross-validation is a technique for evaluation ML models by training several
ML models on subsets of the available input data to detect overfitting which
eventually fails to generalize the pattern
  * Amazon uses macro-average F1 score to provide accuracy of the model


# Big Data Architectural Patterns

[Source](https://www.youtube.com/watch?v=a3713oGB6Zk)
[Slides](https://www.slideshare.net/AmazonWebServices/abd201big-data-architectural-patterns-and-best-practices-on-aws?qid=50b8b8c9-ebf7-4c12-9c5c-acde09a1547f&v=&b=&from_search=1)

### Ever increasing big data:
* Volume
* Velocity
* Variety
  * In addition to text, we are getting audit (siri, alexa) and video 

### Big Data Evolution
* Batch processing (Hive) - 10 years ago
  * Stream processing (real-time stream processing) - now
    * Artifical Intelligence: take the pipelines and make batch and real-time predictions
      * Virtual machines (ec2 instnances with ebs and local disks with your
                          software)
        * Managed services (RDS + EMR)
            * Serverless (DynamoDb, you simply specify what you want here is the
                          table here is the primary key, you don't worry about
                          servers, you worry about your programming abstractions)

### Big data challenges?
* Is there a reference architecture?
* What tools should I use?
* How?
* Why?
* How I enable IA of to my application?


### Architectural principles?
* Build decouples systems:
  * Data -> Store -> Process -> Store -> Analyze -> Answers
  * Decouple storing from compute (we replaced Hive to Spark)
* Use the right tool for the job
  * Data structure, latency, throughput, access patterns
  * If we do build a tool, we want to cover 1-2 cases very well
  * One size doen't fit all
* Leverage managed and serverless services
  * Scalalbe/elastic, available, reliable, secure, no/low admin
* Use log-centric design patterns
  * Immutable logs (data lake), materialized views
  * In many question we don't know the questions some one will ask, you need to
have appended structure / immutable data. You can store historical data, and if
you want to build a model you can use that data, you don't need to get a new
data set for that, **DON'T DELETE ANYTHING**
  * Materialized view: If you have services like elastic search or data
warehouse, you can see these services as simply a VIEW on top of your immutable
data. That you will put in your data in your data lake. Your data lake is like a
blockchain, a big immutable ledger
* Be cost-conscious
  * Big data not equal big costs, pick the cheapest service
* Think of IA/ML enable your applications:
  * Think about if you collect some data, if you need later to enable AI/ML
how/what should I collect

### Simplify Big Data Processing

* Data --> Collect --> Store ---> Process/Analyze ---> Consume ---> Answers
  * Store --> Process/Analyze is in cycle, you go forth and back

* Pipeline latency how long you have time to answer. How fast you want your data
to be materialized (Latency)
  * What is the view, or report, let me shape the data in form of your report 
* Pipeline Throughput, how much data will be processed per second
* Costs: how much are you going to pay for this application


### Data Characteristics

![cold](./img/data-temp.png)

* Having the sense with what type of data you're dealing helps you to pick the
right tools


### Collect

![data types](./img/data-types.png)


### Why Stream Storage?
* Decouple producers & consumers
* Persistent buffer (24hr to 7 days)
* Collect multiple streams
* Preserve client ordering (producer data will get to specific shard always - so
                            you build windows or make some analysis min/max on
                            data)
* Parallel consuming
* Streaming MapReduce


### What about AWS SQS
* No client ordering
* No streaming MapReduce (no separation into partitions)
* No parallel consuming
  * Visibility timeout - if one client consume something, the other consumers
can't see the message
* Data can be retrieved only once and gets deleted


![compare](./img/comparison.png)

* Important: If you're using Kinesis there could be the case that the records
are doubled. You should deduping your system using DynamoDB. But in Kafka it's
already built-in.

### Use S3 as Your Persistent File Store
* Natively supported by big data frameworks (Spark, Hive, Presto)
* Decouple storage and compute
  * No need to run compute clusters for storage (unlike HDFS)
  * Can run trnasient EMR clusters with EC2 Spot Instances
  * Multiple & heterogeneous analysis clusters and services can use the same data

### What About HDFS & Data Tiering
* More and more HDFS is used like a cache for your hot data sets
* Use HDFS for hottest datasets (e.g. interative read on the same datasets)
* Use S3 different tiers for different data temperature
* Use S3 Aanlytis to otpimize tiering strategy


### Materilaized View
* Application ---> DynamoDB ----> Stream ----> Lambda ---> S3 Immutable log / Kinesis Consumer --->
EalsticCache Cache View ---> CloudSearch Search View


![mat-view](./img/mat-view.png)


### Which data store should i use?

* You store the data in the form you access it
* Data structure -> Fixed schema, JSON, Key/Value
* Access patterns -> Store data in the form you access it
* Data characteristics -> Hot, warm, cold
* Cost - Right cost

* Data structure
  * Fixed Schema: SQL, NoSQL
  * Schema-free (JSON): NoSQL, Search
  * Key/Value: In-memory, NoSQL
  * Graph: GraphDB
* Access patterns
  * Put/Get (key, value): In-memory, NoSQL
  * Simple relationships -> 1:N, M:N: NoSQL
  * Multi-table joins, transaction, SQL: SQL
  * Faceting, Search: Search (Elastic Search)
  * Graph traversal: GraphDB

* Faceted search is a technique which involves augmenting traditional search techniques with a faceted navigation system, allowing users to narrow down search results by applying multiple filters based on faceted classification of the items. Basically the amazon.com search on the website

![map](./img/map.png)


![map2](./img/map2.png)


![pricing](./img/price.png)


### Predictive Analytics
* API Driven Services
  * Amazon Lex - Speech recognition
  * Amazon Polly - Text to speech
  * Amazon Rekognition - Image analysis
  * Amazon Comprehension - Text classification
* Managed ML Platforms
  * Amazon ML
  * Spark ML on EMR
* Deep Learning AMI (Amazon Machine Learning)
  * Pre-instlal with MXNet, TensorFlow, Caffe2, Theano, Torch, Keras


### Interactive and Batch Analytics
* Amazon ES
  * Managed Service for Elasticsearch
* Amazon Redshift and Amazon Redshift Spectrum
  * Managed Data Warehouse
  * Spectrum enables querying S3
* Amazon Athena
  * Serverless Interactive Query Service
* Amazon EMR
  * Hadoop, Spark, Flink, Presto, Tez, Hive, Pig, HBase


### Stream / Real-time Analytics
* Spark Streaming on EMR
* Kinesis Analytics
* Kinesis KCL (library for stream processing - checkpointing)
* AWS Lambda


### Which Analytics Should I use?

![analytics](./img/analytics.png)


### Which Stream Processing Technology Should I use?

![streaming](./img/streaming.png)


### Which Analytics Tools Should I use?

![analytics](./img/analytics2.png)


![full map](./img/full-map.png)


![mental map](./img/mental-map.png)


![data lake](./img/data-lake.png)


![summary](./img/summary.png)
