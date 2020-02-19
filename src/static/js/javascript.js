
var list = [
    uno = 0,
    dos = 0,
    tres = 0,
    cuatro = 0,
    cinco = 0,
    seis = 0,
    siete = 0,
    ocho = 0,
    nueve = 0,
    diez = 0];

// ---------------------------------------- FUNCION -------------------------------------------------       
function plastico(){
    
    if(list[0] == 0){
        document.getElementById('plastico').style.backgroundColor = "rgb(255, 224, 45)";
        list[0] = 1;}

        else{document.getElementById('plastico').style.backgroundColor = "rgba(255, 223, 45, 0.349)";
        list[0]--;}}

// ---------------------------------------- FUNCION -------------------------------------------------        
function papel(){
    if(list[1] == 0){document.getElementById('papel').style.background = "rgb(30, 208, 252)";
        list[1] = 1;}

    else{document.getElementById('papel').style.background = "rgba(30, 208, 252, 0.349)";
        list[1]--;}}

// ---------------------------------------- FUNCION -------------------------------------------------
function cristal(){
    if(list[2] == 0){document.getElementById('cristal').style.background = "rgb(22, 211, 5)";
        list[2] = 1;}

    else{document.getElementById('cristal').style.background = "rgba(30, 252, 60, 0.349)";
        list[2]--;}}

// ---------------------------------------- FUNCION -------------------------------------------------
function organico(){
    if(list[3] == 0){document.getElementById('organico').style.background = "rgb(252, 137, 30)";
        list[3] = 1;}

    else{document.getElementById('organico').style.background = "rgba(252, 137, 30, 0.349)";
        list[3]--;}}

// ---------------------------------------- FUNCION -------------------------------------------------
function general(){
    if(list[4] == 0){document.getElementById('general').style.background = "rgb(189, 30, 252)";
        list[4] = 1;}

    else{document.getElementById('general').style.background = "rgba(189, 30, 252, 0.349)";
        list[4]--;}}

// ---------------------------------------- FUNCION -------------------------------------------------
function muebles(){
    if(list[5] == 0){document.getElementById('muebles').style.background = "rgb(252, 30, 115)";

    list[5] = 1;}

    else{document.getElementById('muebles').style.background = "rgba(252, 30, 115, 0.349)";
        list[5]--;}}



function lunes(){
    
    if(list[0] == 0){
        document.getElementById('lunes').style.position = "relative";
        document.getElementById('lunes').style.position = "absolute";
        list[0] = 1;}
        
        else{document.getElementById('plastico').style.backgroundColor = "rgba(255, 223, 45, 0.349)";
        list[0]--;}}
        