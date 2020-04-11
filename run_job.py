import jenkins
JENKINS_SERVER = ''
JENKINS_USER = ''
JENKINS_PWD = ''

JOB_NAME = 'tdd-taxi-validator-py/master'
REPO_URL = 'git@github.com:sqrtqiezi/tdd-taxi-seed-py.git'
CREDENTIALS_ID = 'github_cred_id'

if __name__ == '__main__':
    server = jenkins.Jenkins(JENKINS_SERVER,
                             username=JENKINS_USER,
                             password=JENKINS_PWD)

    server.build_job(JOB_NAME, {
        'REPO_URL': REPO_URL,
        'CREDENTIALS_ID': CREDENTIALS_ID
    })
