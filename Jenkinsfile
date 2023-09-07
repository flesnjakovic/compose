def dockerFilesToBuild

pipeline {
    agent any
    
    environment {
        PATH = "/usr/local/bin:${env.PATH}"
        DOCKER_HOST = "unix:///var/run/docker.sock"
    }

    stages {
        stage('Checkout repository') {
            steps {
                git branch: 'main', url: 'https://github.com/flesnjakovic/compose.git'
            }
        }

        stage('Unit test services') {
            steps {
                script {
                    sh "echo 'Running tests'"
                }
            }
        }

        stage('Build services') {
            steps {
                script {
                    dockerFilesToBuild = sh(returnStdout: true, script: "find . -name Dockerfile").trim().split('\n')
                    println dockerFilesToBuild
                    println dockerFilesToBuild.toString()
                    dockerFilesToBuild.each {
                        service = it.split('/')[1]
                        version = sh(returnStdout: true, script: "cat $service/version.py").trim()
                        docker.build(service, "-f $it ./$service -t flesnjakovic/$service:$version")
                    }
                }
            }
        }

        stage('Run E2E tests') {
            steps {
                script {
                    sh "echo 'Running E2E tests'"
                }
            }
        }

        stage('Push Images') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'docker-credentials', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        docker.withRegistry('', 'docker-credentials') {
                            dockerFilesToBuild.each {
                                service = it.split('/')[1]
                                version = sh(returnStdout: true, script: "cat $service/version.py").trim()
                                docker.image("flesnjakovic/$service:$version").push()
                            }
                        }
                    }
                }
            }
        }
    }
}