pipeline {
    agent any

    tools {
        Python 'Python3'  // ¡"Python" con P mayúscula!
    }

    environment {
        // Ajusta la variable PATH según el SO del agente:
        PATH = "${tool 'Python3'};${tool 'Python3'}\\Scripts;${env.PATH}"  // Windows
    }

    stages {
        stage('Instalar dependencias') {
            steps {
                bat 'pip install -r requirements.txt'  // Usa "sh" para Linux/Mac, "bat" para Windows
            }
        }

        stage('Ejecutar pipeline') {
            steps {
                bat 'python main.py'  // Usa "sh" para Linux/Mac, "bat" para Windows
            }
        }
    }
}