import groovy.json.JsonSlurperClassic
@NonCPS
def jsonParse(def json) {
    new groovy.json.JsonSlurperClassic().parseText(json)
}
node() {
    stage ("Starting >>>") {
        sh 'printenv'
        echo 'Pulling...' + env.BRANCH_NAME
        checkout scm
    }
    stage ("Setup >>>") {
        sh 'pwd;ls;'
        sh 'echo $REPONAME $USERS $ADMINID'
    }
    stage ("getzip"){
        dir('op'){
            sh 'pwd;ls;'
            sh 'export FILE_NAME = echo (ls | grep *.zip);'
            sh 'echo $FILE_NAME;'
        }
    }
}
