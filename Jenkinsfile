pipeline {
    agent any

    environment {
        // Variables de entorno si las necesitas
        PYTHONUNBUFFERED = "1"
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/tuusuario/tu-proyecto.git'
            }
        }

        stage('Run ETL pipeline') {
            steps {
                sh './run.sh'
            }
        }
    }
}