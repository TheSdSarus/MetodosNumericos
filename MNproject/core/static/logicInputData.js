console.log("HELLOS OWRLD");

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
        let input = document.createElement("input");
        input.type="text";
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
main();