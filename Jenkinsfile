pipeline {
    agent any
   stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
                bat """
                    echo "something" > file.txt
                    """
                bat 'call git add file.txt'
                bat 'call git commit -am "Added new text file"'
                bat 'call git push origin main'
            }
        }
    }
}
