pipeline{
    agent any
    environment{
        staging_server="34.210.189.91"
    }
    stages{
        stage('Deploy to Remote'){
            steps{
                sh 'scp -r ${WORKSPACE}/* ec2-user@${staging_server}:/var/www/html/'
                 
            }
        }
    }
}
