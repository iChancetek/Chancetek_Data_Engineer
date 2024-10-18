from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialize PySpark session
spark = SparkSession.builder.appName("ChancellorDataEngineering").getOrCreate()

# Convert pandas DataFrame to PySpark DataFrame
sneaker_spark_df = spark.createDataFrame(sneaker_df)

# Display PySpark DataFrame schema
sneaker_spark_df.printSchema()

# Show first few rows of the DataFrame
sneaker_spark_df.show(5)
