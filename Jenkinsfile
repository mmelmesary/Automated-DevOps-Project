pipeline {
    agent any

    stages {
        stage('Build app image') {
            steps {
                script {
                    def dockerImage = 'flaskapi'
                    def dockerTag = 'v1.0'
                    def dockerRegistry = 'melmesary'

                    // Build Docker image
                    sh "docker build -t ${dockerRegistry}/${dockerImage}:${dockerTag} ./src"

                    // Check if build was successful
                    if (
                        sh(
                        returnStdout: true, 
                        script: "docker images ${dockerRegistry}/${dockerImage}:${dockerTag} | grep ${dockerTag}"
                        )
                       ){
                        echo "Docker image built successfully"
                        } 
                    else {
                        error "Docker image build failed"
                    }

                    // Push image to Docker Hub
                    withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                        sh  "echo $PASSWORD | docker login -u ${USERNAME} --password-stdin" //This approach is more secure because it does not display the password in plain text on the command line.
                        sh "docker push ${dockerRegistry}/${dockerImage}:${dockerTag}"
                    }
                }
            }
        }
        stage ('Build db image'){
            steps {
                script {
                    def dockerImage = 'mysqldb'
                    def dockerTag = 'v1.0'
                    def dockerRegistry = 'melmesary'

                    // Build Docker image
                    sh "docker build -t ${dockerRegistry}/${dockerImage}:${dockerTag} -f db.dockerfile ./src"

                    // Check if build was successful
                    if (
                        sh(
                        returnStdout: true, 
                        script: "docker images ${dockerRegistry}/${dockerImage}:${dockerTag} | grep ${dockerTag}"
                        )
                       ){
                        echo "Docker image built successfully"
                        } 
                    else {
                        error "Docker image build failed"
                    }

                    // Push image to Docker Hub
                    withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                        sh  "echo $PASSWORD | docker login -u ${USERNAME} --password-stdin" 
                        sh "docker push ${dockerRegistry}/${dockerImage}:${dockerTag}"
                    }
                }
               
            }
        }
    }
}