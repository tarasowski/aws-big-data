# Question that I didn't know


* Binary classification whether the customer will subscribe to new product or
not ML models for binary classification predict a binary outcome. To train
binary classification models, AWS uses logistic regression. It uses Are Under
the (Receiver Operating Characteristic) Curve (AUS) to predict the accuracy

* ML modles for multiclass classification problems allow you to geneate
predictions for multiple classes. In Amazon ML, the macor-average F1 score is
sused to evaluate the predictive accuracy of a multiclass metric

* ML models for regression problems predict a numeric value. ML uses root square
error (RMSE) metric

* Redshift: split your load data files so that the files are about equal size, between 1MB
and 1GB after compression. For optimum parallelism, the ideal size is between
1MB and 125MB after compression

* Redshift: Manifest files address eventual consistency issues during loads. S3
provides eventual consistency for some operations. It's possible that new data
won't be available immediately after the upload. You can manage data consistency
by using a manifest file to load data

* You can create chatbots with Amazon Lex service


* Using DynamoDB auto scaling is the recommended way to manage throughput
capacity settings for replica tables that use the provisioned mode. Auto scaling
automatically adsjusts read capacity units (RCUs) and write capacity units
(WCUs) for each replica table based upon your actual application workload


* How TTL works in DynamoDB:
  * A background job checks the TTL attribute of items to see if they are
expired
  * If the epoch time value stored in the attribute is less than the current
time, the item is marked as expired and subsequently delted


* If the list and the set of object processed is incomplete on EMR:
  * Enable consistent view. This allows EMR clusters to check for list and
read-after-write consistency
  * EMR uses DynamoDB database to store object metadata and track consistency
with EMRFS Storage


* Which commands can you use to understand the metadata of the Redshift
architecture?
  * STL table are generated from logs that have been persisted to disk to
provide a history of the system. These files reside on every node in the data
warehouse cluster. The STL tables take the information from the logs and format
them intu usable tables for system
  * STV tables are virtual tables that contain snapshots of the current system
data
  * System tables and views do not use the same consistency model as regular
tables
  * System views that contain any reference to a transient STV table are called
SVV views and references to STL tables are called SVL views


* Key steps in provisioning of devices IoT
  * Enable a device with an existing certificate or have AWS IoT create and
register one for you
  * Define device shadow service to get and set the state of a device over MQTT
or HTTP
  * Assign a policy attached to the certificate and define unique identifier for
the thing (device)
  * Define set of attributes for the thing, including existing thing types and
groups


* HH using kinseis agent to process events and uses consumer libraray to collect
and disseminate streams. What kind of monitoring is enabled by kinesis agent?
  * The agent publishes custom CloudWatch metrics with a namespace of
AWSKinesisAgent
  * The agent publishes Bytes sent, number of records attempted, number of
records that returned failure and the number of calls to PutRecords that
resulted in a service error


* Data Pipeline DataNode: In AWS Data Pipeline, a data node defines the location and type
of data that a pipeline activity uses as input or output. AWS Data Pipeline
supports the following types of data nodes:
  * DynamoDBDataNode: A DynamoDB table that contains data for HiveActivity or
EmrActivity to use
  * SqlDataNode: An SQL table and database query that represent data for a
pipeline activity to use
  * RedshiftDataNode: Redshift table that contains data for RedshiftCopyActivity
to use
  * S3DataNode: S3 location that contains one or more files for a pipeline
activity to use

* Data Pipeline Activity: an activity is a pipeline component that defines the work to
perform. Data Pipeline provides several pre-packaged activities that accomodate
common scenarios, such as moving data from one location to another, running Hive
queries, and so on. 
  * CopyActivity: copies data from one location to another
  * EmrActivity: runs an EMR cluster
  * HiveActivity: runs a Hive query on EMR
  * HiveCopyActivity: runs a Hive query on EMR with support for advanced data
filtering and support for S3DataNode 
  * PigActivity: runs a Pig script on EMR
  * RedshiftCopyActivity: copies data to and from Redshift tables
  * ShellCommandActivity: runs a custom unix/linux shell command as an ectivity
  * SqlActivity: runs a SQL query on a database
 
* Data Pipeline Databases: supports the following types of databases:
  * JdbcDatabase
  * RdsDatabase
  * RedshiftDatabase

* Data Pipeline Taskrunners:  A task runner is an application that polls AWS Data Pipeline for tasks and
then performs those tasks. Can be used and installed on-premise components

* Data Pipeline Actions: are steps that a pipeline component takes when certain
events occur, such as success, failure, or late activities. 

* Data Pipeline Resource: a resource is the computattional resource that
performs the work that a pipeline activity specifies. AWS Data Pipeline supports
the following types of resources:
  * Ec2Resource: An EC2 instance that performs the work defined by a pipeline
activity
  * EmrCluster: EMR cluster that performs the work defined by a pipeline
activity such as EmrActivity


* AWS Migration Hub provides a single location to track the progress of
application migrations across multiple AWS and partner solutions. Using
Migration Hub allows you to choose the AWS tools that best fit your needs, while
providing visibility into the status of migrations across your portfolio of
applications


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


* Amazon ML uses the following learning algorithms:
  * For binary classification, ML uses logistic regression
  * For multiclass classification, ML uses multinominal logistic regression
  * For regression, ML uses linear regression

* Cross-validation is a technique for evaluating ML models by training several
ML models on subsets of the available input data to detect overfitting which
eventually fails to generalize the pattern

* ML uses Area Under the (Receiver Operating Characteristic) Curve (AUC) to
provide accuracy of the model


* Binary Classification Model:
  * ML models for binary classification problems predict a binary outcome. To
train binary classification model ML uses logistic regression
  * Is this email spam or not?
  * Will the customer buy this product?
  * I sthis product a book or a farm animal?
  * I sthis review written by a customer or a robot?

* Multiclass Classification Model
  * ML modles for multiclass classification problems allow you to generate
predictions for multiple classes (predict one of more than two outcomes), ML
uses the multinominal logistic regression
  * Is this product a book, movie or clothing?
  * Is this movie a romantic comedy, documentary or thriller?
  * Which category of products is most interesting for this customer?

* Regression Model
  * ML modles for regression problems predict a numeric value, ML uses linear
regression
  * What will the temperature be in Seattle tomorrow?
  * For this product, how many units will sell?
  * What price will this house sell for?


* Kinesis Analytics Windows:
  * For clickstream data use stagger windows
  * Stagger = Staffel
  * Tumbling = taumeln
  * Sliding = schieben

* In ML Visualizaiton explore the accuracy of your model beyond the prediction
accuracy metric

* Amazon ML uses macro-average F1 score to provide accuracy of the model
  * F1 score is used to evaluate the predictive accuracy of a multiclass metric


* Streaming
  * Metrics configured for streams are automatically collected and pushed to
CloudWatch every minute
  * Metrics are archived for two weeks; after that period, the data is discarded
  * Basic stream level data is captured every minute at no additional charge
  * Shard-level data is sent every minute for an additional cost
  * Enhanced shard-level metrics are being sent to cloudwatch every minute.
These metrics are not enabled by default. There is a charge for enhanced metrics
emitted from Kinesis

* Pipeline:
  * When AWS Data Pipeline runs a pipeline; it compiles the pipeline components
to create a set of actionable instances
  * Pipeline components represent the business logic of the pipeline and are
represented by the different sections of a pipeline definition
  * AWS Data Pipeline retries a failed operation. It continues to do so until
the task reaches the max. number of allowed retry attempts.
  * AWS Data Pipeline hands the instances out to task runners to process


* AWS IoT Components:
  * Device gateway: enables devices to securely and efficiently communicate with
AWS IoT
  * Message broker: Provides a secure mechanism for devices and AWS IoT
applications to publish and receive messages from each other.
  * Rules engine: Provides message processing and integration with other AWS
services
  * Security and Identity service: Provides shared responsitbility for security
in the AWS Cloud. Your devices must keep their credentials safe in order to
securely send data to the message broker
  * Registry: organizes the resources associated with each device in the AWS
Cloud. You register your device and associate up to three custom attributes with
each one.
  * Group registry: alloes you to manage several devices at one by categorizing
them into groups
  * Device shadow: a json document used to store and retrieve current state
information for a device
  * Device shadow service: provides persistent representations of your devices
in the AWS Cloud. You can publish updated state information to a device's ahdow,
and your device can sync its state when it connects. Your devices can also
publish their current state to a shadows for use by applications or other
devices
  * Device provisioning service: allws you to provision devices using a template
that describes the resources required for your device: a thing, a certificate,
and one or more policies
  * Custom auth service: you can define custom athorizers that allow you to
manage your own authentication and authorization strategy using a custom
authentication service and a lambda function
  * Jobs service: allows you to define a set of remote operations that are sent
to and executed on one or more devices connected to AWS IoT


* Kinesis Analytics
  * VPC flow Logs have a capture window of approx. 10 minutes. But they can have
a capture window of up to 15 minutes if you're aggregating data on the client. A
stagger windows query. A query that aggregates data using keyed time-based
windows that open as data arrives. The keys allow for multiple overlapping
windows. This is the recommended way to aggregate data using time-based windows

  * A continuous filter is a common query that uses a where clause to select a
portion of your data stream. For this specific query we will apply a filter on
the "status" column to only select and records with equal "fail" and insert them
into a subsequent stream. This common query is useful for alerting on events
that match a particular query. Commonly, they are then forwarded on to other
Kinesis streams, SNS topics or Lambda function
(https://s3-us-west-2.amazonaws.com/kinesis-helpers/workshops/20170405-streaming-data/SF+loft+Kinesis+workshop.pdf)

  * A tumbling window is similar to a periodic report, where you specify your
query and a time range, and results are emitted a the end of a range ex: COUNT
number of items by key for 10 seconds

  * There are 3 different types of windows

![windows](./img/baa-12-09-screenshot.png)

* Tumbling:
  * Fixed size and non-overlapping
  * Use FLOOR() or STEP() function in a GROUP BY statement
* Sliding:
  * Fixed size and overlapping; row boundaries are determined when new rows
enter window
  * Use standard OVER and WINDOW claus (ex count(col) OVER(RANGE INTERVAL '5' MIN)

* Tumbling windows are useful for periodic reports. You can use a tumbling window to compute an average number of visitors to your website in the last 5 minutes or the maximum over past hour. A single result is emitted for each key in the group as spcivied by the caluse the end of the defined window. An important characteristic of a tumbling window is that the bounds do not overlap; the start of a new tumbling window begins the wht end of the old window. 

![tumbling](./img/e58-12-14-screenshot.png)

* All of our previous window queries were using ROWTIME, which is the procesisng
                                        time of the application. The processing
                                        time is useful in many real-time use
                                        cases like the previous exercise
                                        (sliding window and filter). However
                                        there are many cases where you need to
                                        use your data's event time. An event
                                        time is a stimestamp generated by a data
                                        producer when the event was created. A
                                        key problem with using event time is
                                        that events arrive out of order. You
                                        could perform sorts on the data but
                                        sorts will leave events out which you
                                        need to reconcile later. An alternative
                                        approach to use both processing and
                                        event time in your windows

 
* Kinesis Firehose:
  * Firehose provides the following Lambda blueprints that you can use to create
                                        a lambda function for data
                                        transformation
  * General Firehose Processing: contains the data transformation and status
                                        model described in the previous section.
                                        Use this blueprint for any custome
                                        transfromation logic
  * Apache Log to JSON
  * Apache Log to CSV
  * Syslog to JSON: syslog is a standard for sending and receiving notification
                                        messages-in a particular format-from
                                        various network devices
  * Syslog to CSV
  * Firehosess Process Record Streams as source: accesses the kinesis data
                                        streams records int he input and returns
                                        them with a processing
  * Firehose CloudWatch Logs Processor: parses and extracts incividual log
                                        events from records sent by CloudWatch
                                        logs subscription filter 


* Redshift / Storage
* when the administrator is not availabe nad we are not sure of the workload, it
                                        is always better to go with no
                                        distribtuion style because Redshift
                                        handles the distribution mechanism

* DynamoDB applies adaptive capacity in real time in response to changing
application traffic patterns, which help you maintain uninterrupted prefromance
indefinitely, even for imbalanced workloads. In addition, instan adaptive
capacity helps you provision read and write throughput efficiently instead of
overprovisioning to accomodate uneven data access patterns. Instant adaptive
capacity is on by default at no additional cost ofr all DynamoDB tables

* Amazon ElasticSearch doesn't support COPY command to load data into Redshift.
The COPY command loads data in parallel from S3, EMR, DynamoDB or multple data
sources on remote hosts. COPY loads large amount of data much more efficiently
than using INSERT statements, and stores the data more effectively as well.
Integration of COPY command with Elasticsearch is not supported

* What types of table/views can help access the performance related infor for
diagnosis?
  * STL system table are generated from Redshift log files to provide a history
of the system. They server Logging
  * STV tables are actually virtual system tables that contain snapshots of the
current system data. They server snapshots
  * The system catalog store schema metadata, such as information about tables
and columns


* Visualisation:
  * Combo chart: on the clustered bar combo chart, bars display for each child
dimension, grouped by the parent dimension. On the stacked bar combo chart, one
bar displays per parent dimension

![combo
  chart](http://www.k12science.org/curriculum/weatherproj2/images/graph_combo.gif)
  * The team identified a dataset that they want to delete, on which some
analysis is already generated. They submitted the deletion. What happens next?
  * You receive a warning if you have any analysises that use the data set you
have chosen for deletion
  * Dataset deletion does not delete the dependet analysis
  * Next time you open any of those analyses, you are prompted to select a new
data set for any visuals that wer based on the delelted dataset

* EMR Notebooks is a Jupyter Notebook environemtn built in to the EMR console
that allows you to quickly create Jupyter notebooks, attach them to Spark
cluster, and then open the Jupyter Notebook in the console to remotely run
queries. EMR notebook is saved in S§ independently from clusters for durable
storage, quick access, and flexibility. You can have multiple notebooks open,
attach multiple notebooks to a single cluster and re-use a notebook on different
clusters
* Jupyter Notebook is an open-source web application that you can use to create
and share documents that contain live code, equations, visualizations, and
narrative text. JupyterHub allows you to host multiple instances of a
single-user Jupyter notebook server. When you create a cluster with JupyterHub,
EMR creates a Docker container on the cluster's master node. JupyterHub, alls
the components required for Jupyter and Sparkmagic run within the container


* IoT
  * Device shadow is a json document used to store and retreive current state
information for a device
  * Device shadow service provides persistent representations of your devices in
the AWS Cloud

* Security
  * Read the question: "TI launched EMR 3.2.1 using EMRFS storage to support
their real-time data analytics"... S3 server-side encryption with KM is not
available when using EMR version 4.4 or earlier
  * You can use AWS KMS customer master key (CMK) set up with policies suitable
for EMR
  * With S3 client-side encryption, the Amazon S3 encryption and decryptin takes
place in the EMRFS client on your cluster. Objects are encrypted before being
uploaded to S3 and decrypted after tehy are downloaded. The provider you specify
supplies the encryption key that the client uses. The client can use keys
provided by AWS KMS (CSE-KMS) or a custom Java sclass that provides the
client-side master key CSE-C. The encrytpin specifiecs are slightly differnt
between CSE-KMS and CSE-C.
  * You cannot audit of encryption and decryption of AWS owned CMK using AWS
CloudTrail
  * Redshift database security:
    * Groups are collections of users that can be collectively assigned
privileges for easier security maintenance
    * By default privileges are granted only to the object owner
    * Redshift database users are named user accounts that can connect to a
database. A user account is granted privileges explicitly, by having those
privileges assigned directly to the account or implicitly by being a member of a
group that is granted privileges
    * Schemas are collections of database tables and other database objects.
Schemas are similar to operatinng sytem directoreis, except that schemas cannot
be nested
  * Amazon ElasticSearch: When encryption of data is enabled, what all aspects
of domain are encrypted?
    * Automated snapshots
    * Elasticsearch logs
    * Swap files


* Athena: To run question in Athena, you ust have the appropriate permissions
for:
  * The Athena actions
  * The S3 locations where the underlying data is stored that you are goingt to
query in Athena
  * The resources that you store in AWS Glue Data Catalog, such as databases and
tables, that you are going to query in Athena
  * The encrypted metadata in the AWS Glue Data Catalog. If you migrated to
using that metadata in Athena and the metadata is encrypted


* Apache Phoenix is used for OLTP and poerational analytics, allowing you to use
standard SQL queries and JDBC APIs to work with an Apache HBase backing store


* What kind of windows queries need to be used to aggregate data using keyed
time-based windows that open as data arrives:
  * Stagger Windows Queries


* ML data sources can be created only for RDS, Redshift and S3
* ML provides 3 options to split datasets:
  * Pre-split data
  * Sequential split
  * Random split
* ML AttributeType includes Binary, Categorical, Numeric and Text datatypes

* End-to-End data encryption for all the data that is being accessed through
Athena for both data in S3 and also encrypted results
  * Server-side encryption (S3) with an S3-managed Key (SSE-S3) for encrypted
datasets in S3 and for encrypted query
  * Server-side encryption (SS3) with AWS KMS customer managed key (SSE-KMS)
  * Client-side encryption (CSE) with a AWS KMS customer managed key (CSE-KMS)


* Data Protection in Amazon Kinesis Data Firehose
  * You can enable server-side data encryption when you use Firehose. How you do
this depends on the source of your data
    * Server-side encryption with Kinesis Data Streams as the Data Sources: whn
you configure a kinesis data stream as the data source of Firehose delivery
stream, Kinesis Data Firehose no longer stores the data at rest. Instad, the
data is stored in the data stream
    * Server-side encryption with direct put and other data sources: If you send
data to your delivery stream using PutRecord or PutRecordBatch, or if you send
your data using IoT, you can turn on server-side encryption by using the
StartDeliveryStreamEncryption operation


* Kinesis Stream provide capabilite to use Future objects to validate
UserRecords. No need to complicate the code by storing in memory/transient
storage

* Redshift query optimizer uses sort order when it determines optimal query
plans. Choose the optimal sort key to address querying of most recent data,
frequent range filtering or equality filtering and joining of multiple tables


* Amazon DynamoDb: distribute your upload work by using the sort key to load one
item from each partition key value, then another item from each partition key
value and so on???


* Jupyter Notebook is an open-source web application that you can use to create
and share documents that contain live code, equations, visualization and
narrative text. Amazon EMR offers you two options to work with Jupyter
notebooks:
  * EMR notebook
  * JupyterHub
    

