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
        stage('Style Check') {
            steps {
                echo 'Checking'
                sh 'python -m pylint taxi'
            }
        }
        stage('Test') {
            steps {
                echo 'testing'
                sh 'python -m pytest --cov-branch --cov=taxi tests/ --cov-report xml:coverage.xml'
            }
        }
        stage('Run') {
            steps {
                sh 'python main.py --test-data=./resource/testData.txt > temp'
                script {
                    String diff = sh(returnStdout: true, script: "diff temp resource/answer.txt")
                    if (diff != "") {
                        echo diff
                        error("The answer is incorrect!")
                    }
                }
            }
        }
    }
}