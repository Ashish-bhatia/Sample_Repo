import groovy.json.JsonSlurperClassic
@NonCPS
def jsonParse(def json) {
    new groovy.json.JsonSlurperClassic().parseText(json)
}
node() {
    environment {
        CREDENTIALS = ''
        DEPLOY_ENV = ''
    }
    stage ("Starting >>>") {
        checkout scm
      }
    stage ("Setup >>>") {

    }
}
