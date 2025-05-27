pipeline {
    agent any

    environment {
        DB_HOST = credentials('localhost')
        DB_NAME = credentials('product_db')
        DB_USER = credentials('postgres')
        DB_PASSWORD = credentials('admin')
    }

    stages {
        stage('Instalar dependencias') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Ejecutar pipeline') {
            steps {
                bat 'python main.py'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '**/*.log', allowEmptyArchive: true
        }
    }
}