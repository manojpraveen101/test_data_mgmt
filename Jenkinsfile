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
                    sh "ls"
                    dir('test_data_mgmt'){
                        sh "ls"
                    }
                    }

            }
        }

        stage("Running test") {
            steps {
                dir('drivenbrands5'){
                sh "python3 test_data_mgmt/get_airflow_backfill_commands.py"
                sh "ls"
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
        }
        failure {
            echo 'Failure'
        }

        }

}
//
// sh "rm -rf drivenbrands"
// sh "rm -rf drivenbrands1"