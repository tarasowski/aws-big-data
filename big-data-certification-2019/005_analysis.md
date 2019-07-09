# Analysis

### Kinesis Analytics
* Querying streams of data (similar to spark streaming)
* Kinesis data analytics can receive data from Amazon Kinesis Data Streams or
  Firehose
* Just like in Spark Streaming Analytics you can set windows you can look back
  and aggregate the data, and analyse data across.
* Always receiving never ending data and you can write SQL to analyze data and
  turn around and split out the results to another stream or analytics tools of
  your choice.
* There are 3 main parts of Kinesis Analytics:
  * Source / Input data: this is the data to be streamed is coming from. The
    data come cam from Data Streams / Firehose. You can also optionally
    configure a reference data source to enrich your data stream within the
    application, that is resulted in a reference table. Some sort of a lookup
    data that you want to refer to within your SQL in your analytics job. In
    order to use it, you need to store your reference data as an object in S3.
    When Kinesis Analytics starts it will read the S3 object and create an
    in-application table, so you can refer to that data you wish.
  * Realtime Analytics: here sits the application code. Where the actual
    analysis happens and it's going to perform realtime analytics just using SQL
    queries on your stream of information. The stuff that forms the application
    code is just an SQL code, these are SQL statements which will be processed
    on the streaming data and reference table. It can operate on windows on
    time, so you can look back to fix time period as new data has been received.
      * There can be multiple applications e.g. multiple in-app streams that can
        differently process data and send this data to different destinations.
        One in-application stream can process data every 10seconds and the other
        in-application can pick up this data an do something with it every 1
        minute.
  * Destinations: Where the processed data will go. Once the data is processed
    it can be sent to Kinesis stream back again or to another Firehose stream.
    From there is can go where you want. Lambda can be involved too. If errors
    are encountered, those are sent to the Error stream. Kinesis Analytics will
    provide an Error stream for every application. If the application has
    problems to process any records that error will be written into Error
    Stream.

#### Kinesis Analytics Use Cases
* Streamin ETL
  * You can built an application that continiously reads data stored in a
    Kinesis Stream, organize that data by the sensor type, remove that data,
    normalize the data per specified schema and deliver that data to Amazon S3.
* Continuous metric generation
  * You can build a live leader board for a mobile game. By generating it every
    minute and send it to Amazon DynamoDB. You can check the traffic of your
    website by calculating the number of unique visitors every 5 minuts or so
    and sending the processs results to Amazon Redshift for further analysis.
* Responsive analytics
  * In application computing the availability or success metric of a customer
    facing API overtime and send those results to Amazon CloudWatch. 
  * You can use Kinesis Analytics ---> Kinesis Streams ---> SES to notify a
    customer.

#### Kinesis Analytics
* Pay only for resources consumed (but it's not cheap)
* Serverless; scales automatically
* Use IAM permissions to access streaming source and destination(s)
* Schema discovery
  * How the column names are in your SQL found
  * Can analyze the incoming stream and infer the schema

![kinesis
analytics](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/images/kinesis-app.png)

#### RANDOM_CUT_FOREST
* Detects anamalies and outliers in a streaming data
* SQL function used for anomaly detection on numeric columns in a stream
* They're especially proud of this because they published a paper on it
* It's a novel way to identify outliers in a data set so you can handle them
  however you need to
* Example: detect anomalous subway ridership during the NYC marathon

* While you might in turn connect S3, Redshift, or Lambda to your Kinesis Analytics output stream, Kinesis Analytics must have a stream as its input, and a stream as its output.
* If a record arrives late to your application during stream processing, what happens to it? The record is written to the error stream
* You have heard from your AWS consultant that Amazon Kinesis Data Analytics elastically scales the application to accommodate the data throughput. What though is default capacity of the processing application in terms of memory? Kinesis Data Analytics provisions capacity in the form of Kinesis Processing Units (KPU). A single KPU provides you with the memory (4 GB) and corresponding computing and networking. The default limit for KPUs for your application is eight.
* You have configured data analytics and have been streaming the source data to the application. You have also configured the destination correctly. However, even after waiting for a while, you are not seeing any data come up in the destination. What might be a possible cause? Issue iwth IAM role, Mismatched name for the output stream, Destination service is currently unavailable
![transaction alaram](./img/transaction-alarm.png)

### Amazon Elasticsearch Service
* Petabyte-scale analytics and reporting
* Elasticsearch started as a search engine but it's not a search engine anymore.
  It's more for analysis and reporting.
* For some applications it can analyse massive data sets much faster than Apache
  Spark can do it. For the right source of queries ES can be a good choice for
  getting answers back really quickly across massive data sets across an entire
  cluster

#### What is Elasticsearch?
* The elastic stack (Elasticsearch is just a component of the stack):
* Elasticsearch is distributed version of Lucene. They took the open source
  version of Apache Lucene and made it distributed so it can work across many
  machines. It's has expanded over the year to include more tools
* A search engine
* An analysis tool
* A visualization tool (Kibana)
  * You can store a semi-structured data
* A data pipeline (Beats / is package of Beats LogStash)
  * Feed data at scale to Elasticsearch
  * Import from other sources data into Elasticsearch cluster
  * You can use Kinesis too
* Horizontally scalable
  * Lucene scaled out indifinetely
* Kibana + ElasticSearch is a good alternative to Google Analytics

#### Elasticsearch applications
* Analysing logs is the market of Elasticsearch or a niche that they cover
* Full-text search
* Log analytics
* Application monitoring
  * Based on incoming log data to visualize what happens in realtime
  * Adobe uses ES can easily see traffic patterns and error rates for developers
* Security analytics
* Clickstream analytics
  * [Hearst cooperation use case how to build clickstream engine](https://www.youtube.com/watch?v=6cwbbqi36k8)
  * [slides](https://www.slideshare.net/AmazonWebServices/bdt306-how-hearst-publishing-manages-clickstream-analytics-with-aws)

#### ElasticSearch Main Concepts
* Documents: Documents are the things you#re searching for. They can be more
  than text - any structured JSON data works. Every document has a unique ID,
  and a type.
* Types: A type defines the schema and mapping shared by documents that
  represent the same sort of thing. (a log entry, an encyclopedia article etc.)
  (deprected). Thing about documents and indicies, but in an exam it could be
  asked.
* Indices: An index powers search into all documents within a collection of
  types. They contain inverted indicies that let you search across everything
  within them at once.
    * An index is split into shards
    * Documents are hashed to a particular shard
    * Each shard may be on a different node in a cluser
    * Every shard is a self-contained Luecene index of its own (every shard is
      it's own little mini search engine)

#### Redundancy
* This index has to primary shards and two replicas.
* Your application should round-robin request among nodes.
  * So you don't need to put that load just only on the primary shard 
  * You can use those replica nodes to expand your read throughput as well
* Write request are routed to the primary shard, then replicated to how many
  replicas you specify
* Read request are routed to the primary or any replica

![shards](./img/es-shards.png)

![shards](https://cdn-images-1.medium.com/max/1600/1*u6kVsD_Yl3DY43IJAixDqw.png)

#### Amazon Elasticsearch Service
* Fully-managed (but not serverless)
  * You need to think about how many servers do you need (nodes)
* Scale up or down without downtime
  * But this isn't automatic
* Pay for what you use
  * Intance-hours, storage, data transfer
* Network isolation
  * With Amazon VPC
  * Encrypt your data at rest and in transit
* AWS integration
  * S3 buckets (via Lambda to Kinesis)
    * Use Lambda as Glue between S3 and pipe the data to Kinesis
  * Kinesis Data Streams
  * DynamoDB Streams
  * CloudWatch / CloudTrail
  * Integrates with IoT services of AWS
  * Zone awareness
    * You can allocate ES nodes across two different availability zones in the
      same region, by doing that you can increase your availability of each
      service but it can increase latency

#### Amazon ES options
* How many dedicated master node(s)
  * How many of them and what instance type 
* Domains
  * AWS service domain is a collection of all the resources needed to run an ES
    cluster. It contains all the configuration for the cluster as a whole. So
    basically a cluster in Amazon ES is a domain
* Snapshots to S3
  * For data backup processes. If you accidentally shutdown your cluster you
    will keep the data
* Zone Awareness
  * Increased availability on the price of higher latency

#### Amazon ES Security
* Resource-based policies
  * You can attach those to the service domain. That determines what actions
    principals can take on Elastic Search API's. Where principals are users, an
    account or a role that can be granted access.
* Identity-based policies
  * Using AIM policies
* IP-based policies
  * To tight specific actions to specific IP ranges
* Request signing
  * Sign your request. When you send a request from AWS SDK's to ES. You need
    digitally sign all the request are going in. So they're basically secure the
    traffic in flight. 
* VPC
  * You can put a cluster into a VPC instead of making it public. VPC is not
    accessible from the outside world. But it makes it hard to connect to your
    cluster and use tools like Kibana
  * You have to decide upfront if your cluster is going to live in the VPC or be
    publically accessible. You can't change that later.
* Cognito
  * It integrates with Cognito and primarily it used in the context with Kibana.

#### Securing Kibana
* If you host your cluster inside a VPC, how to you access Kibana. You have to
  access Kibana through a web interface.
* Cognito - The simplest way to do it using Cognito. It allows users to log into
  Kibana though an enterprise identity provider such as microsoft active
  directory using Saml 2.0 or Google, Amazon, Facebook. Cognito allows you to
  access the cluster via Kibana even if it's inside a VPC. 
* Getting inside a VPC from outside is hard...
  * Some ways around it
    * Nginx reverse procy on EC2 forwarding to ES domain
    * SSH tunnel for port 5601 (which is what Kibana listens on)
    * VPC Direct connect
    * VPN

#### Amazon ES anti-patterns
* OLTP
  * No transactions
  * RDS or DynamoDB is better
* Ad-hoc data querying
  * Athena is better
* Remember Amazon ES is primarily for search and analytics

#### Notes on AWS ES
* Database is called domain in Elasticsearch
* Node-to-node encryption: This setting provides an additional layer of security. Each Amazon ES domain operates within a secure, dedicated VPC. Node-to-node encryption enables TLS encryption for all communications within that VPC. (In flight)
* Data at rest encryption: Encryption at rest secures the indices and automated snapshots associated with the domain.
* Index rotation: Select how often to rotate the Elasticsearch index. Firehose appends a corresponding timestamp to the index and rotates it.

* As recommended by AWS, you are going to ensure you have dedicated master nodes
  for high performance. As a user, what can you configure for the master nodes?
    The count and instance types of the master nodes
* Which are supported ways to import data into your Amazon ES domain? Kinesis, DynamoDB, Logstash / Beats, and Elasticsearch's native API's offer means to import data into Amazon ES.


#### MyArchitecture:
* [How Appnext does big data
  analytics](https://www.youtube.com/watch?v=wEOm6aiN4ww)
* Kinesis Firehose ---> JSON S3 ---> EMR ---> Parquet ---> Athena / Spectrum
* [ ] Analyse other Architectures: https://www.youtube.com/watch?v=mxKhbU_ToMs&list=PLhr1KZpdzukdeX8mQ2qO73bg6UKQHYsHb


#### Amazon Athena
* SQL interface for S3
* Serverless interactive queries of S3 data
* Interactive query service for S3 (SQL)
  * No need to load data, it stays in S3
* Presto under the hood
  * Highly customized and preconfigured ec2 instance for you
* Serverless
* Supports many data formats (depending on the application, you need to choose
  the right format -
  [Benchmarks](https://www.slideshare.net/oom65/file-format-benchmarks-avro-json-orc-parquet))
  * CSV (human readable) - comma separated also TSV tab separated list
  * JSON (human readable) - bit more structure and hiarchy
  * If you do want to do things at scale, you need something which is more
      efficient. You should looking for non-human readable. Instead of
      organizing data by rows, it's organizing it by each column. So if you have
      an application that does query your data based on specific columns. They
      are also spittable, the files can be split and distributed across the
      entire cluster. 
      * ORC (columnar, splittable)
      * Parquet (columnar, splittable)
      * Avro (spittable, no columnar, not-human readable) - more for a row based storage
* Unstructured, semi-sctructured, or structured
  * Doesn't really care how the data is structured in S3 it can work with a Glue
    & Glue Data Catalog and impart structure on that data. 

![Columnar](https://mariadb.com/files/inline-images/columnstore-row-vs-column-orientated_0.png)

#### Some examples
* Ad-hoc queries of web logs
* Querying staging data before loading to Redshift
* Analyze CloudTraiil / CloudFront / VPC / ELB etc. logs in S3
* Integration with Jupyter, Zeppelin, RStudie notebooks
* Integration with QuickSight
* Integration via ODBC / JDBC with other visualization tools
  * An ODBC driver uses the Open Database Connectivity (ODBC) interface by Microsoft that allows applications to access data in database management systems (DBMS) using SQL as a standard for accessing the data. ... ODBC permits maximum interoperability, which means a single application can access different DBMS.


#### Athena + Glue
* Amazon S3 ----> AWS Glue ---> Amazon Athena ---> Amazon QuickSight
* Glue imparts structure on unstructured data in S3 that Athena can query it as
  a database. 
  * Glue crawler populating the Glue Data Catalog for your S3 data. That's
    looking at what's stored in S3 and trying to extract columns and table
    definitioins out for you. 
  * Once you have Glue Data Catalog with your published data. Athena will see it
    automatically and can build a table from there automatically. Anytime Athena
    sees something in you Data Catalog in your account. It's going to make a
    table for you, so you can query just you would any other SQL database. 
  * Data catalog allows other analytics tools to visualize and anlyse that data
    as well. E.g. RDS, Redshift, Redshift Spectrum, EMR, any application
    compatibable with Apache Metastore. Glue catalog can be used as a Hive
    metastore too.
* Athena integrated with Glue's Data Catalog that allows you to create unified
  metadata repository across various services, crawl data to discover schemas,
  populate your catalog with a new and modified table partition definitions and
  maintain schema versioning all under the hood and Athena just sits on top of
  that and provides SQL interface to that underlying Glue structure.

#### Athena cost model
* Pay-as-you-go
  * $5 per TB scanned
  * Successful or cancelled queries (charged for), failed queries (are
    free).
  * No charge for DDL (Create, Alter, Drop etc)
* Save LOTS of money by unsing columnar formats
  * Better performance for applications that querying a small number of columns
    use:
    * ORC, Parquet
    * Save 30-90% and get better performance
    * It allows Athena only to select the required column and process your data.
      You are reducing the amount of data that you need to scan with Athena. By
      reducing that scanning you win.
    * Partition your data can reduce your costs as well. If you have your data
      partitioned such as by date, hour etc. queries that are restricted to that
      given partition will also scan less data as well. 
* Glue and S3 have thir own charges. Athena justs sits on top of Glue, just to
  get the table definition of your data and the data is stored in S3.

#### Athen Security
* Access control
  * IAM, ACLs, S3 bucket policies
  * AmazonAthenaFullAccess / AWSQuicksightAthenaAccess
* Encrypt results at rest in S3 staging directory
  * Server-side encryption with S3-managed key (SSE-S3)
  * Server-side encryption with KMS key (SSE-KMS)
  * Client-side encryption with KMS key (CSE-KMS)
* Cross-account access in S3 bucket policy possible
  * It's possible for Athena to access a data lake from another acccount
* Transport Layer Security (TLS) encrypts in-transit (between Athena and S3)

#### Athena anti-patterns
* Highly formatted reports / visualization
  * That's what QuickSight is for
  * Nice stuff with graphs and visualization
* ETL
  * Use Glue instead
  * Or with Apache Spark

#### Athena Example
* Glue can be run on demand or frequently: daily, hourly, monthly etc.
* Glue sees partitions. Our data was broken up into year subdirectory, month
  subdirectory, a day subdirectory, and hour subdirectory. These is what the
  partitions are in the crawler view (the prefixes of the files). It's a
  subdirectory structure that our S3 data lives with in. We can take advantage
  of those partitions to speed up our queries.
* If you want to transform a data type recognized by Glue into something else
  e.g. InvoiceDate from String to Date. The best way to do that is to write an
  ETL jobs to do this conversion for you.
* A table in Glue give some structure to a collection of CSV files that are
  sitting in S3. We can start treat the S3 datalake as a database.

![glue table](./img/glue-table.png)

![Athena](./img/athena.png)

### Redshift 
* Fully-managed, petabyte-scale distributed data warehouse. Spread across an
  entire cluster.

#### What is Redshift
* Fully-managed, petabyte scale data warehouse service
* 10x better performance than other DW's
  * Via machine larning, massivley parallel query execution, columnar storage
* Designed for OLAP, not OLTP
  * OLAP - online analytical processing
  * OLTP - more row based storage (massive transaction rates to expect fast
    responses)
* Cost effective
  * Super cheap, the most effective data warehouse. No upfront costs.
* SQL, ODBC, JDBC interfaces
  * SQL based clients or BI tools (ODBS, JDBC)
  * Connect analytical / visualization tool
* Scale up or down on demand
* Built-in replication & backups
* Monitoring via CloudWatch / CloudTrail
  * You can see which user queries consuming much resources and optimize based
    on that data.

#### Redshift Use-Cases
* Accelerate analytics workloads
  * If you just want to have your DW faster, move to Redshift
* Unified data warehouse & data lake
  * Spectrum is a way to import unstructured data into Redshift as a table  
* Data warehose modernization
* Analyze global sales data
* Store historical stock trade data
* Analyse ad impressions & clicks
* Aggregate gaming data
* Analyze social trends

#### Redshift Architecture
* We have clusters:
  * A cluster is a core infrastructure component of an AWS Redshift datawarehouse
  * A cluster is composed of a leader node and one or more compute nodes
  * It can contain between 1 and 120 compute nodes depending on the node type
  * Each cluster can contain 1 or more databases
  * The user data is going to be stored on the compute nodes.
  * The leader node is just managing the communication between client programs
    and the communication with the compute nodes. It's sort an interface between
    you external clients to redshift and compute nodes under the hood. It
    receives the queries from the clients, parses the queries and develops
    execution plans which are an ordered steps to process those queries.It then
    coordinates parallel execution of those plans with the compute nodes and
    aggregates the intermediate results from the compute nodes. Finally the
    leader node will turn those results back to the client application.
  * Compute nodes are responsible to execute the steps specified in the
    execution plan that it's getting for the leader node and transmitting data
    among themselves to server those queries. It then sends those intermediate
    results back to the leader node for aggregation before sent back to the
    client application. Each compute node has its own cpu, memory and attached
    disk storage, which are determent by the node type you choose. There are two
    different types:
      * DS (dense storage) type: allows you to create very large datawarehouse
        using hard disk drives (hdd) for a very low price points. These are
      * DC (dense compute) type: allows you to create fast performing node types
        with lots of CPU, large amounts of RAM, and SSD (solid state disks).
      * Compute nodes can be aither DS or DC if you want to optimize for
        computing or storage capacity. 
    * Every compute node is divided into slices. And a portion of the memory in
      the space is going to be allocated to each slice. Where processes a
      portion of a work Slices process a chunk of a data given to it.load assigned to that node. The number of slices per node
      is determined by the node size of the cluster. Slices process a chunk of a
      data given to it.
![storage](https://panoply.io/uploads/versions/media-20170927-4---x----713-354x---.png)

![redshift](https://hevodata.com/blog/wp-content/uploads/2017/10/Screen-Shot-2017-10-11-at-3.14.59-PM.png)

#### Redshift Spectrum
* Query exabytes of unstructued data in S3 without loading (into a cluster) or transforming that
  data
* Limitless concurrency
* Horizontal scaling
* Separate storage & compute resources
  * Allows you to separate and scale independently
    * Storage is done in s3
    * Spectrum is just doing the compute part to analyse that data
* Wide variety of data formats
  * Avro
  * CSV
  * Grok
  * ION
  * JSON
  * ORC
  * Parquet
  * RC
  * Regex
  * Sequence files
  * Text files
  * TSV
* Support of Gzip and Snappy compression
  * To save space and bandwidth
* AWS Glue Catalog does makes tables on top of your S3 data.
* Instead of looking like a console based SQL engine like in Athena, it just
  looks like another table in the databse
* That way you can have tables that embody your S3 data lake, alongside with
  tables that embody data that is stored on the Redshift cluster itself. You can
  treat them as the same thing and join them or whatever you want to do.
* Amazon Redshift Spectrum ---> AWS Glue Catalog ---> S3
* Why is Redshift so fast?
  * It uses massively parallel processing (MPP)
    * Data and quering is distribitued across all nodes
    * Does all your queries in parallel. If you need more speed, just add more
      nodes to your cluster.
  * Columnar Data Storage
    * Ideas for large data set queriying
    * Typically you just looking at specific column
    * Requires far less IO
    * Amazon automatically converts the data that enters the system into
      Columnar Data Storage format.
    * Not for OLTP only for OLAP
    * Uses block size of 1 MB
  * Column Compression
    * Compared to row based data stores, columnar-based data stores can
      generally be compressed much more, as it all sequentially stored on disk
      at the same type of data format.
    * Multiple compression techniques are often applied for better results. So
      indexes or materialized views are not required for Redshift and uses less
      space. It will automatically sample the data and select the most
      appropriate compression scheme when the data is loaded into an empty
      table.
    * It reduces the size of the data when it is stored. And the size of data
      when it's read from the storage. It reduces disk IO and therefore improves
      your query performance.
    * When you load your data into a Redshift cluster, usually you use a copy
      command to do that most efficiently. It allows you to copy the data into
      distributed parallelized manner. When you issue that copy command it will
      automatically analyse and apply that compression automatically.
    * It's not possible to change the compression encoding after the table is
      created. CheckAnalysisCommand produces report about the compression.

#### Redshift Durability
* Replication within cluster
* Backup to S3
  * Asynchronously replicated to another region
  * 3 copies of the data are maintained (data is stored on 3 places)
    * On the original (within your cluster)
    * On the replica of compute nodes (replica copy on your copy)
    * On backup on S3  (async S3 backup)
* Automated spanshots
  * 1 day retention is by default
  * You can increase to 35 days
  * If you turn your retention period down to 0, automated backups will be
    turned off
* Failed drives / nodes automatically replaced
  * If you need to restore one of your backups. You choose the backup you want
    and AWS will provision a new data warehouse cluster and restore your data to
    it. You can switch over to the newly restored cluster from the old one.
  * In event of drive failure Redshift cluster will be available with a slight
    performance hit in the quries. While Redshift rebuilds that drive from a
    replica on that drive which is stored on another drive on that node. 
  * Single node clusters do not support data replication because nothing is
    replicated too. In that case you have to restore your cluster from a
    snapshot in S3 instead.
  * In event of node failure, the cluster will be unavailable for query and
    updates utill it's fully restored. Mostly accessed data from S3 is loaded
    frist.
  * Single node cluster, don#t support data replication. You need to restore
    that cluster from S3 in case of a node failure on a single node cluster.
  * In production you should have at least two nodes in your cluster.
* However - limitied to a single availablity zone (AZ)
  * In case of AZ outtage, you will not able to access your cluster until power
    and access is restored.
  * You can restore a snapshot to a new availability zone within the same
    region.
  * Your mostly accessed data will be restored first from S3, so you can resume
    your queries.
  * Redshift support single AZ deployment. So when an entire zone goes down, you
    would have to restore data from S3 to different AZ.

#### Scaling Redshift
* Vertical (increasing the node instance type) and horizontal (increasing the
  number of nodes) scaling on demand
* During scaling (requiest for changed applies immediately):
  * A new cluster is created while your old one remains available for reads
  * CNAME is flipped to new cluster ( a few minutes downtime)
    * CNAME is a canonical name record or alias record. A type of resource
      record in the domain name system (dns), that specifies that one domain
      nameis an alieas of another canonical domain name.
  * Data moved in parallel to new compute nodes

#### Redshift Deistribution Styles
* Data is distributed across compute nodes and slices on the compute nodes.
* There are several ways of doing that distribution. When data is loaded into a
  table, Redshift will distribute that data into compute nodes and slices
  according to the distribution style that you chose, when you created the
  table.
* Two goals of data distirbution:
  * To distribute the workload uniformely among the nodes in the cluster and to
    minimise query execution. There 4 different distribution styles:
* AUTO
  * If you don't specify distirbution style. Amazon Redshift uses
    auto-distribution and based on the size of the table data. Redshift will
    assign an optimal distribution style for you and that might be:
      * EVEN
        * Regarding the data in the table, the leader node disributes that data
          in a round-robin fashion. It's going to step through each individual
          slice and keep assigning new data to each slice in a circular manner.
        * This is appropriate when the table doesn't participate in joins or
          when there is not a clear choice between a KEY distribution or ALL
          distribution. Just spreads the data as even as possible w/o trying to
          cluster data that might be accessible at the same time.
        * Rows distributed across slices in round-robin
      * KEY
        * The rows are distributed acording the values in one column.
        * Leader node will place matching values on the same node slice
        * And matching values of the common columns are physically stored
          together
        * Use case: when you do query on specific columns on your data, by using
          KEY distribution you can make sure that associated data with a
          specific key value will be located on the same slice. Can speed up
          your queries. Based on key hashes!
        * Rows distributed based on one column
      * ALL
        * A copy of an entire table is distributed on every node.
        * That ensures that every row is co-located for every join that a table
          will participate in. 
        * It multiplies the storage requirements by the number of nodes in the
          cluster. It takes much longer to upload or insert data into multiple
          tables. 
        * Only appropriate for really slow moving tables. Tables that are not
          updated frequently or extensively. 
        * You can query the ssvinfoview it will show the current distribution
          style for that table. 
        * **Important:** it's not possible to change the style of the table
          after it has been created. If you want to use a different distribution
          style you have to recreate that table and populate the new table with
          a deep copy.
        * Entire table is copies to every node

#### Redshift Sort Keys
* Sort keys are similar to indexes like in RDS
* In Redshift a column can be a sort key
* Allows you to skip over entire of ranges of data very quickly
* Rows are stored on disk in sorted order based on the column you designate as a
  sort key
* Like an index
* Makes for fast range queries
  * Min and max values will be stored as part of the metadata
* Choosing a sort key
  * Recency?: if recent data is quered frequently, you need to specify the
    timestamp column as a leading column for the sort key. That will help to
    skip the entire blocks that fall outside of time range. 
  * Filtering?: If you do equality filtering on one column. Specify that column
    as a sort key. Redshift can skip reading entire blocks of that data column,
    because it tracks min/max values stored on each block and can skip blocks
    that don't apply to that predicate range.
  * Joins?: specify the join column as both the sort key and the disribution
    key. That would a query optimizer to choose a sort/merge join instead of
    lower hash join. 
* Single vs. 
  * Using a single key to sort the data. Useful when you consistently querying
    the data within a single filter column. If you querying primarily by date
    you might choose a single column sort key by date. 
* Compound vs. 
  * Is made of all the columns listed in the sort key defintion. In the order
    they are listed in. Most useful when a filter applies conditions such as
    filters and joins that use prefix of the sort keys. Performance can decrease
    when keys depend on only secondary sort columns without referncing the
    primary column. You need to think about the order of the columns.
  * Compound is the default sort type. Also helps to improve compression. 
* Interleaved sort keys
  * Interleaved gives equal weight to each column or a subset of columns in the
    sort key. Can be useful if multiple queries use for different filters. It
    uses internal compression scheme for zone map...

![sort keys](./img/sort-keys.png)

#### Redshift Data Flows: Importing/Exporting data
* Important topic for the examp: importing/exporting data from a Redshift
  cluster
* COPY command (import data):
  * You can read from multiple data streams simultaneously
  * Parallelized; efficient
  * From S3, EMR, DynamoDB, remote hosts
  * S3 requires a manifest file and IAM role
    * Use S3 prefix to load data from S3 followed by authorization
    * You can also a manifest json file that sits in S3 and lists the data you
      want to load. 
* UNLOAD command (export data):
  * Unload form a table into files in S3
* Enhanced VPC routing
  * Force of your copy and unload traffic between your cluster and the
    repositories through your Amazon VPC. Otherwise all of that copy and unload
    traffic will be routed through the internet. For this to work you need to
    configure your VPC correctly or your copy or unload functions will fail.  

#### Redshift copy grans for cross-region snapshot copies
* Let's say you have a KMS-encrypted Redshift clsuter and a snapshot of it
* You want to copy that snapshot to another region for backup
* In the destination AWS region:
  * Create a KMS key if you don't have one already
  * Specify a unique name for your snapshot copy grant
  * Specify the KMS key ID for which you're creating the copy grant
* In the source AWS region:
  * Enable copying of snapshots to the **copy grant** you just created

#### DBLINK
* Connect Redshift to PostgreSQL (possibly in RDS might be hosted on AWS)
* You can get best of both world: columnar storage (redshift) and row-based
  storage (PostgreSQL)
* PostgreSQL cluster and Redshift cluster has to be in the same AZ
  * You connect VPC securiy group on Redshift cluster to allow connection from
    the RDS PostgreSQL endpoint. You then connect RDS endpoint and run the SQL
    code to establish that DBLINK connection between RDS instance and AWS
    Redshift.
* Good way to copy and sync data between PostgreSQL and Redshift

#### Integration with other services
* S3
  * You can use parallel processing to export your Redshift data to S3
  * You can also import data from S3 or sitting on top using Spectrum
* DynamoDB
  * By using a copy command you can also load a Redshift table using single
    Amazon DynamoDB Table. 
* EMR / EC2
  * You can import data using ssh via the copy command. You can load data from
    one or more remote hosts such as EMR, or EC2
* Data Pipeline
  * Automate the data movement in/out of Redshift and transformation tables
* Database Migration Service (DMS)
  * Can migrate your data into Redshift for you (help you with the process)

#### Redshift Workload Managemetn (WLM)
* It's a way users to prioritize workloads so that fast running queries are not
  stuck behind long running queries (slow). It works by creating a query queues
  at runtime according to service classes. And configuration parameters are
  defined by those service classes.
* Prioritize short, fast queries vs. logn, slow queries
* Query queues
* Via console, CLI or API
  * You can modify the settings of the service classes

#### VACUUM command
* Recovers space from deleted rows and to restor the sort order. It cleans up
  your table.
* VACUUM FULL: It will resort all the rows and reclaim space from deleted rows
  (default)
* VACUUM DELETE ONLY: is the same as the FULL it skips the sorting part. It's
  reclaiming deleted row space and not sorting
* VACUUM SORT ONLY: will resort the table but not reclaim disk space
* VACUUM REINDEX: reinitializing interleaved indexes and perform a FULL VACUUM
  operation after that

#### Redshift anti-patterns
* Small data sets
  * Use RDS instead
* OLTP
  * Use RDS or DynamoDB instead
* Unstructued data
  * ETL first with EMR etc.
* BLOB (binary large object) data
  * Store references to large binary files in S3, not the files themselves

#### Security on a Redshift Cluster
* KMS
* HMS - security on Redshift if you have hardware security possibilities

#### Other
* If you want to query S3 data from S3 with Spectrum you need to use Glue Data
  Catalog for this reason. 

#### Amazon RDS
* For small data not for big data
* Hosted relational database
  * Amazon Aurora
  * MySQL
  * PostgreSQL
  * MariaDB (open source version of MySQL)
  * Oracle
  * SQL Server
* Not for "big data"
  * Might appear on exam as an example of what not to use
  * Or in the context of migrating from RDS to Redshift etc.

#### ACID
* RDS databses offer full ACID complience
  * Atomicity: ensures that the transaction as a whole is successfully executed,
    or if a part of a transaction fails it makes sure that the whole transaction
    is invalidated.
  * Consistency: ensures that the data written to db as part of the transaction
    must adhere to all defined rules, restrictions including constrains,
    cascades and triggers
  * Isolation: ensures that each transaction is independent to itself, critical
    in achieving concurrency control
  * Durability: ensures that all of the changes made to the database are
    preminent once the transaction is successfully completed

#### Amazon Aurora
* MySQL and PostgreSQL compatible
* up to 5x faster then MySQL, 3X faster than ProstgreSQL
* 1/10 the cost of commercial databases
* Up to 64TB per database instance
* Up to 15 read replicas
* Continuous backup to S3
* Replication across availability zones
* Automatic scaling with Aurora Serverless

#### Aurora Security
* VPC network isolation
* At-rest with KMS
  * Data, backup, snapshots, and replicas can be encrypted
* In-transit with SSL 
