// import { removeAllChildNodes } from "../inputdata.js";
const URL_WEB = "http://127.0.0.1:8000/";
console.log("HELLOS WORLD!");

var method = document.getElementById("metodo");
var strMethod = method.value;
var orderMtrx = document.getElementById("orderMatrix");
var container = document.getElementById("contenedorMatrix");
var sendDataButton = document.getElementById("sendDataButton");
var utilMethod = document.getElementById("utilButton");
function main(){

    if(method == null |
         orderMtrx == null |
         container ==null ){
        // | sendDataButton == null
        console.log("Error en algun id { metodo, orderMatrix,contenedorMatrix }")
        return;
    }
    method.addEventListener("change",updateMethod);
    orderMtrx.addEventListener("change",createMatrix);
    //sendDataButton.addEventListener("click",sendData);
    utilMethod.addEventListener("click",sendData);
}

function removeAllChildNodes(parent) {
    while (parent.firstChild) {
        parent.removeChild(parent.firstChild);
    }
}

function updateMethod(){
    strMethod = this.value;
    console.log(strMethod);
}

function createMatrix(){
    let order = this.value*this.value;//3x3,2x2
    removeAllChildNodes(container);
    let cont = 0;
    while( cont != order){

        let minBox = document.createElement("div");
        let label = document.createElement("label");
        let input = document.createElement("input");
        //add attributes
        input.type = "number";
        input.maxLength=3;
        input.size = 3;
        input.id = "x"+cont;
        label.textContent = "x"+(cont+1);
        //concat
        label.appendChild(input);
        minBox.appendChild(label);
        container.appendChild(minBox);
        cont++;
    }
    
}
function getMatrix(order){
    console.log("Order : **",order);
    let matrix = [];
    let cont = 0;
    let row;
    let col;
    for(row = 0; row < order; row++){
        let genRow = [];
        for(col = 0; col < order; col++){
            let item = document.getElementById("x"+cont);
            let val;
            if(item == null){
                console.log("I dont found ID","x"+cont);
            }
            if(item.value == ""){
                val = "0";
            }else{
                val = item.value;
            }

            genRow.push(val);
            cont++;
        }
        matrix.push(genRow);
    }
    console.log("matriz: ",matrix);
    return toRequest(matrix,order)
}
function toRequest(matrix,order){
    let request = ""
    let count = 0;
    for(let i = 0; i < order; i++){
        for(let j = 0; j < order; j++){
            request += `&x${count}=${matrix[i][j]}`;
            count++;
        }
    }

    return request;    
}
function sendData(){
    let order = document.getElementById("orderMatrix").value;
    let requestMatrix = getMatrix(order);

    let request = URL_WEB+"resultLU/?method="+strMethod+requestMatrix+"&order="+order;
    //console.log(request);

    window.location.href = request;
}

main();