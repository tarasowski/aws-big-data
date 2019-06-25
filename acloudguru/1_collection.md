# Introduction

### Kinesis Streams
* Scenarios:
  * Fast log and feed intake and processing
  * Real-time metrics and reporting
  * Real-time data analytics (e.g. for the website in realtime)
  * Complex stream processing (chaining streams together)

* Benefits:
  * Loading the aggregate data into a data warehouse / map reduce cluster
  * Real-time aggregation of data
  * Durability and Elasticity

* Methods to load/get data
  * Kinesis Producer Library (KPL) - any app that put records into Kinesis
    stream
  * Kinesis Client Library (KCL) - consumers get records and process them the
    consumers can emit data to lambda, s3, EMR, DynamoDB, Redshift
  * Kinesis REST API
  * Kinesis Agent

#### Kinesis Streams Core Concepts
* What is a shard?
  * Uniquely identified group of data records in a stream

* You can create multiple shards in a stream
  * Stream with 2 shards
  * 2MB/sec input
  * 4MB/sec input
  * 10 trans/sec for reads
  * 2000 records/sec for writes
  * Resharding:
    * Shard split to increate the capacity (divide 1 into 2)
    * Merge shards to reduce the capacity (combine)

* What is a record?
  * Unit of data stored in a stream
  * Partition key: 
    * Allows to group the data by shard
    * Tells you which shard the data belogs to
  * Sequence number:
    * Unique identifiers for records inserted into a shard
    * Think of it as a qunie key that identifies a data blob
    * Assigned when a producer calls PutRecord or PutRecords operations to add
      data to a stream
    * You can't use sequence number to distribute records among shards, you need
      a partition key for that
  * Data blob
    * Data blog is the data your data producer adds to a stream
    * The max. size of data blob is 1MB
  * Retention period:
    * 24hrs default
    * increase to 7 days
    * change the retention by CLI

* Data producers:
  * Streams Api
    * SDK for Java
      * PutRecord
      * PutRecords (higher throughput)
  * KPL (Producer Library)
    * Configurable library to create producer apps
    * Collects records to rwite multiple records to multiple shardds per request
    * Emits errors to CloudWatch
    * Should use if you want to write 1000 of events per second into Kinesis
      Stream
    * Don't use KPL if your producer app use case cannot incur an additional
      processing delay
    * Aggregation (batching)
      * better throughput: User records (actual data from server) and streams
        records
      * combines aggregation
    * Collection (batching)
      * Multiple streams records are batched and sent as a single http call
    * Read this post for more information: https://aws.amazon.com/blogs/big-data/implementing-efficient-and-reliable-producers-with-the-amazon-kinesis-producer-library/
  * Agent
    * Standalone Java Application
    * Web server, log server, database servers
    * Download and install the agent
    * Monitor multiple directories and write to multiple streams
    * Pre-process data before it gets sent to a stream

* Data consumers:
  * KCL
    * consume and process data from the stream
    * uses connector library to send the data to s3, redshift etc.
    * KCL handles compex tasks
    * Java, Node.js, Python
    * Runs on the ec2
    * Handles checkpointing with DynamoDB table (application state)

* For the exam:
  * Any kind of scenario where you are straming large amount of data that needs
    to be processed quickly and you have a requirement to build a custom
    application to process and analyze streaming data
  * You should know the capacity of shard, records, data producers (KPL), data
    consumer (KCL), additional throughput for DynamoDB exception errors

#### Emitting data to other AWS services

* Consumers can emit data to S3, DynamoDB, ElasticSearch, Redshift, EMR
* To emit the data, the consumer needs to use the consumers connect library
  (java)
* With EMR emit the data to S3 and consme the data from S3
* Spark Streaming can consume the data from Kinesis
* Use cases:
  * S3 - archiving data 
  * Dynamodb - for realtime metrics / live dashboard
  * Elasticsearch - searchable and indexing
  * Redshift - micro batching loading to use within the warehouses
    * If you need to consume the data in near-realtime you can load the data
      e.g. hourly into dwh
  * EMR - Process and Analyze data from the stream with the Spark Streaming
  * Lambda - Automate emitting data in order to emit the data to DynamoDB, S3,
    Redshift
* Kinesis Connector Library to send the data to other AWS services
  * Java based
  * Used with the Kinesis Client Library
  * Connectors for:
    * DynamoDb
    * Redshift
    * S3
    * ElasticSearch
  * Kinesis Connector Library is a pipeline for how records form the Kinesis
    Stream will be handled:
      * The records are retrieved from the stream
      * The records are transformed according to user data model
      * Buffered for batch processing
      * Emitted to the AWS service s. above
  * Pipeline workflow:
    * Kinesis Stream ->
    * iTransformer: defines the transformation of records from the Kinesis
      stream in order to suit the user-defined data model ->
    * iFilter: excludes irrelevant records from the processing ->
    * iBuffer: buffers the set of records to be processed by specifying size
      limit (# of records) & total byte count ->
    * iEmitter: makes client calls to other aws services and persists the
      records stored in the buffer  ->
    * S3, DynamoDB, ElasticSearch, Redshift
  * Interfaces and Classes:
    * S3Emittter class
      * Writes buffer content into a single file S3 (when the buffer is full)
      * Requires the configuration of an S3 bucket and endpoint
* For the exam:
  * Data can be emitted to S3, DynamoDB, Elasticsearch and Redshift from Kinesis
    Streams using the Kinesis Connector Library
  * Lamba function can automatically read records from a Kinesis Stream, process
    them and send the records to S3, DynamoDB or Redshift

### Firehose Core Concepts
  * Collect and loads stream data in near real-time
  * Load data into S3, Redshift, and Elasticsearch
  * Use existing BI tools and dashboards
  * Can batch and compress the data
  * Encrypt the data before it's loaded

