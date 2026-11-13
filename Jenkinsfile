pipeline {
  agent any
  stages {
    stage('Environment') {
      steps { sh 'python3 --version' }
    }
    stage('Unit tests') {
      steps { sh 'python3 -m unittest discover -v' }
    }
  }
  post {
    always {
      withCredentials([
        string(credentialsId: 'webex-bot-token', variable: 'WEBEX_TOKEN'),
        string(credentialsId: 'webex-room-id', variable: 'WEBEX_ROOM')
      ]) {
        withEnv(["RESULT=${currentBuild.currentResult}"]) {
          // single quotes: the shell, not Groovy, expands the secrets
          sh '''
            python3 -c 'import json, os; print(json.dumps({
              "roomId": os.environ["WEBEX_ROOM"],
              "markdown": "**" + os.environ["JOB_NAME"] + " #" + os.environ["BUILD_NUMBER"] + ": " + os.environ["RESULT"] + "**  \\nCommit " + os.environ.get("GIT_COMMIT", "?")[:7] + " · " + os.environ.get("BUILD_URL", "")}))' > webex.json
            curl -sS -o /dev/null -w "Webex API: HTTP %{http_code}\\n" \
              -X POST https://webexapis.com/v1/messages \
              -H "Authorization: Bearer $WEBEX_TOKEN" \
              -H "Content-Type: application/json" \
              -d @webex.json
          '''
        }
      }
    }
  }
}