

//code logic for html Input Data
import {strMethod,getVariables} from "./main.js";

export const URL_WEB = "http://127.0.0.1:8000/";
export var hola = "AAAAAAA";
var value = 10;
var container = document.getElementById("inputBoxes");
var select = document.getElementById("coeficientes");
var sendButton = document.getElementById("sendButton");
export var crossList = [];
export function mainInput(){
    if(select == null){
        console.log("No existe elemento!");
        return;
    } 
    if(container == null){
        console.log("No existe el ID inputBoxes");
        return;
    }
    if(sendButton == null){
        console.log("No existe el ID sendButton");
        return;
    }
    select.addEventListener("change",eventFunction);
    sendButton.addEventListener("click",getData);
}

function eventFunction(){
    removeAllChildNodes(container);  
    let value = this.options[this.selectedIndex].value;
    //crear item
    let intValue = parseInt(value);
    createItems(intValue);

}
export function getData(){
    let list = accion();
    let filterList = [];
    for(const x of list){
        let val = x;
        if(isNaN(x)){
            val = 0;
        }
        filterList.push(val);
    }
    // return filterList;
    console.log("Lista Filtrada: ");
    console.log(filterList);
    crossList = filterList;
    sendData();
}
function sendData(){
    let cantVars =document.getElementById("coeficientes").value;
    let strMethodValue = document.getElementById("method").value;
    console.log(cantVars);
    //console.log(sendData);
    let variables=0;
    if(strMethodValue == "bairstow"){
        variables = 0;
    }else if(strMethodValue == "muller"){
        variables = 3;
    }else if(strMethodValue=="newton"){
        variables = 2;
    }else{
        variables = -1;
        console.log("Error, no tenemos el metodo conocido=",strMethod);
        return;
    }

    let sendVars = getVariables(variables);
    //console.log("sendvars:",sendVars);

    window.location.href = URL_WEB+"inputData/?method=" + strMethod+ 
    "&x0="+crossList[0]+
    "&x1="+crossList[1]+
    "&x2="+crossList[2]+
    "&x3="+crossList[3]+
    "&x4="+crossList[4]+
    "&x5="+crossList[5]+
    "&x6="+crossList[6]+
    "&x7="+crossList[7]+
    "&x8="+crossList[8]+
    "&x9="+crossList[9]+
    sendVars+"&cant="+cantVars+"";    

    print(crossList[9])
}


function createItems(value){
    let cont = 0;
    while(value != cont){            
        let label = document.createElement("label");
        label.textContent = "X"+(cont);
        //label.id = cont; //ADEDD
        let input = document.createElement("input");
        input.type="text";
        input.id = "x"+cont;

        let box = document.createElement("div");
        label.appendChild(input);
        box.appendChild(label);
        container.appendChild(box);

        cont++;
    } 
}
export function removeAllChildNodes(parent) {
    while (parent.firstChild) {
        parent.removeChild(parent.firstChild);
    }
}

function accion() {
    value = document.getElementById("coeficientes").value;//3
    let x0,x1,x2,x3,x4,x5,x6,x7,x8,x9;
    for(let i = 0; i < value; i++) {
        if(i==0){
            x0 = parseInt(document.getElementById("x"+i).value);
        }else if (i == 1) {
            x1 = parseInt(document.getElementById("x"+i).value);
        }else if(i==2) {
            x2 = parseInt(document.getElementById("x"+i).value);
        }else if(i==3) {
            x3 = parseInt(document.getElementById("x"+i).value);
        }else if(i==4) {
            x4 = parseInt(document.getElementById("x"+i).value);
        }else if(i==5) {
            x5 = parseInt(document.getElementById("x"+i).value);
        }else if(i==6) {
            x6 = parseInt(document.getElementById("x"+i).value);
        }else if(i==7) {
            x7 = parseInt(document.getElementById("x"+i).value);
        }else if(i==8) {
            x8 = parseInt(document.getElementById("x"+i).value);
        }else if(i==9) {
            x9 = parseInt(document.getElementById("x"+i).value);
        }
    }

    for(let i = value; i < 10; i++) {
        if(i==0){
            x0 = 0;
        }else if (i == 1) {
            x1 = 0;
        }else if(i==2) {
            x2 = 0;
        }else if(i==3) {
            x3 = 0;
        }else if(i==4) {
            x4 = 0;
        }else if(i==5) {
            x5 = 0;
        }else if(i==6) {
            x6 = 0;
        }else if(i==7) {
            x7 = 0;
        }else if(i==8) {
            x8 = 0;
        }else if(i==9) {
            x9 = 0;
        }
    }
    return [x0,x1,x2,x3,x4,x5,x6,x7,x8,x9];

    //window.location.href = URL_WEB+"passData/?can=" + value+ "&x0="+x0+"&x1="+x1+"&x2="+x2+"&x3="+x3+"&x4="+x4+"&x5="+x5+"&x6="+x6+"&x7="+x7+"&x8="+x8+"&x9="+x9+"";
}

// mainInput();