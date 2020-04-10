pipeline {
    agent {
        docker {
            image 'python:3.6'
        }
    }
    stages {
        stage('Checkout code') {
            steps {
                dir('taxi-code') {
                    git branch: 'master',
                        credentialsId: 'github_cred_id',
                        url: 'git@github.com:sqrtqiezi/tdd-taxi-seed-py.git'
                    sh 'ls -lat'
                }
            }
        }
        stage('Copy code file') {
            steps {
                fileOperations([fileCopyOperation(
                    excludes: '',
                    flattenFiles: true,
                    includes: '.\\taxi-code\\taxi\\*',
                    targetLocation: '.\\taxi'
                )])
                sh 'pwd'
                sh 'ls -lat'
            }
        }
    }
}