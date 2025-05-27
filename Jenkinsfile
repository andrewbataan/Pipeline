pipeline {
    agent any

    environment {
        PYTHON_PATH = "C:\\Users\\rolan\\AppData\\Local\\Programs\\Python\\Python312"
        PATH = "${env.PYTHON_PATH};${env.PYTHON_PATH}\\Scripts;${env.PATH}"
        // Usa las credenciales configuradas en Jenkins
        DB_CREDENTIALS_USR = credentials('DB_CREDENTIALS').username
        DB_CREDENTIALS_PSW = credentials('DB_CREDENTIALS').password
    }

    stages {
        stage('Instalar dependencias') {
            steps {
                bat 'python -m pip install --upgrade pip setuptools wheel'
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Ejecutar pipeline') {
            steps {
                bat 'python main.py'
            }
        }
    }
}