
import {mainInput,hola,crossList,removeAllChildNodes} from "./inputdata.js"; 
var method = document.getElementById("method");
var varContainer = document.getElementById("initialGuesses");
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
    let initVariables;
    if(varContainer == null){
        console.log("El contenedor con ID initialGuesses no se recupero");
        return;
    }
    if(valMethod == "bairstow"){
        //no necesitamos input vars!
        initVariables = 0;
        createInputVars(initVariables);
        console.log("bairstow Method!!");
        removeAllChildNodes(varContainer);
        
    }else if(valMethod == "muller"){
        initVariables = 3;

        createInputVars(initVariables); 

        getVariables(initVariables);       
        console.log("muller Method!!");
    }else if(valMethod == "newton"){
        initVariables = 2;
        createInputVars(initVariables);
        getVariables(initVariables); 
        console.log("newton Method!!");
    }else{
        console.log("NOTHING Method!!");
    }
    strMethod = valMethod;    
}
function createInputVars(numberVars){
    removeAllChildNodes(varContainer);
    const vars = numberVars;
    let cont = 0;
    while(cont != vars){
        let label = document.createElement("label");
        let inputVar = document.createElement("input");
        let box = document.createElement("div");
        //add attributes
        inputVar.type="text";
        inputVar.id ="var"+cont;
        label.textContent = "Variable "+(cont);
        label.appendChild(inputVar);
        box.appendChild(label);
        varContainer.appendChild(box);

        cont++;
    }

}
export function getVariables(initVariables){
    if(initVariables == 0){
        console.log("Bairstow Methos en getVariables() no se usa");
        return "&var=0";
    }
    const variables = initVariables;
    let items = [];
    let i=0;
    //recuperar 3 inputs
    while(i < variables){
        let myItem = document.getElementById("var"+i);
        if(myItem == null){
            console.log("Error, no se ecuentra el var con index",i,"en getVariables() archivp main.js");
            return;
        }
        let strVal = myItem.value;
        if(strVal==""){
            strVal = "0";
        }
        items.push(strVal);
        i++;
    }
    let str = "";
    console.log(items);
    i = 0;
    for(const myIt of items){
        str+="&var"+i+"="+myIt;
        i++;
    }
    console.log(str);
    return str;
}


main();



