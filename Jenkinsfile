pipeline {
    agent any

    environment {
        PYTHON_PATH = "C:\\Users\\rolan\\AppData\\Local\\Programs\\Python\\Python312"
        PATH = "${env.PYTHON_PATH};${env.PYTHON_PATH}\\Scripts;${env.PATH}"
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
                withCredentials([usernamePassword(credentialsId: 'credenciales', usernameVariable: 'DB_USER', passwordVariable: 'DB_PASSWORD')]) {
                    bat """
                        set DB_CREDENTIALS_USR=%DB_USER%
                        set DB_CREDENTIALS_PSW=%DB_PASSWORD%
                        python main.py
                    """
                }
            }
        }

        stage('Guardar logs') {
            steps {
                archiveArtifacts artifacts: 'logs/pipeline.log', onlyIfSuccessful: true
            }
        }
    }
}