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
        stage('Copy code files') {
            steps {
                fileOperations([
                    folderCopyOperation(
                        sourceFolderPath: './taxi-code/taxi',
                        destinationFolderPath: './taxi'
                    ),
                    folderCopyOperation(
                        sourceFolderPath: './taxi-code/tests',
                        destinationFolderPath: './tests'
                    ),
                    fileCopyOperation(
                        includes: 'taxi-code/main.py',
                        targetLocation: '.'
                    )
                ])
                sh 'ls -lat'
            }
        }
    }
}