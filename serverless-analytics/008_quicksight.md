# QuickSight

* Scalable
* Pay for what you use
* Serverless, and fully managed
* Fully integrated into AWS Services Aurora, S3, Athena, Redshift, Rds,
  CloudTrail 
* You can log via Microsoft Active Directory

* On-premises
  * Excel
  * Csv
  * Taradata

* In the cloud
  * Redshift
  * RDS
  * S3

* Applications
  * Salesforce
  * Twitter

### Spice
* Spice a super-fast calculation engine taht delivers unprecedented performance
  and scale delivering insights at the speed of thought.
* Data sources: Connect aws data services; upload files; or connect to apps such
  as Salesforce
* In-memory calculation engine: The super-fast, parallel, in-memory, calucation
  engine ("SPICE") generates answers on large datasets and returns rapid
  responses
* QuickSight UI: SPICE allows for very fast analysis and smart visualization for
  sharing and collaboration

![direct
connect](https://media.amazonwebservices.com/blog/2017/qs_vpc_private_1.png)


### Metrics
* Green in quicksight are measures (sign up, list adds, mobile uniques,
  visitors) - metrics measure data (quantative)
* Blue are dimensions (e.g. date, events) - dimensions describe data
  (qualitative)
* Manifest file is one of the input parameters, that says which files needs to
  be picked up for the analysis
* Below is the content of the manifest file
```json
{
  "entries": [
  {"url": "s3://tarasowski-city-data/CityData.csv", "mandatory": true},
  {"url": "s3://tarasowski-city-data/CityData1.csv", "mandatory": true}
  ]
}
```
* You can give premissions via linking userId from a permission file to the data
  set you need to restrict to specific users.

### Dimensions and Measures
* In the Field list pane, dimensions fileds have blue icons and measure fields
  have green icons.
* Dimensions are text or date fields that may be itmes, like products, or
  attributes that are related to measrures and can be used to partition them,
  like sales date for sales figures
* Measures are numeric values that you use for measurement, comparison and
  aggregation.
* If QuickSight interpreted a field as a measure and you would rather use it as
  a dimension (or the other way around), you can change the setting for that
  field
* Changing a field's measure or dimension setting changes it for all visuals in
  the analysis that use that data set, but does not change it in the data set
  itself.
