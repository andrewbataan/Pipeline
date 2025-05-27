pipeline {
    agent any

    environment {
        // Ruta explícita al ejecutable de Python (ajustada a tu sistema)
        PYTHON_PATH = "C:\\Users\\rolan\\AppData\\Local\\Programs\\Python\\Python312"
        PATH = "${env.PYTHON_PATH};${env.PYTHON_PATH}\\Scripts;${env.PATH}" // Windows
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
}