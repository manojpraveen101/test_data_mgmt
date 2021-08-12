pipeline {

    agent any

     environment {
        AIRFLOW_VERSION = '1.10.10'
    }

    stages {
        stage("Dependency install") {
            steps {
                echo 'Hello world!'
                sh "pip install apache-airflow==${AIRFLOW_VERSION}"
//                 sh "airflow version"
            }
        }
        stage("Running test") {
            steps {
                sh "python3 test_data_management/get_airflow_backfill_commands.py"
            }
        }

    }
}
