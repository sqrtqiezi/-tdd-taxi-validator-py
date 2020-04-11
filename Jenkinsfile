pipeline {
    agent {
        docker {
            image 'python:3.6'
        }
    }
    parameters {
        string(name: 'BRANCH', defaultValue: 'master', description: 'work branch')
        string(name: 'REPO_URL', description: 'git repo url')
        string(name: 'CREDENTIALS_ID', description: 'credentials for fetch git repo')
    }
    stages {
        stage('Checkout code') {
            steps {
                dir('taxi-code') {
                    git branch: '${BRANCH}',
                        credentialsId: '${CREDENTIALS_ID}',
                        url: '${REPO_URL}'
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
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'pip install -i https://pypi.doubanio.com/simple/ -r ./requirements.txt'
            }
        }
    }
}