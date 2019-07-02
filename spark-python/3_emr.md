# Spark on EMR

* Make sure things run locally on a subset of your data first, use `top(),
  sample()` on your dataset. By doing that you can create a subset to test it
  out, so you don't pay a lot of money for EMR

### Partitioning
* Optimizing for running on a cluster
* Spark isn't totally magic - you need to think about how your data is
  partitioned
* You need to think you to spread the work across executors with partitions
* Running our movie similarity script as-is won't work at all
  * That self-join is expensive, and Spark won't distribute it on its own
* Use `.partitionBy()` on an RDD before running a large operation that benefits
  from partitioning. Into how many pieces can we break RDD that the executor can
  deal with
    * join(), cogroup(), groupWith(), leftOuterJoin(), rightOuterJoin(),
      groupByKey(), reduceBykey(), combineByKey(), and lookup()
    * Those operations will preserve your partitioning in their result too
* **Important**: When you call any of the methods above, do I need to call
  `partitionBy()` first? Odds are you do!!!
* Choosing a partition size:
  * To few partitions won't take full advantage of your cluster
  * Too many results in too much overhead from shuffling data
  * At least as many partitions as you have cores, or executors that fit within
    your available memory
  * `partitionBy(100)` is usually a reasonable place to start for large
    operations. For a cluster of 10 computers!

### Specifying Memory per Executor
* Just use an empty `conf = SparkConf()`, default SparkConf in your driver - this way we'll use the
  defaults EMR set up instead, as well as any command-line options you pass into
  spark-submit from your master node
* In our example, the default executor memory budget is of 512MB is insufficient
  for processing one million movie ratings. So instead we do:
    * `spark-submit --execturo-memory 1g MovieSimilarities1M.py 260` (from the
      master node of our cluster)
    * I knew this because executors kept failing while running with the default
      memory settings
* Can use`--master yarn` to run on a YARN cluster, but if you run it on EMR it
  sets YARN as default cluster manager

### Troubleshooting Spark Jobs
* It is a dark art
* Your master will run a console on port 4040
  * But in EMR, it's next to impossible to actually connect to it from outside
  * If you have your own cluster running on your own network, it can be easy
* You need to troubleshoot if e.g. your jobs are keeping failing, or are to slow
* Logs:
  * In standalone mode, they're in the web UI
  * In Yarn though, the logs are distributed. Yo need to collect them after the
    fact using yarn logs -applicationID <app ID>
* While your driver script runs, it will log errors like executors failing to
  issue heartbeats
    * This generally means you are asking too much of each executor
    * You many need more of them - ie. more machines in your cluter
    * Each executor may need more memory
    * Or use partitionBy() to demand less work from individual executors by
      using smaller partitions
* Managing dependencies, even when something runs on your local machine, it has
  no guarantee to run on the cluster.
* Remember your executors aren#t necessarily on the same box as your driver
  script
* Use broadcast variables to share data outside of RDD's
* Need some Python package that's not pre-loaded on EMR?
  * **Set up a step in EMR to run pip for what you need on each worker machine**
  * Or use -py-files with spark-submit to add individual libraries that are on
    the master
  * Try to just avaoid using obscure packages you don't need in the first place.
    Time is money on your cluster, and you're better off not fiddling with it.

