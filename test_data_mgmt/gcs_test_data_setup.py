from google.cloud import storage
import datetime
from utils import copy_gcs_blob
from gcs_pipeline_config import dag_ids
import sys, os

sys.path.append("../../")

from dags.config.dateng_fullslate_kubernetes_config import dag_config, production_env, staging_env, development_env

for dag_id in dag_ids:
    src_file_location = dag_config[dag_id]["gcs_path_prefix"]
    if os.environ["CURRENT_ENVIRONMENT"] == "production_data_replica":
        src_bucket = production_env[dag_id]["src_bucket"]
        src_bucket_vendor = production_env[dag_id]["dest_bucket"]

        dest_bucket = "static-" + development_env[dag_id]["src_bucket"]
        dest_bucket_vendor = "static-" + development_env[dag_id]["dest_bucket"]

    elif os.environ["CURRENT_ENVIRONMENT"] == "development_env":
        src_bucket = "static-" + development_env[dag_id]["src_bucket"]
        src_bucket_vendor = "static-" + development_env[dag_id]["dest_bucket"]

        dest_bucket = development_env[dag_id]["src_bucket"]
        dest_bucket_vendor = development_env[dag_id]["dest_bucket"]

    elif os.environ["CURRENT_ENVIRONMENT"] == "staging_env":
        src_bucket = production_env[dag_id]["src_bucket"]
        src_bucket_vendor = production_env[dag_id]["dest_bucket"]

        dest_bucket = staging_env[dag_id]["src_bucket"]
        dest_bucket_vendor = staging_env[dag_id]["dest_bucket"]

    print(src_bucket, dest_bucket)

    storage_client = storage.Client()
    source_bucket = storage_client.bucket(src_bucket)
    blobs = source_bucket.list_blobs(prefix="")
    blob_list = list(blobs)

    i = -1
    while True:
        blob_name = blob_list[i].name
        blob_size = source_bucket.get_blob(blob_name).size
        blob_size = blob_size / (1024 * 1024)
        print(blob_name, blob_size)
        if dag_config[dag_id]["filename_prefix"] in blob_name and blob_size <= 250:
            print("File size satisfied")
            break
        i = i - 1

    src_blob_name = blob_name

    date = datetime.datetime.today()
    tomorrow_date = datetime.datetime.strftime(date, '%Y%m%d')
    dest_blob_name = dag_config[dag_id]["filename_prefix"] + '_' + tomorrow_date + ".xlsx"

    copy_gcs_blob(src_bucket, src_blob_name, dest_bucket, dest_blob_name)

    src_schema = dag_config[dag_id]["bq_schema_object"]

    if os.environ["CURRENT_ENVIRONMENT"] == "production_data_replica":
        storage_client = storage.Client()
        bucket = storage_client.get_bucket(dest_bucket_vendor)
        blob = bucket.blob(src_schema)
        if blob.exists():
            backup_src_schema = src_schema.replace('.json', '_backup.json')
            copy_gcs_blob(dest_bucket_vendor, src_schema, dest_bucket_vendor, backup_src_schema)

    copy_gcs_blob(src_bucket_vendor, src_schema, dest_bucket_vendor, src_schema)
