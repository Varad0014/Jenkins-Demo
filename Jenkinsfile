pipeline { 
    agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/Varad0014/Jenkins-Demo.git'
            }
        }
        stage('Build Code') {
            steps {
                sh "chmod u+x Program.py"
                sh "./Program.py"
            }
        }
     stage('Test Code') {
            steps {
                sh "chmod u+x Test.py"
                sh "./Test.py"
            }
        }
    } 
}
