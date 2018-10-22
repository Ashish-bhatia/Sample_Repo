import groovy.json.JsonSlurperClassic
@NonCPS
def jsonParse(def json) {
    new groovy.json.JsonSlurperClassic().parseText(json)
}
node() {
    String  FILES_LIST
    def file_name = ""
    def run_config = ""
    def pwd = pwd()
    stage ("Starting >>>") {
        sh 'printenv'
        echo 'Pulling...' + env.BRANCH_NAME
        checkout scm
        run_config = jsonParse(readFile file: 'command.json')
        println run_config
        if (run_config.Run_Config.Deploy_Lambda == true){
        echo "Executing Deploy Lambda"
        } else if (run_config.Run_Config.Deploy_Lambda == true) {
          echo "Executing RSDK "
        }
        def scmUrl = scm.getUserRemoteConfigs()[0].getUrl()
        println scmUrl
    }
    stage ("Setup >>>") {
        sh 'pwd;ls;'
        sh 'echo $REPONAME $USERS $ADMINID'
    }
    stage ("getzip"){
        dir('op'){
            sh 'pwd;ls;'
            file_name = "this is file name"
            FILES_LIST = sh (script: "ls | grep *.zip", returnStdout: true).trim()
            println file_name
            println FILES_LIST
        }
    }
    stage ("Docker Setup"){
        /*sh 'docker build -t img . '*/
        println FILES_LIST
        println file_name
        sh 'cd $PWD/op/;ls'
        sh 'docker run  -v $PWD/op/:/opt/app-root/src/app/op img:latest'
    }
    stage("Publish deployable image")
        {
            println FILES_LIST
            println artifact_name: FILES_LIST, artifact_local_path: pwd+"/"+FILES_LIST
        }

}
