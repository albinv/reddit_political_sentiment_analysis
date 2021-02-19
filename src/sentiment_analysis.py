from pyspark.sql.types import StructType, StructField, StringType
import pyspark
import sparknlp


def convert_comments_list_to_df(spark_context, sql_context, list_to_convert):
    data = spark_context.parallelize(list_to_convert)

    # Define schema
    schema = StructType([
        StructField("Comment", StringType(), True),
        StructField("Username", StringType(), True)
    ])

    return sql_context.createDataFrame(data, schema)


def perform_analysis(comments_list):
    sc = pyspark.SparkContext('local[*]')
    sql_c = pyspark.sql.SparkSession.builder.appName('reddit_sentiment_analysis').getOrCreate()
    df = convert_comments_list_to_df(sc, sql_c, comments_list)
    print("here")
    df.show()
