
var method = document.getElementById("method");
var objNumber = document.getElementById("inputRows");
var sendButton = document.getElementById("sendButton");
var selectMethod;
const URL_WEB = "http://127.0.0.1:8000/";
function main(){
    if(objNumber == null|sendButton==null|method == null){
        console.error("No hay el tag con ID: inputRows or ID:sendButton, ID:method");
        return;
    }    
    method.addEventListener("change",updateVal);
    objNumber.addEventListener("change",makeInputs);
    sendButton.addEventListener("click",sendData);
}
function updateVal(){
    selectMethod = this.value;
    console.log("METODO; ",selectMethod);
}
function makeInputs(){
    let val = this.value;    
    // console.log("Valor");
    //PARA LAS X
    let inputX = document.getElementById("inputsX");
    removeAllChildNodes(inputX);
    for(let i = 0; i < parseInt(val); i++){
        let label = document.createElement("label");
        let inputNumber = document.createElement("input");
        let box = document.createElement("div");
        inputNumber.type="number";
        inputNumber.id = "x"+i;
        label.textContent = "Ingrese X"+i+": ";
        box.appendChild(label);
        label.append(inputNumber);
        inputX.append(box);
    }
    //PARA LAS Y
    let inputY = document.getElementById("inputsY");
    removeAllChildNodes(inputY);
    for(let i = 0; i < parseInt(val); i++){
        let label = document.createElement("label");
        let inputNumber = document.createElement("input");
        let box = document.createElement("div");
        inputNumber.type="number";
        inputNumber.id = "y"+i;
        label.textContent = "Ingrese Y"+i+": ";
        box.appendChild(label);
        label.append(inputNumber);
        inputY.append(box);
    }
}
function removeAllChildNodes(parent) {
    while (parent.firstChild) {
        parent.removeChild(parent.firstChild);
    }
}
function sendData(){
    //RETRIEVE ALL DATA!!!
    //la cantidad
    let items =parseInt(objNumber.value);
    //los X items
    let arrX = [];
    for(let i = 0; i < items; i++){
        let key = "x"+i;
        let item = document.getElementById(key);
        if(item ==  null){
            console.log("El ID ",key,"No existe");
            break;
        }
        let val = parseInt(item.value);
        if(isNaN(val)){
            val = 0;
        }
        arrX.push(val);
    }
    // console.log(arrX);
    //los Y items
    let arrY = [];
    for(let i = 0; i < items; i++){
        let key = "y"+i;
        let item = document.getElementById(key);
        if(item ==  null){
            console.log("El ID ",key,"No existe");
            break;
        }
        let val = parseInt(item.value);
        if(isNaN(val)){
            val = 0;
        }
        arrY.push(val);
    }
    // console.log(arrY);
    sendData_request(arrX,arrY);
    //SENDDATA
}
function sendData_request(arrX,arrY){
    let selectedmethod = method.value;
    let request = URL_WEB+"inputMSquare/?";
    let items =parseInt(objNumber.value);
    if(isNaN(items)){
        console.log(selectedmethod);
        return;
    }
    for(let i = 0; i < items; i++){
        request +="&x"+i+"="+arrX[i];
        request +="&y"+i+"="+arrY[i];
    }
    request += "&cant="+items;
    request+="&method="+selectedmethod;
    window.location.href = request;
}

main();