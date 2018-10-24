import groovy.json.JsonSlurperClassic
@NonCPS
def jsonParse(def json) {
    new groovy.json.JsonSlurperClassic().parseText(json)
}
node() {
    String  FILES_LIST
    def file_name = ""
    def run_config = ""
    def check_config = ""
    def pwd = pwd()
    stage ("Starting >>>") {
        //sh 'printenv'
        echo 'Pulling...' + env.BRANCH_NAME
        checkout scm
        check_config = readFile file: 'command.json'
        run_config = jsonParse(check_config)
        println run_config 
        println "variable direct."
        println run_config.Run_Config.Deploy_Lambda
        check_config = readFile file: 'service.yaml'
        properties([
             parameters([
            string(name: 'submodule', defaultValue: 'ashish'),
            string(name: 'submodule_branch', defaultValue: 'test'),
          ])
        ])
        println submodule
    /*    println check_config
        def lines = check_config.readLines()
        lines.each { String line ->
                println line
            if(line.contains('api_proxy')){
                println line
                def ashish = line.split(':')
                println ashish[0]
                                println ashish[1].trim()
                                                println ashish[1].trim().length()


            }
            } */

    
        if (run_config.Run_Config.Deploy_Lambda){
        echo "Executing Deploy Lambda"
        }
        if (run_config.Run_Config.Generate_RSDK) {
          echo "Executing RSDK "
        }
        def scmUrl = scm.getUserRemoteConfigs()[0].getUrl()
        println scmUrl
    }
    stage ("Setup >>>") {
        println "Love400"
        println submodule
        sh 'pwd;ls;'
        sh "echo sh submodule is ${params.submodule}"
    }
    stage ("getzip"){
        dir('op'){
            sh 'pwd;ls;'
          //  file_name = "this is file name"
            FILES_LIST = sh (script: "ls  *.zip", returnStdout: true).trim()
          //  println file_name
            println "AB"
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
      //      println artifact_name: FILES_LIST, artifact_local_path: pwd+"/"+FILES_LIST
        }

}
