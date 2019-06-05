# Section 2

### What is Severless Computing?
* Serve users from zero to planet-scale, all without managing any
  infrastructure ~ Google Cloud Functions 
* Just put your code in the cloud and run it ~ Serverless for Dummies
* IaaS, PaaS, Serverless (only application is important, the underlying
  infrastructure is managed by the provider), SaaS
* On-premise you are not decoupling storage and compute ??
* Run 24h/365 days, can be optimized via Spot instances

![on premise](./img/on-premise.png)

![sls pipeline](./img/serverless-pipeline.png)

* How all these components communicate with each other? See Data Lake

### Data Lake Basics
* Multiple sources and formats are coming every day and the number is growing:
  * Documents and files:
    * Clickstream data
    * Mobile app data
    * Spreadsheets
    * Infrastructure logs
    * Social media
  * Records:
    * Amazon RDS
    * ERP
    * DynamoDB
    * On Premises database
    * Amazon Redshift
  * Streams:
    * AWS IoT
    * Kinesis Streams
    * Device data
    * Kinesis Firehose
    * Sensor data
* Data lake vs. data warehouse
  * Data lake:
    * Semi-structured / unstructured / structured data
    * Schema on read (take the data as it is and store it together)
    * Data scients, predictive analysis, BI use cases
    * Great for storing granular data; raw as well as processed data
    * Separation of compute and storage (store the data on S3, but compute
      depends on what tool you're going to use for analysis)
  * Data warehouse (cetral repository where the data is stored, you create a
    data mart -> for marketing, finance, hr have their own data warehouses):
    * Structured data (STAR or SNOWLFAKE model)
    * Schema on write
    * SQL based BI use cases
    * Grat for storing frequently accessed data as well as data aggregates and
      summary
    * Tightly coupled compute and storage (e.g. Redshift have storage and
      compute is on the same machine)
* Reasons for building a data lake?
  * Exponetial growth in data:
    * Transactions
    * Billing
    * ERP
    * Web logs
    * Sensor data
    * Infrastructure logs
    * Social
  * Diversified consumers:
    * Data scientists (more data is requierd for training and model creation)
    * Applications
    * Business Analysts
    * External Consumers
  * Multiple access mechanisms
    * API Access (web services / micro services)
    * Notebooks (kind of IDE's, Apache Zepplin, Jupyter)
    * BI Tools (endpoint applications)
* Characteristics of a Data lake?
  * Collect and store any data, at any scale, and at low cost
  * Secure the data and prevent unauthorized access
  * Catalogue, search, and discover data
  * Decouple Compute from Storage
  * Future Proof against a highly changing complex ecosystem

