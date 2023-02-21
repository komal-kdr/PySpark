# Databricks notebook source
# DBTITLE 1,Spark – Overview
# MAGIC %md
# MAGIC 
# MAGIC Apache Spark is an open-source, distributed processing system used for big data workloads. It utilizes in-memory caching, and optimized query execution for fast analytic queries against data of any size. It provides development APIs in Java, Scala, Python and R, and supports code reuse across multiple workloads—batch processing, interactive queries, real-time analytics, machine learning, and graph processing.
# MAGIC 
# MAGIC Apache Spark is a lightning fast real-time processing framework. It came into picture as Apache Hadoop MapReduce was performing batch processing only and lacked a real-time processing feature. Hence, Apache Spark was introduced as it can perform stream processing in real-time and can also take care of batch processing.
# MAGIC 
# MAGIC Apart from real-time and batch processing, Apache Spark supports interactive queries and iterative algorithms also. Apache Spark has its own cluster manager, where it can host its application. It leverages Apache Hadoop for both storage and processing. It uses HDFS (Hadoop Distributed File system) for storage and it can run Spark applications on YARN as well.

# COMMAND ----------

# DBTITLE 1,What is PySpark?
# MAGIC %md
# MAGIC 
# MAGIC PySpark is a Spark library written in Python to run Python applications using Apache Spark capabilities, using PySpark we can run applications parallelly on the distributed cluster (multiple nodes).
# MAGIC 
# MAGIC In other words, PySpark is a Python API for Apache Spark. Apache Spark is an analytical processing engine for large scale powerful distributed data processing and machine learning applications.
# MAGIC 
# MAGIC Spark basically written in Scala and later on due to its industry adaptation it’s API PySpark released for Python using Py4J. Py4J is a Java library that is integrated within PySpark and allows python to dynamically interface with JVM objects, hence to run PySpark you also need Java to be installed along with Python, and Apache Spark.

# COMMAND ----------

# DBTITLE 1,Who uses PySpark?
# MAGIC %md
# MAGIC 
# MAGIC PySpark is very well used in Data Science and Machine Learning community as there are many widely used data science libraries written in Python including NumPy, TensorFlow. Also used due to its efficient processing of large datasets. PySpark has been used by many organizations like Walmart, Trivago, Sanofi, Runtastic, and many more.

# COMMAND ----------

# DBTITLE 1,Features of PySpark
# MAGIC %md
# MAGIC 1. In-memory computation
# MAGIC 2. Distributed processing using parallelize
# MAGIC 3. Can be used with many cluster managers (Spark, Yarn, Mesos e.t.c)
# MAGIC 4. Fault-tolerant
# MAGIC 5. Immutable
# MAGIC 6. Lazy evaluation
# MAGIC 7. Cache & persistence
# MAGIC 8. Inbuild-optimization when using DataFrames
# MAGIC 9. Supports ANSI SQL

# COMMAND ----------

# DBTITLE 1,Advantages of PySpark
# MAGIC %md
# MAGIC 
# MAGIC 1. PySpark is a general-purpose, in-memory, distributed processing engine that allows you to process data efficiently in a distributed fashion.
# MAGIC 2. Applications running on PySpark are 100x faster than traditional systems.
# MAGIC 3. You will get great benefits using PySpark for data ingestion pipelines.
# MAGIC 4. Using PySpark we can process data from Hadoop HDFS, AWS S3, and many file systems.
# MAGIC 5. PySpark also is used to process real-time data using Streaming and Kafka.
# MAGIC 6. Using PySpark streaming you can also stream files from the file system and also stream from the socket.
# MAGIC 7. PySpark natively has machine learning and graph libraries.

# COMMAND ----------

# DBTITLE 1,PySpark Architecture
# MAGIC %md
# MAGIC Apache Spark works in a master-slave architecture where the master is called “Driver” and slaves are called “Workers”. When you run a Spark application, Spark Driver creates a context that is an entry point to your application, and all operations (transformations and actions) are executed on worker nodes, and the resources are managed by Cluster Manager.

# COMMAND ----------

# DBTITLE 1,PySpark Modules & Packages
# MAGIC %md
# MAGIC 1. PySpark RDD (pyspark.RDD)
# MAGIC 2. PySpark DataFrame and SQL (pyspark.sql)
# MAGIC 3. PySpark Streaming (pyspark.streaming)
# MAGIC 4. PySpark MLib (pyspark.ml, pyspark.mllib)
# MAGIC 5. PySpark GraphFrames (GraphFrames)
# MAGIC 6. PySpark Resource (pyspark.resource) It’s new in PySpark 3.0
# MAGIC 
# MAGIC 
# MAGIC Besides these, if you wanted to use third-party libraries, you can find them at [https://spark-packages.org/]
# MAGIC This page is kind of a repository of all Spark third-party libraries.

# COMMAND ----------

# DBTITLE 1,Apache Spark Workloads/Components
# MAGIC %md
# MAGIC The Spark framework includes:
# MAGIC 
# MAGIC Spark Core as the foundation for the platform
# MAGIC 
# MAGIC Spark SQL for interactive queries
# MAGIC 
# MAGIC Spark Streaming for real-time analytics
# MAGIC 
# MAGIC Spark MLlib for machine learning
# MAGIC 
# MAGIC Spark GraphX for graph processing
# MAGIC 
# MAGIC 
# MAGIC <h2><b>1. Spark Core</b></h2>
# MAGIC Spark Core is the foundation of the platform. It is responsible for memory management, fault recovery, scheduling, distributing & monitoring jobs, and interacting with storage systems. Spark Core is exposed through an application programming interface (APIs) built for Java, Scala, Python and R. These APIs hide the complexity of distributed processing behind simple, high-level operators.
# MAGIC 
# MAGIC <h2>2. MLlib</h2>
# MAGIC <b>Machine Learning</b>
# MAGIC Spark includes MLlib, a library of algorithms to do machine learning on data at scale. Machine Learning models can be trained by data scientists with R or Python on any Hadoop data source, saved using MLlib, and imported into a Java or Scala-based pipeline. Spark was designed for fast, interactive computation that runs in memory, enabling machine learning to run quickly. The algorithms include the ability to do classification, regression, clustering, collaborative filtering, and pattern mining.
# MAGIC 
# MAGIC <h2>3. Spark Streaming</h2>
# MAGIC <b>Real-time</b>
# MAGIC Spark Streaming is a real-time solution that leverages Spark Core’s fast scheduling capability to do streaming analytics. It ingests data in mini-batches, and enables analytics on that data with the same application code written for batch analytics. This improves developer productivity, because they can use the same code for batch processing, and for real-time streaming applications. Spark Streaming supports data from Twitter, Kafka, Flume, HDFS, and ZeroMQ, and many others found from the Spark Packages ecosystem.
# MAGIC 
# MAGIC <h2>4. Spark SQL</h2>
# MAGIC <b>Interactive Queries</b>
# MAGIC Spark SQL is a distributed query engine that provides low-latency, interactive queries up to 100x faster than MapReduce. It includes a cost-based optimizer, columnar storage, and code generation for fast queries, while scaling to thousands of nodes. Business analysts can use standard SQL or the Hive Query Language for querying data. Developers can use APIs, available in Scala, Java, Python, and R. It supports various data sources out-of-the-box including JDBC, ODBC, JSON, HDFS, Hive, ORC, and Parquet. Other popular stores—Amazon Redshift, Amazon S3, Couchbase, Cassandra, MongoDB, Salesforce.com, Elasticsearch, and many others can be found from the Spark Packages ecosystem.
# MAGIC 
# MAGIC <h2>5. GraphX</h2>
# MAGIC <b>Graph Processing</b>
# MAGIC Spark GraphX is a distributed graph processing framework built on top of Spark. GraphX provides ETL, exploratory analysis, and iterative graph computation to enable users to interactively build, and transform a graph data structure at scale. It comes with a highly flexible API, and a selection of distributed Graph algorithms.
