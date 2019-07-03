# SparkSQL / Data Frames and DataSets


### SparkSQL
* Let you deal with structured data instead of RDD's that can different
  information in every row, we can give our rows structure and treat RDD's as
  little databases. We will call them Data Frames and DataSets and you can
  perform SQL-queries and SQL-like operations  
* Extends RDD to a DataFrame object (imparting some structure)
* DataFrames:
  * Contain Row objects
  * Can run SQL queries
  * Has a schema (leading to more efficient storage)
  * Read and write JSON, Hive, parquet
  * Communicates with JDBC/ODBC, Tableau

```py
from pyspark.sql import SQLContext, Row
hiveContext = HiveContext(sc)
inputData = spark.read.json(dataFile)
inputData.createOrReplacteTempView('myStructuredStuff')
# create a table in memory to issue SQL queries on that
myResultDataFrame = hiveContext.sql("""SELECT foo FROM bar ORDERED BY
foobar""")

myResultDataFrame.show()
myResultDataFrame.select('someFieldName')
myResultDataFrame.filter(myResultDataFrame('someFieldName' > 200))
myResultDataFramw.groupBy(myResultDataFrame('someFieldName')).mean()
myResultDataFrame.rdd().map(mapperFunction)
```

* In Spark 2.0, a DataFrame is a really a DataSet of Row objects
* DataFrame is just an RDD of row objects
* A Dataset is a DataFrame of structured data. It can contain more than just a
  row object it can contain a specific type of class (more important when you
  code in Scala or Java)
* When people talk about DataSets they talk about a DataFrame with structured
  data. A DataFrame is a DataSet of row objects
* DataSets can wrap known, typed data too. But this is mostly transparent to you
  in Python, since Python is untyped
* So - don't sweat this too much with Python. But the Spark 2.0 way is to use
  DataSets instead of DataFramews when you can

* Shell Access:
  * Spark SQL exposes a JDBC/ODBC server (if you built Spark with Hive support)
  * Start it with sbin/start-thriftserver.sh
  * Listen on port 10000 by default
  * Connect using bin/beeline -u djbc:hive2//localhost:10000
  * You have a SQL shell to SparkSQL
  * You can create new tables or query existing ones that were cached using
    hiveCtx.cacheTable('tableName')

* User defined functions (UDF's):
  * You can use UDF to extend SQL-syntax by itself e.g.
  * That will exectued across your cluster automatically

```py
from pyspark.sql.types import IntegerType
hiveCtx.registerFunction("suqare", lambda x: x*x, IntegerType())
df = hiveCtx.sql("select square('someNumberField') from tableName)
``` 

### JSON
* If we are importing unstructured data such as text, we need first to convert
  it to a DataFrame

```py
# Get the raw data
lines = spark.sparkContext.textFile("file:///SparkCourse/ml-100k/u.data")
# Convert it to a RDD of Row objects
movies = lines.map(lambda x: Row(movieID =int(x.split()[1])))
# Convert that to a DataFrame
movieDataset = spark.createDataFrame(movies)
```
* But if we are loading a json file, it creates a DataFrame for us. We don't
  need to convert anything, we can simply operate on it directly.

* You need always to `spark.stop()` to close the session, it's like a connection
  to a database.
