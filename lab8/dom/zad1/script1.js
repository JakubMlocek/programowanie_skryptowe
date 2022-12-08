//window.prompt("Tekst1","Tekst2");
function printForm(){
    var inp  = document.forms[0].elements;
    console.log(inp[0].value);
    console.log(typeof(inp[0].value));
    console.log(inp[1].value);
    console.log(typeof(inp[1].value));
    window.alert(inp[0].value + ", " + inp[1].value);
    document.write(inp[0].value + ", " + inp[1].value);
}

function onLoader(){
    console.log('Tekst 1');
}
