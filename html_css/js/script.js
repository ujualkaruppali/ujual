function read(){
    var name= document.getElementById("getname").value;
    console.log(name);
    var roll= document.getElementById("roll").value;

    console.log(roll)
    var uk= document.getElementById("uk").value;
    console.log(uk)
    var age=document.getElementById("age").value;
    console.log(age)

    if(age>=18)
    {
        console.log("eligible");}
    else
    {console.log("noteligible");}
}