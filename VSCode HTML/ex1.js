console.log("1)This is ex1.js")
var myname = "Tal" 
var mylastname = "Cohen"
var birthyear = 2009
document.getElementById("student_message").innerHTML = "Hi, my name is " + myname + " " + mylastname + " " + "Im " + (2022 - birthyear).toString() + ' ' + "years old and Im learning Javascript"
function calculateaverage(num01,num02){
    num01 = Number(num01)
    num02 = Number(num02)
    var average = (num01+num02)/2
    

    return average.toFixed(2)
}
function setavg(){
    var num = document.getElementById("amount").value
    var num2 = document.getElementById("amount2").value
    var realaverage = calculateaverage(num,num2)
    document.getElementById("averagetext").innerHTML = realaverage
    alert("result is: " + realaverage)
}
var phone1 = "988866552";
var phone2 = "99087612366";
var phone3 = 876543123;
phone3 = phone3.toString()
if(phone1.length == 9){
    console.log("4)phone1:valid")
}else{
    console.log("4)phone1:invalid")
}
if(phone2.length == 9){
    console.log("phone2:valid")
}else{
    console.log("phone2:invalid")
}
if(phone3.length == 9){
    console.log("phone3:valid")
}else{
    console.log("phone3:invalid")
}
var result = Math.pow(32,6)
console.log("5)"+result)
console.log("6)typeof לא תקין כי הוא מילה שמורה בjavascript.\nfirst-name לא תקין כי יש בו קו אמצעי ואי אפשר לקרוא למשתנה ככה")
console.log("2ndAttempt לא תקין כי הוא מתחיל עם מספר\nfull name לא תקין כי יש רווח באמצע")
console.log("7)console.log( (7+5) / number + 2 );\n    console.log(typeof pressure); \nconsole.log(typeof temperature); ")
document.getElementById("url_2").innerHTML= "https://www.youtube.com"
document.getElementById("url_4").innerHTML= "www.google.com"