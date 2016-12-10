# Wenxiao Song final project

## Introduction

This final project contains five analysis. The first two analysis are trying to check that whether the supporting rate of Democrat and Republican has something to do with poverty rate or unemployment rate. The third one is trying to show that the median household income of all the state in the US. The last two analysis are trying to show some information about the certain state.

## Data Source description

The data source contains in 15 csv files. [Link to the data source](https://github.com/songwenxiao/DataAnalysisWithPython/tree/master/final/data). 
The first, forth and fifth analysis are based on [xaa.csv](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/data/xaa.csv), [xab.csv](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/data/xab.csv), [xac.csv](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/data/xac.csv) and [xad.csv](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/data/xad.csv). 
The second analysis are based on all the csv file.
The third analysis are based on [xaa.csv](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/data/xaa.csv), [xab.csv](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/data/xab.csv), [xac.csv](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/data/xac.csv), [xad.csv](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/data/xad.csv) and [Unemployment.csv](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/data/Unemployment.csv)

The [xaa.csv](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/data/xaa.csv), [xab.csv](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/data/xab.csv), [xac.csv](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/data/xac.csv) and [xad.csv](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/data/xad.csv) are splited from one data file [usa-2016-presidential-election-by-county.csv](https://public.opendatasoft.com/explore/dataset/usa-2016-presidential-election-by-county/table/). They have the same columns.
The columns of these files are covered from state, county, votes, race ratio, poverty rate, business structure to age distriubtion. 
The sample data are shown below:

![alt tag](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/images/Screen%20Shot%202016-12-10%20at%202.03.12%20PM.png)
![alt tag](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/images/Screen%20Shot%202016-12-10%20at%202.03.41%20PM.png)
![alt tag](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/images/Screen%20Shot%202016-12-10%20at%202.04.12%20PM.png)

The [Unemployment.csv](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/data/Unemployment.csv) contains some useful informations like state, unemployment rate from 2007 to 2015. 

The sample data of [Unemployment.csv](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/data/Unemployment.csv) are shown below:

![alt tag](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/images/Screen%20Shot%202016-12-10%20at%202.17.38%20PM.png)

The [est05All.csv](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/data/est05ALL.csv) to [est14All.csv](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/data/est14ALL.csv) contains information like state, county, median househould income.

The sample data of [est05All.csv](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/data/est05ALL.csv) are shown below:

![alt tag](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/images/Screen%20Shot%202016-12-10%20at%202.28.23%20PM.png) ![alt tag](https://github.com/songwenxiao/DataAnalysisWithPython/blob/master/final/images/Screen%20Shot%202016-12-10%20at%202.28.15%20PM.png)



## Building Spark

Spark is built using [Apache Maven](http://maven.apache.org/).
To build Spark and its example programs, run:

    build/mvn -DskipTests clean package

(You do not need to do this if you downloaded a pre-built package.)

You can build Spark using more than one thread by using the -T option with Maven, see ["Parallel builds in Maven 3"](https://cwiki.apache.org/confluence/display/MAVEN/Parallel+builds+in+Maven+3).
More detailed documentation is available from the project site, at
["Building Spark"](http://spark.apache.org/docs/latest/building-spark.html).

For general development tips, including info on developing Spark using an IDE, see ["Useful Developer Tools"](http://spark.apache.org/developer-tools.html).

## Interactive Scala Shell

The easiest way to start using Spark is through the Scala shell:

    ./bin/spark-shell

Try the following command, which should return 1000:

    scala> sc.parallelize(1 to 1000).count()

## Interactive Python Shell

Alternatively, if you prefer Python, you can use the Python shell:

    ./bin/pyspark

And run the following command, which should also return 1000:

    >>> sc.parallelize(range(1000)).count()

## Example Programs

Spark also comes with several sample programs in the `examples` directory.
To run one of them, use `./bin/run-example <class> [params]`. For example:

    ./bin/run-example SparkPi

will run the Pi example locally.

You can set the MASTER environment variable when running examples to submit
examples to a cluster. This can be a mesos:// or spark:// URL,
"yarn" to run on YARN, and "local" to run
locally with one thread, or "local[N]" to run locally with N threads. You
can also use an abbreviated class name if the class is in the `examples`
package. For instance:

    MASTER=spark://host:7077 ./bin/run-example SparkPi

Many of the example programs print usage help if no params are given.

## Running Tests

Testing first requires [building Spark](#building-spark). Once Spark is built, tests
can be run using:

    ./dev/run-tests

Please see the guidance on how to
[run tests for a module, or individual tests](http://spark.apache.org/developer-tools.html#individual-tests).

## A Note About Hadoop Versions

Spark uses the Hadoop core library to talk to HDFS and other Hadoop-supported
storage systems. Because the protocols have changed in different versions of
Hadoop, you must build Spark against the same version that your cluster runs.

Please refer to the build documentation at
["Specifying the Hadoop Version"](http://spark.apache.org/docs/latest/building-spark.html#specifying-the-hadoop-version)
for detailed guidance on building for a particular distribution of Hadoop, including
building for particular Hive and Hive Thriftserver distributions.

## Configuration

Please refer to the [Configuration Guide](http://spark.apache.org/docs/latest/configuration.html)
in the online documentation for an overview on how to configure Spark.

## Contributing

Please review the [Contribution to Spark guide](http://spark.apache.org/contributing.html)
for information on how to get started contributing to the project.
