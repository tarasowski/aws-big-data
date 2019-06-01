# AWS Service Integrations

### IoT

* IoT Topic -> IoT rules -> IoT Rules Actions -> sends data to places such as:
  Kinesis, DynamoDB, SQS, SNS, S3, Lambda + many others 

### Kinesis Data Streams
* Producers: SDK, KPL, Kinesis Agent, Spark, Kafka connect
* Consumers: Spark, Kinesis Connect Library, SDK, KCL, Lambda, Firehose

### Kinesis Data Firehose
* Producers: SDK (Kinesis), Kinesis Agent, Kinesis Data Streams, CloudWatch Logs
  & Events, IoT rules actions
* Transformation: AWS Lambda
* Consumers: S3, Splunk, Redshift, ElasticSearch 

### Kinesis Data Analytics
* Producers: Kinesis Data Streams, Kinesis Data Firehose, Referece Data (JSON,
  CSV) in S3
* Transformation: AWS Lambda
* Consumers: Kinesis Data Streams, Kinesis Data Firehose, AWS Lambda

### SQS
* Producers: SDK-based application EC2, ECS etc, IoT Core (Rules Engine), S3
  events (new files)
* Consumers: SD-based application EC2, ECS, etc, AWS Lambda

### S3
* Producers: Snowball, Snowball Edge, Firehose, Redshift (uploads data to S3), Athena (queries and
  writes to), Data Pipeline, IoT Core, AWS DMS, EMR (EMRFS), Glue (as target)
* Consumers: AWS Lambda, SQS Queue, SNS Topic 

### DynamoDB
* Producers: Client SDK, DMS (Database Migration Service), Data Pipeline (batch
  processing)
* Consumers: Glue (will get all the tables metadata information into it's catalog), EMR (can read using Hive, can scan the entire table), DynamoDB Streams -> Lambda, Kinesis Client Library

### Glue
* Producers: DynamoDB, S3, JDBC based (RDS)
* Transformation: Glue Crawlers + Glue Data Catalog (can be used by different
  technologies to query data - Athena, Hive, Spectrum)


### EMR
* Producers: S3 / EMRFS, DynamoDb, Apache Ranger on Ec2 (for controlling access
into EMR cluster), Glue Data Catalog (to know what to query)
* Consumers: S3 / EMRFS
* Modules: Spark, Hadoop, Presto, HBase, Jupyter, Hive, Pig, Flink

### Amazon Machine Learning
* Producers: S3, Redshift
* Prediction API that spils out the data

### Amazon SageMaker
* Producers: only S3
* When we deploy the model we can run predictions whenever we want
* Modules: TensorFlow, Tytorch, Mxnet

### AWS Data Pipeline
* It's batch-related
* Activies: S3, JDBC (e.g. RDS), EMR / Hive, DynamoDB

### ElasticSearch Service
* Producers: Kinesis Data Firehose, IoT Core, CloudWatch Logs
* Consumers: ElasticSearch, Kibana, Logstash
* Access: IAM and Cognito

### Athena
* Producers: S3, Glue Data Catalog
* Integration: QuickSights
* Consumers: S3

### Redshift
* Producers: S3 (COPY / LOAD / UNLOAD)
* Integration: Quicksight (can be used to query your data warehouse in
  redshift), PostgreSQL (DBLINK to replicate some data)

### QuickSight
* Producers: RDS / JDBC, Redshift, Athena, S3, Jira, Excel, Teradata, Salesforce

### Instace Types for Big Data
* General Purpose: T2, T3, M4, M5 (webserver)
* Compute Optimized: C4, C5 (C stands for compute) 
  * Batch processing, distributed analytics, machine deep learning
* Memory Optimized: R4, R5, X1, Z1d (R stands for Ram)
  * High performance database, in-memory database, real time big data analytics:
    Spark
* Accelerated Computing: P2, P3, G3, F1
  * GPU instances, Machine or Deep Learning, High Preformance Computing:
    TensorFlow
* Storage Optimized: H1, I3, D2
  * Distributed File System (HDFS), NFS, Map Reduce, Apache Kafka, Redshift (D2)
  * Lot of data written or read from the disk

### EC2 for Big Data
* On demand, Spot & Reversed instances:
  * Spot: aws can take it at any time, can tolerate loss, low cost => chechpointing features (ML, etc): Machine Learning, Spark
  * Reserved: long running clusters, database or rds database (over a year)
    you'll get a discount for reserverd
  * On demand: remaining workloads
* Auto Scaling:
  * Leverage for EMR etc.
  * Authomated for DynamoDB, Auto Scaling Groups
* EC2 is behind EMR
  * Master Nodes
  * Compute Nodes (containt data)
  * Task Nodes (do not contain data)
