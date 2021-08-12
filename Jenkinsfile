pipeline {

    agent any

     environment {
        AIRFLOW_VERSION = '1.10.10'
    }

    stages {

        stage("Dependency install") {
            steps {
                sh "rm -rf drivenbrands4"
                sh "rm -rf drivenbrands5"
                echo 'Airflow installation started'
                sh "pip install apache-airflow==${AIRFLOW_VERSION}"
            }
        }

        stage("Git clone") {
            steps {
                sh "mkdir drivenbrands6"
                dir('drivenbrands6') {
                    echo 'git clone started'
                    git credentialsId: 'github_credentials', url: 'https://github.com/manojpraveen101/test_data_mgmt.git'
                    sh "ls"
                    }
//                 sh "cd drivenbrands6"
//                 sh "ls"
            }
        }

        stage("Running test") {
            steps {
                dir('drivenbrands6'){
                sh "python3 test_data_mgmt/get_airflow_backfill_commands.py"
                sh "ls"
                }
            }
        }

    }


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
//
// sh "rm -rf drivenbrands"
// sh "rm -rf drivenbrands1"