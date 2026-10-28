//makes a pop up massage
alert("this is a pop up massage")
//prints a massage in inspect<console
console.log("this massage will only be shown in the console")



console.log(document.getElementById("blue_box").innerHTML)
document.getElementById("blue_box").innerHTML = "<h1>Javascript</h1>"
console.log(document.getElementById("blue_box").innerHTML)

function sum_args(x,y){
    var sum = x + y;
    console.log(sum);
}

sum_args(10,15);

var student = {
    'name':'ido cohen',
    'age':13,
    'grade':'7th',
};
student.grade = '8th';
student.phonenumber = '666'
var teacher = {
    'name':'tamar glazner',
    'age':40,
    'school':'yachad'
}
teacher.age = 41
teacher.kids = 2