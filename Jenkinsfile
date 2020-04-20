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
        stage('Checkout Code') {
            steps {
                echo "${BRANCH}"
                dir('taxi-code') {
                    git branch: "${BRANCH}",
                        credentialsId: "${CREDENTIALS_ID}",
                        url: "${REPO_URL}"
                    sh 'ls -lat'
                }
            }
        }
        stage('Copy code files') {
            steps {
                sh "cp -avr ./taxi-code/taxi ./taxi"
                sh "cp -avr ./taxi-code/tests ./tests"
                sh "cp -v ./taxi-code/main.py ./"
                sh 'ls -lat'
            }
        }
        stage('Install Requirements') {
            steps {
                sh 'pip install -i https://pypi.doubanio.com/simple/ -r ./requirements.txt'
            }
        }
        stage('Check Code Style') {
            steps {
                sh 'python -m pylint taxi'
            }
        }
        stage('Run Test') {
            steps {
                sh "python -m pytest --cov-branch \
                        --cov=taxi tests/ \
                        --cov-report xml:coverage.xml \
                        --cov-report html:coverage_html \
                        --cov-fail-under=100"
            }
        }
        stage('Check Answer') {
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
    post {
        always {
            deleteDir()
        }
    }
}