pipeline {
    agent { 
        node {
            label 'Discordbot'
            }
      }
    triggers {
        pollSCM '* * * * *'
    }
    stages {
        stage('Build') {
            steps {
                echo "Bouwen.."
                sh '''
                cd /opt/Discordbot
                pip install -r requirements.txt
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing.."
                sh '''
                cd /opt/Discordbot
                python3 main.py
                '''
            }
        }
        stage('Deliver') {
            steps {
                echo 'Deliver....'
                sh '''
                echo "doing delivery stuff.."
                screen -S Discordbot
                python3 main.py
                '''
            }
        }
    }
}