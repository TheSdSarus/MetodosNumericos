

//code logic for html Input Data



var container = document.getElementById("inputBoxes");
var select = document.getElementById("coeficientes");
function main(){

    if(select == null){
        console.log("No existe elemento!");
        return;
    } 
    
    if(container == null){
        console.log("No existe el ID inputBoxes");
        return;
    }

    
    select.addEventListener("change",eventFunction);

}
function eventFunction(){
    removeAllChildNodes(container);  
    let value = this.options[this.selectedIndex].value;
    //crear item
    let intValue = parseInt(value);
    createItems(intValue);

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
function removeAllChildNodes(parent) {
    while (parent.firstChild) {
        parent.removeChild(parent.firstChild);
    }
}

function accion() {
    let value = document.getElementById("coeficientes").value;
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

    window.location.href = "http://127.0.0.1:8000/passData/?can=" + value+ "&x0="+x0+"&x1="+x1+"&x2="+x2+"&x3="+x3+"&x4="+x4+"&x5="+x5+"&x6="+x6+"&x7="+x7+"&x8="+x8+"&x9="+x9+"";
}
main();