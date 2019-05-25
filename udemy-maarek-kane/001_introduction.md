# Introduction

* Very challenging certification.
* Topics:
  * Collection: Kinesis, IoT Core, Snowball, SQS, DMS, Direct Connect
  * Storage: S3 + Glacier, DynamoDb, ElastiCache
  * Processing: Lambda, ML, Glue, SageMaker, EMR, Data Pipeline
  * Analysis: ElasticSearch, Athena, Redshift
  * Visualization: QuickSight
  * Data Security: KMS, CloudHSM


# Case Study
* Cadabra.com a huge e-commerce company
* Requirement 1: Order history app
  * Server logs -> Amazon Kinesis Data Streams -> AWS Lambda -> Amazon DynamoDB -> Client App

![case](./img/case-1.png)

* Requirement 2: Product recommmendations (training a machine learning algorithm)
  * Sever logs -> Amazon Kinesis Data Firehouse -> S3 -> Amazon EMR

![case](./img/case-2.png)

* Requirement 3: Predicting order quantities that user might order for a specific item (automatically suggest to order more than 1 specific thing)
  * Server logs -> Amazon Kinesis Data Firehouse -> S3 -> Amazon Machine Learning

![case](./img/case-3.png)

* Requirement 4:  Transaction rate alarm (when an unexpected rate of orders come out of a sudden) - must work in realtime
  * Server logs -> Amazon Kinsis Data Streams -> Amazon Kinesis Data Analytics -> Amazon Kinesis Data Streams -> AWS Lambda -> Amazon SNS

![case](./img/case-4.png)

* Requirement 5: Near-rel-time log analysis (analyze server data in realtime for operational purposes
  * Server logs -> Amazon Kinesis Data Firehouse -> Amazon Elasticsearch Service

![case](./img/case-5.png)

* Requirement 6: Data warehousing & visualization
  * Server logs -> Amazon Kinesis Data Firehouse -> Amazon S3 
      1. Solution -> AWS Glue -> Amazon Athena (SERVERLESS)
      2. Solution -> Amazon Redshift -> Amazon QuickSight (MANAGED)

![case](./img/case-6.png)

