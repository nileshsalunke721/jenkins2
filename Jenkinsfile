pipeline {
    agent any
    
    environment {
        PYTHON = "\\Users\\Lenovo\\AppData\\Local\\Programs\\Python\\Python314\\python.exe"
        VENV = "jen-project"
        api_key = credentials("api_key")
    }
    
    stages {
        stage("checkout code") {
            steps {
                git url: "https://github.com/nileshsalunke721/jenkins2.git", branch: "main"
            }
        }
        
        stage("install dependencies") {
            steps {
                bat """
                %PYTHON% -m venv %VENV%
                %VENV%\\Scripts\\python.exe -m pip install -r requirements.txt
                """
            }
        }
        
        stage("extract data") {
            steps {
                bat """
                SET API_KEY = %api_key%
                %VENV%\\Scripts\\python.exe extract.py
                """
            }
        }
        
        stage("cleanup") {
            steps {
                bat """
                rmdir /s /q %VENV%
                """
            }
        }
    }
}