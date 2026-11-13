pipeline {
  agent any
  environment {
    WEBEX_TOKEN = credentials('OTYzNjk5MzMtMmI0OC00OGY1LWIzMTgtNmVjOTk5M2Y5NmFlYzVmNjM5YjItN2E1_P0A1_9f897fa5-c956-4265-b098-4452767a0486')
    WEBEX_ROOM  = credentials('Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vODRkMDdjOTAtZGYxMS0xMWYxLTg0NWMtYzVmZWI3M2ZhMzQw')
  }
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