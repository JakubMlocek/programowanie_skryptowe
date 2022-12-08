"use strict";

function isNumber(char) {
    if (typeof char !== 'string') {
      return false;
    }
    if (char.trim() === '') {
      return false;
    }
    return !isNaN(char);
  }

function cyfry(napis){
    var sum = 0;
    for(var i = 0; i < napis.length; i++){
        if(isNumber(napis[i])){
            sum += parseInt(napis[i],10);
        }
    }
    return sum;
}

function litery(napis){
    var counter = 0;
    for(var i = 0; i < napis.length; i++){
        if(!isNumber(napis[i])){
            counter += 1;
        }
    }
    return counter;
}

function suma(napis){
    if(isNumber(napis[0])){
        gsum += cyfry(napis);
    }
    return gsum;
}

var napis = "";
var gsum = 0;
while(1){
    napis = window.prompt("Podaj dane","");
    if(napis == null){
        break;
    }
    var result = String(cyfry(napis));
    result += "\t";
    result += String(litery(napis));
    result += "\t";
    result += String(suma(napis));
    window.alert(result);
}

