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
            def file_name = "this is file name"
            println file_name
            sh 'echo ls | grep *.zip;'
            sh 'echo $file_name;'
        }
    }
}
