# AWS Athena

### What is Athena
* Interactive query service to analyze data in S3 using standard SQL
* Pay only for queries run, save 30-90% on per-query cost through compression
* Mix of Presto & Hive
* Pay per query
* 5$ per TB scanned from S3
* DDL Queries and failed queries are free
* Save by using compression, partitions
* Raw logs -> structured logs -> staging S3 bucket -> AWS Glue -> Final S3
  Bucket -> Athena -> SQL
* Create partitions on S3 with Glue ETL

### Athena Features
* You can use Athena to run ad-hoc queries using ANSI SQL, without the need to
  aggregate or load the data into Athena
* In Athena, tables and databases are containers for the metadata definitions
  that define a schema for underlying source data. For each dataset, a table
  needs to exists in Athena
* The metadata in the table tells Athena where the data is located in S3, and
  specifies the structure of the data, for example, column names, data types,
  and the name of the table
* Databases are a logical grouping of tables, and also hold only metadata and
  schema information for a dataset
* For each dataset that you'd like to query, Athena must have an underlying
  table it will use for obtaining and returning query results. Therefore, before
  querying data, a table must be registered in Athena
* Regardless of how the tables are created, the tables creation process
  registers the dataset with Athena. This registration occurs either in the AWS
  Glue Data Catalog, or in the internal Athena data catalog and enables Athena
  to run queries on the data
* You use the internal Athena data catalog in regions where AWS Glue is not
  available and where the AWS Glue Data Catalog cannot be used
* The AWS Glue Data Catalog is accessible thorughout your AWS account. Other AWS
  Services can share the AWS Glue Data Catalog, so you can see databases and
  tables created throughout your organization using Athena and vice versa
* In addition, AWS Glue lets you automatically discover data schema and extract,
  transform, and load (ETL) data
* When you create tables and databases manually, Athena uses HiveQL data
  definition language DDL statements such as `create table, create database, and
  drop table` under the hood to create tables and databases in the AWS Glue Data
  Catalog
* Athena uses IAM policies to restrict access to Athena operations. Encryption
  options enable you to encrypt query result files in S3 and query data
  encrypted in S3. Users must have the appropriate permissions to access S3
  location and decrypt files


### Athena Object Model
#### Athena Tables
* You can run DDL statements in the Athena console, using a JDBC or an ODBC
  driver, or using the Athena Create Table wizard
* When you create a new table schema in Athena, Athena stores the schema in a
  data catalog and uses it when you run queries
* Athen auses an approach known as `schema-on-read`, which means a schema is
  projected on to your data at the time you execute a query. This eliminates the
  need for data loading or transformation
* Athena does not modify your data in S3
* Athena uses Hive to define tables and create databases, which are essentially
  a logical namespace of tables
* When you create a database and table in Athena, you are describing the schema
  and the location where the table data are locate din S3 for read-time
  querying. Database and table, therefore, have a slightly differente meaning
  that they do for traditinonal relational database systems because the data
  isn't stored along with the schema definition for the database and table
  (compute / storage)
* Athena query enginge is based on Hive DDL
* When you query, you query the table using standard SQL and the data is read a
  that time
* The maximum query string lenght is 256KB
* Hive supports multiple data formats through the use of a
  serializer-deserializer (SerDe) libraries. You can also define schema using
  regex
* Athena stores query results in S3. Each query that you run has a result file
  stored automatically in a CSV format `(*.csv)` and an Athena metadata file
  `(*.csv.metadata)` 


#### Athena Queries
* Athena stores query results in S3
* Athena stores query results in S3. Each query that you run has a result file
  stored automatically in a CSV format `(*.csv)` and an Athena metadata file
  `(*.csv.metadata)` 
* Athena lets you create arrays, concatenate them, convert them to different
  data types, and then filter, flatten and sort them
* Geospatial queries are specialized type of SQL queries supported in Athena.
  They differe fron nonspatial SQL queries in the following ways:
    * Using geospatial queries in Athena, you can run these and other similar
      operations:
      * Find the distance between two points
      * Check whether one are (polygon) contains another
      * Check whether one line crosses or touches another line or polygon

#### Athena DDL Commands

* If you use DDL to create object in Athena. All of those objects are
  automatically registered in the AWS Glue Data catalog

* Below is an example of DDL statement


```sql
CREATE EXTERNAL TABLE IF NOT EXISTS MyFirstAthenaDB.CityDataTarasowski (
  `id` int,
  `country` string,
  `state` string,
  `city` string,
  `amount` double
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe'
WITH SERDEPROPERTIES (
  'serialization.format' = ',',
  'field.delim' = ','
) LOCATION 's3://tarasowski-city-data/CityData/Active/'
TBLPROPERTIES ('has_encrypted_data'='false');
``` 

#### Amazon Athena DDL - Data Types
* primitive data types
* array type
* map type
* struct type

#### DDL Statements
* drop table
* drop database
* msck repair table
* show columns
* show create table
* alter database set dbproperties
* alter table add partition
* database objects are table, views, columns

#### Create Table
* Creates a table with the name and the parameters that you specify
* To run ETL jobs, AWS glue requires that you create a table with the
  classification property to indicate the data type for Glue as csv, parquet,
  orc, avro, json
* For example `classification=csv`. ETL jobs will fail if you do not specify
  this property. You can subsequently specify it using the Glue console

```sql
create external table if not exists db_name.table_name
'classification'='aws-glue_classification'...
```
