// console.log("This is Working");
// alert("THIS is working");
// var x="hello";
// alert(x);
// alert(x);
// var x;
// for(x=0; x<=5;x++){
//     console.log(x)
// }
function validateform(){
    x=document.forms["myform"]["username2"].value;
    if(x==""){
        document.getElementById('username2').placeholder="Enter your email";
        document.getElementById('username2').style.border   ="2px solid red";
        x=document.getElementById("valid")
        x.innerHTML="*Enter your email*"
        x.style.color="red"
        return false;
    }
}