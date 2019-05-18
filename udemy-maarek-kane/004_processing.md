# Processing

### Lambda
* A way to run code snippets "in the cloud"
  * serverless
  * continuous scaling
* Often used to process data as it's moved around
* Some services don't talk directly to each other, so Lambda as a glue between them.
* Use cases:
  * Real-time file processing
  * Real-time stream processing
  * ETL (light-weight)
  * Cron replacement
  * Process AWS events
* Languages:
  * Node.js
  * Python
  * Java
  * C#
  * Go
  * Powershell
  * Ruby
* Lambda triggers:
  * S3, SES, Kinesis Streams/Firehose (Lambda polling data into a Stream, Kinesis is not pushing the data into Lamda), DynamoDB, SNS, SQS, AWS config, IoT, Lex, CloudWatch,
    CloudFormation, Gateway, Cognito, CodeCommit
* S3 --- triggers --> Lambda ----> Elasticsearch Service
* S3 --- triggers --> Lambda -- activates the pipeline --> Data Pipeline
* S3 --- triggers --> Lambda ----> Redshift (not efficient, better to batch them up and send them together)
  DynamoDB - streams ->      ----> Redshift (how to batch? We can use DynamoDb,
  it can keep track the progress checkpoints in DynamoDB, when some threshold is
  reached the data gets to be copies a batch to redshift)

#### Lambda + Kinesis
* Your Lambda code receives an event with a batch of stream records (lambda
  won't be invoked for every event)
  * You specify a batch size when setting up the trigger (up 10,000 records)
  * Too large a batch size can cause timeouts! (15m max time lambda can run)
  * Batches may also be split beyond Lambda's payload limit (6 MB)
* Lambda will retry the batch until it succeeds or the data expires
  * This can stall the shard if you don't handle errors properly
  * Use more shards to ensure processing isn't totally held up by errors
* Lambda processes shard data synchronously!!! As data is received from Kinesis
  that data is sent to Lambda and Kinesis shard sits there and waits for a response
  from Lambda. When Kinesis get stuck waiting for response from Lambda or get
  stuck because it's retriying Lambda function that keeps erroring out on it,
  that going to stall a shard.


#### Cost Model 
* Pay for what you use
* $0.20 / million requests
* $0.00001667 per GB / second

#### Other Promises
* High availability
* Unlimited scalability
  * 1000 concurrency lambda per region
* High performance
  * But you do specify a timeout! This can cause problems. Max is 900 seconds!

#### Anti-patterns
* Long-running applications (should use ec2 instead or chain multiple lambda
  functions together, split processing into steps to do heavy processing)
* Dynamic websites (ec2 and cloudfront)
* Stateful applications (but you can store state in DynamoDb or S3 that can
  share state between Lambda invocations)

* **Important:** The Kinesis stream should be in the same account as the Lambda. Lambda must be in the same account as the service triggering it, in addition to having an IAM policy granting it access.
* Although you think of a trigger as "pushing" events, Lambda actually polls your Kinesis streams for new activity.


#### AWS Glue (Table Defintions & ETL)
* It can provide structure to unstructured data
* Serverless discovery and defintion of table definitions and schema
  * S3 "data lakes"
  * RDS
  * Redshift
  * Most other SQL databases
* Custom ETL jobs
  * Under the hood it uses Apache Spark (you don't have to worry about it, it's
    serverless and managed)
  * Trigger-driven, on schedule, or on demand
  * Fully managed

#### Glue Crawler / Data Catalog
* Glue crawler is one component of Glue. 
  * It scans your data in S3 and often the Glue crawler will infer a schema
    automatically just based on the structure of the data it finds there in s3
    buckets. If you have some Csv or tsv data sitting in s3 it will
    automatically break-out those columns for you automatically and even name
    them for you.
  * You can schedule the cralwer periodically to run to. If you know you get new
    data just popping into s3 at random times. Glue can discover those
    automatically and run on the schedule discover and automatically pick up
    that data so other service downstream can see it and process it
  * The Glue crawler will populate the data catalog.
* Glue catalog:
  * Is a central meta data repository used by other tools that might alanalyze
    that data. 
  * The data itself remains where it was originally in S3, only the table
    definition itself is stored by Glue in the Glue data catalog. That means
    like the column names, the types of data in those columns, where that data
    is stored. That's what Glue catalog stores and vending to other services
    like Redshift, Athena or EMR. The data itselfs stays in s3, the data catalog
    just itself tells other services how to interper that data and how it's
    structured. Once it's catalogued, the data is immediately available for
    analysis in Spectrum, Athema, EMR. Once you have that in place you can
    visualize that data and run reports using Amazon QuickSight 
* Glue and S3 Partitions
  * Glue crawler will extract **partitions** based on how your S3 data is organized
  * How partitions are structured it can have impact on your partitions
  * Think up front about how you will be querying your data lake in S3
  * Example: devices send sensor data every hour
  * Do you query primarily by time ranges?
    * If so, organize your buckets as yyyy/mm/dd/device
  * Do you query primarely by device?
    * If so, organize your buckets as device/yyyy/mm/dd
  * If you know that you are going to query on one attribute. Make sure that
    your data get's structured that physically that information is in the same
    place, and you can do that by smartly choosing your directory structure in
    S3.

#### Glue + Hive
* Hive is a service that runs on ElasticMapReduce that allows you to issue
  SQL-like queries on data accessible to your EMR cluster. 
* Glue can integrate with Hive. You can use your AWS Glue Data Catalog as your
  meta (data) store for Hive. Also you can import a Hive meta store into Glue.

#### Glue ETL
* Automatic code generation
* It runs on Spark under the hood. Spark runs on Scala or Python.
* Scala or Python
* Encryption
  * Server-side (at rest)
  * SSL (in transit)
* Can be event-driven
* Can provision additional "DPU's" (data processing units) to increate
  performance of underlying Spark jobs
* Errors reported to CloudWatch

### Glue cost model
* Billed by the minute for crawler (extract information for the schema) and ETL (transforming that data on demand) jobs
* First 1M objects stored and acceses are free for the Glue Data Catalog
* Development endpoints for developing ETL code charged by the minute

#### Glue Anti-patterns
* You shouldn't use Glue for streaming data (Glue is batch oriented, minimum 5 minute intervals)
* If you need to ETL your data while you're streaming it in, it's better idea to
  perform your ETL using Kinesis store the data in S3 or Redshift and trigger
  Glue to continue transforming it.
* Multiple ETL enginges. Glue ETL is implemented in Spark. When you want to use
  other enginges such as Hive, Pig. So data pipeline or EMR might be a better
  choice for doing that ETL then glue ETL.
* Glue doesn't support NoSQL databases such as DynamoDB. And it wouldn't make
  sense anyway, because NoSQL databases don't require rigid schema. That's the
  whole point of Glue it provides schema for unstructured data for databased or
  analysis tools that require some sort of structure at data that they are
  looking at.

* Glue can integrate with most SQL databases, regardless of whether they are AWS services.
* You want to load data from a MySQL server installed in an EC2 t2.micro
  instance to be processed by AWS Glue. What applies the best here? A: Instance
  should be in your VPC.
* You can run your existing Scala or Python code on AWS Glue. Simply upload the code to Amazon S3 and create one or more jobs that use that code. You can reuse the same code across multiple jobs by pointing them to the same code location on Amazon S3.


### EMR (Elastic MapReduce)

#### What is EMR?
* Elastic MapReduce
* Managed Hadoop framework on EC2 instances
* In addtion of Hadoop it includes other tools that runs on top of Hadoop: Spark, HBase, Presto, Flink, Hive & more
* EMR Notebooks
  * Allows you interactively query data on your EMR cluster
  * Using python from a web browser
  * Sounds like a cloudera. It runs on ec2 and has built-in integration to other
    AWS services
* Several integration points with AWS

#### An EMR Cluster
* A cluser is a collection of ec2 instances
* Each ec2 instance is refered as a node
  * Each ec2 instance has a role, that is called a role type
* Master node: manages the cluser  (monitors health, does runs other services to
  keep the whole cluser runnning. Sometimes also called as a leader node)
  * Single EC2 instance
* Core node: Hosts HDFS data and runs tasks (have software components that run
  tasks and store data in the hadoop distributed file system - a file system
  that is spread out across your entire cluster)
  * Analyze the data on the cluster
  * Can be scaled up & down, but with some risk (you can loose some partial
    data, that's why we have task nodes available)
* Task node: Runs tasks, does not host data (they don't store the data, they
  just analyse that data, so there is no risk of data loss as e.g. with a core
  node)
  * You can add them as needed, without a risk
  * No risk of data loss when removing
  * Good use of **spot instances**. You can get cheap instance availability and
    use them on demand as needed to quickly scale up and down the computing
    capacity of the cluster as a whole.

#### EMR Usage
* Transient Cluser (can be automatically terminated - perform a taks and
  terminate) vs. Long-Running Clusers (termination is deactivated by default)
  * Can spin up task nodes using Spot instances for temporary capacity
  * can use reserved instances on long-running clusters to save $
* Connect directly to master to run jobs
* Submit ordered steps via the console
