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
            def  FILES_LIST = sh (script: "ls | grep *.zip", returnStdout: true).trim()
            println file_name
            println FILES_LIST
        }
    }
    stage ("Docker Setup"){
        /*sh 'docker build -t img . '*/
        def pwd = pwd()
        def host_mount_path = pwd+ "/op/"
        println host_mount_path
        sh 'cd host_mount_path;ls'
        sh 'docker images'
    }
}
