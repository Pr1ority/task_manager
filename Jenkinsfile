pipeline {

    agent any
    stages {
        stage('Initialize') {
            steps {
                script {
                    def dockerHome = tool 'myDocker'
                    env.PATH = "${dockerHome}/bin:${env.PATH}"
                }
            }
        }
        stage('Build') {
            steps {
                script {
                    sh 'docker pull python:3.10-slim'
                }
                docker.image('python:3.10-slim').inside {
                    sh 'pip install -r requirements.txt'
                    sh 'python manage.py collectstatic --noinput'
                }
            }
        }
        stage('Deploy'){
            steps {
                script {
                    sh 'docker compose down'
                    sh 'docker compose up -d --build'
                }
            }
        }
    }
}