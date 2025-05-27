pipeline {
    agent any

    environment {
        PYTHONUNBUFFERED = "1"
    }

    stages {

        stage('Instalar dependencias') {
            steps {
                sh 'python -m venv venv'
                sh '. venv/Scripts/activate && pip install -r requirements.txt'
            }
        }

        stage('Ejecutar pipeline') {
            steps {
                sh '. venv/Scripts/activate && bash run.sh'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'logs/pipeline.log', fingerprint: true
        }
    }
}