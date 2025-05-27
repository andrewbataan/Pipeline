pipeline {
    agent any

    environment {
        DB_CREDENTIALS = credentials('POSTGRES_CREDENTIALS_ID') /
    }

    stages {
        stage('Instalar dependencias') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Ejecutar pipeline') {
            steps {
                bat 'python main.py' // Asegúrate de que el script se llama main.py (no process_data.py)
            }
        }
    }

    post {
        always {
            script {
                node {
                    archiveArtifacts artifacts: '**/*.log', allowEmptyArchive: true
                }
            }
        }
    }
}