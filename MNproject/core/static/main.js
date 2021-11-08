
function main(){
    var method = document.getElementById("method");

    if(method == null){
        console.log("No encontro el ID 'method'");
        return;
    }

    method.addEventListener("change",funMethod);
    
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
}

main();