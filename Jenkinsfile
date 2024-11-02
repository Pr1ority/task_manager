pipeline {

    agent none
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:3.10-slim'
                    args '-u root'
                }
            }
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Deploy'){
            agent any
            steps {
                script {
                    sh 'docker compose down'
                    sh 'docker compose up -d --build'
                }
            }
        }
    }
}