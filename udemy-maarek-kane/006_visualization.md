### Amazon QuickSight
* It's not made for a developer, it's made for business people
* Business analytics in the cloud
* Fast, easy, cloud-powered business analytics service
* Allows all employees in an organization to:
  * Build visualization
  * Perform ad-hoc analysis
  * Quckly get business insights from data
  * Anytime, on any device (browsers, mobile)
* Serverless

#### QuckSight Data Sources
* Redshift
* Aurora / RDS
* Athena
* EC2-hosted databases
* Files (S3 or on-premises)
  * Excel
  * CSV, TSV
  * Common or extended log format
* Data prepartion allows limited ETL

#### SPICE
* QuickSight is not sitting on top of your data through some JDBC interface.
  It's actually importing your data sets into a engine that is called SPICE.
* Data sets are imported in SPICE
  * Super-fast, Parallel, In-memory Calculation Engine
  * Uses columnar storage, in-memory, machine code generation
  * Accelerates interactive queries on large datasets
* Each user gets 10GB of SPICE - every user on QuickSight gets 10GB of SPICE
* Highly available / durable
* Scales to hunders of thousand of users

#### QuickSight Use Cases
* Interactive ad-hoc expolration / visualization of data
* Dashboards and KPI's
* Stories:
  * Guided tours through specific views of an analysis
  * Convery key points, through process, evolution of an analysis
* Analyze / visualize data from:
  * Logs in S3
  * On-premise databases
  * AWS (RDS, Redshift, Athena, S3)
  * SaaS applications, such as Salesforce
  * Any JDBC/ODBC data source

#### QuickSight Anti-Patterns
* Highly formatted canned reports
  * QS is for ad-hoc queries, analysis, and visualization
* ETL
  * use Glue instead, although QS can do some transformations

#### QS Security
* Multi-factor authentication on your account
* VPC connectivity
  * Add QS's IP address range to your database security group
* Row-level security
* Private VPC access
  * Elastic Network Interface (ENI), AWS Direct Connect (for on-premises
    databases or files)

#### QS User Management
* There are two editions of QS: standard & enterprise
  * In the standard: users defined via IAM, or email signup (just email like
    another email based service)
  * In the enterprise: Active directory integration with QS enterprise edition


#### QS Pricing
* Annual subscription
  * Standard: $9 / user / month
  * Enterprise: $18 / user / month
* Extra SPICE capacity (beyond 10GB)
  * $0.25 (standard) $0.38 (enterprise) / GB / month
* Month to month:
  * Standard: $12 / GB / month
  * Enterprise: $24 / GB / month
* Enterprise edition
  * Encryption at rest
  * Microsoft Active Directory integration

#### QuickSight Visual Types
* AutoGraph
  * If you select some columns in QS it will automatically try to figure out
    what kind of visual to present that kind of information. It select the most
    appropriate visualizations based on the property of the data.
* Bar Charts
  * For comparison and distribution (histograms - bucket things by certain
    ranges - e.g. airplane arriveal in 2m buckets, and grouping it together into
    a single bar)
  * If you want to compare the qunatitiy of different things together.
![ww2](https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Human_losses_of_world_war_two_by_country.png/310px-Human_losses_of_world_war_two_by_country.png)
* Line graphs
  * For change over time
![de](https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/De_wanderung.svg/2000px-De_wanderung.svg.png)
* Scatter plots, heat maps
  * For correlation
  * Linear relationship between two dimensions of data
  * Heat maps can be used to with 2 dimensions
![scatter](https://chartio.com/images/tutorials/scatter-plot/Scatter-Plot-Weight-and-Height-Scatter-Plot-Trendline.png)
![heat
map](https://sebastianraschka.com/images/blog/2013/heatmaps_in_r/heatmaps_in_r.png)
* Pie graphs, tree maps (is a hierarchical pie chart = tree map)
  * For aggregation
  * How different components of something add up to a whole
![pi](https://www.mathsisfun.com/data/images/pie-chart-movies.svg)
![tree
map](https://i.redd.it/hhzz8640oqk11.png)
* Pivot tables
  * Used for tabular data and if you want to aggregate that data in a
    statistical way or apply some functions to it a pivot table is the way to do
    that
  * For tabular data
  * Multi-dimensional data
![pivot](https://www.maketecheasier.com/assets/uploads/2017/12/Pivot-Tables-Featured.jpg)
* Stories
  * Create a narative create iterations of your analysis that people can dive in
    and explore
  * You can create a story by using the capture button. These are used to show
    the thought process or the evolution of an analysis.
  * You can capture them and annotate specific states of your analysis.
  * When readers of the story, click on the image in the story, they are taken
    into analysis at that point.

#### Questions
* Your manager has asked you to prepare a visual on QuickSight to see trends in
  how money was spent on entertainment in the office in the past 12 months. What
  visual will you use? 
    * Line Chart
* You wish to publish a visual you've created illustrating trends of work coming into your company, for your employees to view. Which tool in QuickSight would be appropriate?
  * A dashboard is a way to publish a screen of data to a larger audience.
* You want to build a visualization from the data-set you have imported, but you are unsure what visual to select for the best view. What can you do?
  * Auto-graph will automatically try to select the most appropriate visualization type for the data you have selected.
* The source data you wish to analyze is not in a clean format. What can you do to ensure your visual in QuickSight looks good, with a minimum of effort?
  * Select edit / preview data before loading it into analysis, and edit it as
    needed
* How can you point QuickSight to fetch from your database stored on the EC2 instance in your VPC ?
  * Add Amazon QuickSight IP range to the allowed IPs of the hosted DB

#### Alternative Visualization Tools
* Web-based visualization tools (deployed to the public)
  * D3.js (data driven documents)
  * Charts.js
  * Hightcharts.js
* Business intelligence Tools
  * Tableau
  * MicroStrategy
