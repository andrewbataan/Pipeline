pipeline {
    agent any

    tools {
        python 'Python3'   // Usa el nombre que pusiste en Jenkins
    }

    environment {
        PATH = "${tool 'Python3'}\\Scripts;${tool 'Python3'};${env.PATH}"
    }

    stages {
        stage('Instalar dependencias') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Ejecutar pipeline') {
            steps {
                bat 'python tu_script.py'
            }
        }
    }
}