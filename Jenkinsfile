pipeline {

    agent any

    stages {

        stage("Executing the file") {
            steps {
                sh "python3 test_data_mgmt/get_airflow_backfill_commands.py"
                echo "the output file contents is"
                sh "cat airflow_backfill.txt"
                echo "Running ${env.BUILD_ID}"
                echo "Running ${env.BUILD_NUMBER}"
                echo '${env.BUILD_URL}'
            }
        }

    }

        post {

        always {
            cleanWs()
        }
        success {
            echo 'Success'
            echo '${Env.BUILD_URL}'
            mail bcc: '', body: 'Status of pipeline :Success', cc: '', from: '', replyTo: '', subject: 'Pipeline status', to: 'manojpraveenkgm@gmail.com'
        }
        failure {
            echo 'Failure'
            mail bcc: '', body: 'Status of pipeline :Failure', cc: '', from: '', replyTo: '', subject: 'Pipeline status', to: 'manojpraveenkgm@gmail.com'
        }

        }

}
