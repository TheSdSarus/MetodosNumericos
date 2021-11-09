
import {mainInput,hola,crossList} from "./inputdata.js"; 
var method = document.getElementById("method");
export var strMethod = "";
function main(){

    if(method == null){
        console.log("No encontro el ID 'method'");
        return;
    }
    method.addEventListener("change",funMethod); 
    // console.log(hola); 

    mainInput();   
}
function funMethod(){
    let valMethod = this.value;
    if(valMethod == "bairstow"){
        console.log("bairstow Method!!");
    }else if(valMethod == "muller"){
        console.log("muller Method!!");
    }else if(valMethod == "newton"){
        console.log("newton Method!!");
    }else{
        console.log("NOTHING Method!!");
    }
    strMethod = valMethod;    
}

main();



