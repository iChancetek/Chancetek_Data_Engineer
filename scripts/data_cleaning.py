# Remove rows with null values
cleaned_df = sneaker_spark_df.dropna()

# Rename columns for consistency
transformed_df = cleaned_df.withColumnRenamed('release_date', 'releaseDate') \
                           .withColumnRenamed('id', 'sneakerID')

# Show cleaned and transformed data
transformed_df.show(5)
