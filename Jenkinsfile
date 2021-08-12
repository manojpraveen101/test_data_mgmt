pipeline {

    agent any

     environment {
        AIRFLOW_VERSION = '1.10.10'
    }

    stages {

        stage("Dependency install") {
            steps {
                echo 'Airflow installation started'
                sh "pip install apache-airflow==${AIRFLOW_VERSION}"
            }
        }

        stage("Git clone") {
            steps {
                sh "mkdir drivenbrands5"
                dir('drivenbrands5') {
                    echo 'git clone started'
                    git credentialsId: 'github_credentials', url: 'https://github.com/manojpraveen101/test_data_mgmt.git'
                    }

            }
        }

        stage("Running test") {
            steps {
                dir('drivenbrands5'){
                sh "python3 test_data_mgmt/get_airflow_backfill_commands.py"
                echo "the output file contents is"
                sh "cat airflow_backfill.txt"
                }
            }
        }

    }

        post {

        always {
            sh "rm -rf drivenbrands5"
        }
        success {
            echo 'Success'
            emailext body: 'Status of pipeline :Success', subject: 'Pipeline Status', to: 'manojpraveenkgm@gmail.com'
            mail bcc: '', body: 'done', cc: '', from: '', replyTo: '', subject: 'Pipeline status', to: 'manojpraveenkgm@gmail.com'
        }
        failure {
            echo 'Failure'
            emailext body: 'Status of pipeline :Failure', subject: 'Pipeline Status', to: 'manojpraveenkgm@gmail.com'
        }

        }

}
