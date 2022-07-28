# Databricks notebook source
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


