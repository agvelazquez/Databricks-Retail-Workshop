# Databricks notebook source
# DBTITLE 1,How to connect Datagrip to Databricks
# https://docs.databricks.com/dev-tools/datagrip.html

# COMMAND ----------

# DBTITLE 1,Mount "retail" blob container
mount_point = "/mnt/retail"

if dbutils.fs.ls('/mnt/retail'):
  print(f'Blob Storage container already mounted')

else:
  storage_account_name = "apuse2digydvsta01data"
  storage_account_access_key = "XDSWUIEgGK/IWhU7WyiUqga/ahBjhw/xMuqb8Hua6R9FEFudURpLciIxsSq/W1r0uO8ais89HEDEiFT8EjJI2A=="
  container = 'retail'

  dbutils.fs.mount(
    source = "wasbs://" + container + "@" + storage_account_name + ".blob.core.windows.net",
    mount_point = mount_point,
    extra_configs = {"fs.azure.account.key." + storage_account_name + ".blob.core.windows.net": "XDSWUIEgGK/IWhU7WyiUqga/ahBjhw/xMuqb8Hua6R9FEFudURpLciIxsSq/W1r0uO8ais89HEDEiFT8EjJI2A=="}
  )
  print(f'{mount_point} succesfully mounted')

# COMMAND ----------

base_folder = mount_point + "/retail_workshop_aug/"

for f in dbutils.fs.ls(base_folder):
  print(f)

# COMMAND ----------

# DBTITLE 1,Create schema (a.k.a database)
# MAGIC %sql 
# MAGIC CREATE SCHEMA IF NOT EXISTS retail_workshop;
# MAGIC 
# MAGIC USE retail_workshop;

# COMMAND ----------

# DBTITLE 1,Load table to staging schema
#Loop trhough 5 csv files (total 30MB) and create table for each of them with schema infered in 36 seconds
file_type = ".csv"
database = "retail_workshop"
schema = "stg"
for f in dbutils.fs.ls(base_folder):
  if file_type in f.name: 
    table_name = f.name.replace(file_type,"")
    df = spark.read.format(file_type.replace(".","")) \
      .option("inferSchema", True) \
      .option("header", True) \
      .option("sep", ',') \
      .load(f.path)

    df.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("{0}.{1}_{2}".format(database,schema,table_name))

# COMMAND ----------

#3 minutes to load 7gb of data (100M records) with correct schema
df_test = spark.read.format("csv") \
      .option("inferSchema", True) \
      .option("header", True) \
      .option("sep", ',') \
      .load('dbfs:/mnt/retail/retail_workshop_aug/fake_100M.csv')

df_test.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("retail_workshop.stg_trips_fake")

# COMMAND ----------

# MAGIC %sql 
# MAGIC CREATE TABLE IF NOT EXISTS retail_workshop.stg_nyc_airlines_v2
# MAGIC USING DELTA
# MAGIC LOCATION 'dbfs:/mnt/retail/retail_workshop_aug/nyc_airlines.csv'

# COMMAND ----------

# MAGIC  %sql 
# MAGIC  describe detail retail_workshop.stg_nyc_airlines
