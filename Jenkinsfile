pipeline {
    agent any

    environment {
        PYTHONUNBUFFERED = "1"
    }

    stages {
        stage('Clonar repositorio') {
            steps {
                git 'https://github.com/andrewbataan/Pipeline.git'
            }
        }

        stage('Instalar dependencias') {
            steps {
                sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Ejecutar pipeline') {
            steps {
                sh './run.sh'
            }
        }
    }
}