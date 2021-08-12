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
                sh "mkdir drivenbrands"
                dir('drivenbrands') {
                    echo 'git clone started'
                    git credentialsId: 'github_credentials', url: 'https://github.com/manojpraveen101/test_data_mgmt.git'
                    }
                sh "cd drivenbrands"
                sh "ls"
            }
        }

        stage("Post Condition") {
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

