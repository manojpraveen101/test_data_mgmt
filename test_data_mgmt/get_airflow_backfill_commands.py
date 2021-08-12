import datetime
import fnmatch
import os


def backfill_commands(dag_ids):
    today = datetime.datetime.strftime(datetime.datetime.today(), '%Y-%m-%d')
    previous_date = datetime.datetime.strftime(datetime.datetime.today() - datetime.timedelta(1), '%Y-%m-%d')
    with open('airflow_backfill.txt', 'a') as airflow:
        for dag_id in dag_ids:
            backfill_string = "airflow backfill -m " + dag_id + " -s " + previous_date + " -e " + today
            backfill_string = backfill_string + "\n"
            airflow.write(backfill_string)


with open('airflow_backfill.txt', 'w') as airflow:
    pass


for file in os.listdir('test_data_mgmt'):
    if fnmatch.fnmatch(file, '*pipeline_config.py'):
        file = file.split('.')[0]
        print(file)
        file = __import__(file)
        backfill_commands(file.dag_ids)

