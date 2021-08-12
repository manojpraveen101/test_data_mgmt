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
//         stage("Running test") {
//             steps {
//                 sh "python3 test_data_mgmt/get_airflow_backfill_commands.py"
//             }
//         }
        stage("Git clone") {
            steps {
                sh "mkdir drivenbrands3"
                dir('drivenbrands3') {
                    echo 'git clone started'
                    git credentialsId: 'github_credentials', url: 'https://github.com/manojpraveen101/test_data_mgmt.git'
                    }
                sh "cd drivenbrands3"
                sh "ls"
            }
        }

        stage("Running test") {
            steps {
                dir('drivenbrands3'){
                sh "python3 get_airflow_backfill_commands.py"
                }
            }
        }

        stage("Post Condition") {
        steps {
        post {

        always {
            echo 'I will always say Hello again!'
        }
        success {
            echo 'Success'
        }
        failure {
            echo 'Failure'
        }

        }
        }
        }

    }
}
//
// sh "rm -rf drivenbrands"
// sh "rm -rf drivenbrands1"