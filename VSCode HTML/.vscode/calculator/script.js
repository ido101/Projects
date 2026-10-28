// This function clear all the values
function clearScreen() {
    document.getElementById("result").value = "";
}


// This function display values
function display(value) {
    document.getElementById("result").value += value;
}

// This function evaluat  es the expression and return result
function calculate() {
    var p = document.getElementById("result").value;
    var q = eval(p);
    document.getElementById("result").value = q;
}