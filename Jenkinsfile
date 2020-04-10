pipeline {
    agent {
        docker {
            image 'python:3.6'
        }
    }
    stages {
        stage('Checkout code') {
            steps {
                git branch: 'master',
                    credentialsId: 'github_cred_id',
                    url: 'ssh://git@github.com:sqrtqiezi/tdd-taxi-seed-py.git'
                sh "ls -lat"
            }
        }
    }
}