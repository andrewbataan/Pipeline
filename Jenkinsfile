pipeline {
    agent any

    environment {
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
                bat 'process_data.py'
            }
        }
    }

    post {
        always {
            // Ejecutar archiveArtifacts dentro de un nodo
            script {
                node {
                    archiveArtifacts artifacts: '**/*.log', allowEmptyArchive: true
                }
            }
        }
    }
}