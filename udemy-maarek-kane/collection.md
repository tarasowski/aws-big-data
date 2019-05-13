# Collection Introduction

* RealTime Collection - Where we can perform immediate action on our data 
  * All these services allow you in your application to react realtime events or
    data that is happening in your infrastructure
  * Kinesis Data Streams (KDS)
  * Simple Queue Service (SQS)
  * Internet of Things (IoT)

* Near-real time - Reactive actions
  * Kinesis Data Firehose (KDF)
  * Database Migration Service (DMS)

* Batch - Historical Analysis (not very close to realtime). Is needed when you
  want to move large amount of data for historical analysis into AWS to do some
  big data analysis on that.
  * Snowball
  * Data Pipeline

## AWS Kinsis Overview

* An very important exam topic and overall a collection topic for AWS if you
  want to perform big data.

* Kinesis is a managed alternative to Apache Kafka. It's great to gather data in
  realtime
* Great for application logs, metrics, IoT, clickstreams
* Great for "real-time" big data
* Integrates with streaming processing frameworks (Spark, NiFi, etc...)
* Data is automatically replicated synchronously to 3 AZ (highly available
  setup)

### Kinesis services

* Kinesis Streams: low latency streaming ingest at scale (low latency describes
  a computer network that is optimized to process a very high volume of data
  messages with minimal delay (latency).
* Kinesis Analytics: perform real-time analytics on streams using SQL
* Kinesis Firehose: load streams into S3, Redshift, ElasticSearch & Splunk


### Architecture of Kinesis

* Amazon Kinesis:
  * Streams: can take data from click streams, OoT devices (e.g. connected bike), Metrics & Logs
  * Analytics: if you want to analyse data in realtime e.g. you want to build
    alerts
  * Firehose: when you have all your data and you want to store it somewhere for
    later analysis (visualization) - near real-time --> Redshift, S3, Splunk,
    ElasticSearch

### Kinesis Streams
* Streams are diviced in ordered Shards / Partitions
* Data retention is 24 hours by default, can go up to 7 days (time to consume
  the data)
* Ability to reprocess / replay data. Once you processed that data the data is
  not gone from Kinesis streams, it will be gone based on data retention period.
  But you are able to read over the same data as long as the retention period
  is.
* Multiple applications can consume the same stream
* Real-time processing with scale of throughput. 
* Kinesis stream is not a database. Once data is inserted in Kinesis, it can't
  be deleted (immutability). It's an append only stream

#### Kinesis Streams Shards
* One stream is made of many different shards or partitions
* Billing is per shard provisioned, can have as many shards as you want
* Batching available or per message calls
* The number of shards can evelove over time (reshard / merge)
* Records are ordered per shard. They are ordered based on the information when
  they were received.

#### Kinesis Streams Records
* What is a record made of?
  * Data Blob: data being sent, serialized as bytes. Up to 1 MB.
    Can represent anything - 1MB
  * Record Key:
    * sent alongside a record, helps to group records in Shards. Same key = Same
      shard. The key helps Kinesis to which shard to send that data to.
    * Use a highly distributed key to avoid the "hot partition" problem. The key
      has to be super distrubuted. You can choose e.g. user Id if you have a
      million users and they will allow you to avoid the hot partition problem
      where all the data goes to the same shard.
  * Sequence number: Unique identifier for each records in put in shard. Added
    by Kinesis after ingestion (not made by producer)

#### Kinesis Data Streams Limits to know
* Producer:
  * 1 MB/s or 1000 messages/s at write PER SHARD (if you have 10 shards, you'll
    get 10MB/s or 10.000 messages)
  * If you go over that limit you'll get "ProvisionedThroughputException"
    otherwise 
* Consumer Classic:
  * 2 MB/s at read PER SHARD across all consumers
  * 5 API calls per second PER SHARD across all consumers
* Consumer Enhanced Fan-Out:
  * 2 MB/s at read PER SHARD, PER ENHANCED CONSUMER
  * No API calls needed (push model)
Data Retention:
  * 24 hours data retention by default
  * Can be extended to 7 days

#### Kinesis Producers
* How can we produce data in Kinesis?

  * **Kinesis SDK**: allows you to write code or use the CLI to directly send data
  into Amazon Kinesis Streams. Uses PutRecrod(s) API
    * APIs that are used are PutRecord (one) and PutRecords (many records)
    * PutRecords uses batching and increases throughput => less HTTP requests
    * If you go over your througput you'll get ProvisionedThroughputExceeded if
      you go over the limits
    * + AWS Mobile SDK: Android, iOS, etc.
    * **When to choose to use producer SDK**: low throughput, higher latency,
      simple API, AWS Lambda
    * Managed AWS sources for Kinesis Data Streams:
      * CloudWatch Logs, you can send your logs directly into Kinesis
      * AWS IoT
      * Kinesis Data Analytics
    * Kinesis API - Exceptions:
      * ProvisionedThroughputExceeded Exceptions: Happens when sending more data
        (exceeding MB/s or TPS for any shard)
        * Make sure you don't have a hot shard (such as your partition key is
          bad and too much data goes to that partition) e.g. you have a device
          id as the key and 99% of devices are being iPhones, you're going to
          get a hot key
      Solution:
        * Retries with backoff. Retry maybe after 2 seconds, if no working try
          in 4 seconds, 8 seconds etc.
        * Increase shard (scaling)
        * Ensure your partition key is a good one (very distributed one)


  * **Kinesis Producer Library (KPL)**: The library has some advanced features and
    allows you to write better code. Allows to get enhanced throughput into
    Kinesis stream.
      * Easy to use and highly configurable C++/ Java library
      * Used when you want to build high performance, long-running producers
      * Automed and configurable retry mechanism (in the SDK there is no such a
        mechanism built-in)
      * It has two kinds of API:
        Synchronous: the same as the SDK
        Asynchronous API (better performance for async)
      * In the exam if we need to send data asynchronously, usually Kinesis
        Producer Library (KPL) is the way to do it
      * Submits metrics to CloudWatch for monitoring. Everytime you write an
        application with KPL, you can monitor it in CloudWatch.
      * It supports **Batching** (both turn don by default) - increase
        throughput, decrease cost: 
          * **Collect** Records and Write to multiple shards in the same
            PutRecords API call
          * Aggregate - increased latency 
            * Capability to store multiple records in one record (go over 1000
              records per second limit)
            * Increase payload size and imporive throughput (maximize 1MB/s
              limit)
      * Compression must be impleted by the user
      * KPL Records must be de-coded with KCL or special helper library 
      * Kinesis Producer Library KPL Batching:
        * We're sending a record to Kinesis of 2kb. It's not going to be sent
          right away, it's going to see if more records are coming in. The next
          record is of 40kb, the next record is of 500kb. The producer Library
          will at some point aggreate it into One Record < 1MB. So instead of
          sending 3 records now, we're sending 1 Record and it's still less than
          1MB.
        * Here we have Aggregation to aggreate records into 1 < MB. And we can
          put all the records into a collection of PutRecords. The producer
          Library will at some point aggreate it into One Record < 1MB. So
          instead of sending 3 records now, we're sending 1 Record and it's
          still less than 1MB.
        * Here we have Aggregation to aggreate records into 1 < MB. And we can
          put all the records into a collection of PutRecords.
        * How does Kinesis knows how long to wait to aggregate a Record? We can
          infulce the batching efficiency by introducing some dely with
          RecordMaxbufferedTime (default 100ms)

  * **Kinesis Agent**: is a linux program that runs on a server and allows to get a
    log file and send that reliably to Kinesis streams (log aggregation at
    scale)
      * Monitor log files and sends them to Kinesis Data Streams
      * java-based agent, buiilt on top of KPL
      * Install in Linux-based server environments
      * Features:
        * Write from multiple directories and write to multiple streams
        * Routing feature based on directory / log file
        * Pre-process data before sending to streams (single line, csv, to json,
          log to json)
        * The agent handles file rotation, checkpointing, and retry upon
          failures
        * Emits metrics to CloudWatch for monitoring

  * **3rd pary libraries**: Spark, Log4j, Appenders, Flue, Kafka Connect, Nifi
