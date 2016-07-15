from pyspak.sql import SQLContext
from pyspark import SparkConf, SparkContext

conf = SparkConf().setAppName("Twitter Sentiment Analysis")
sc = SparkContext(conf=conf)
sqlContext  = SQLContext(sc)

df = sqlContext.read.json("C://spark-1.6.1-bin-hadoop2.6//spark-1.6.1-bin-hadoop2.6//examples//src//main//resources//people.json")

df.show()