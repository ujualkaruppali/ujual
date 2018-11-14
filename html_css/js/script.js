function Read(){
    var name= document.getElementById("getname").value;
    console.log(name);
    var roll= document.getElementById("roll").value;

    console.log(roll)
    var uk= document.getElementById("uk").value;
    console.log(uk)
    var age=document.getElementById("age").value;
    console.log(age)
    var op=document.getElementById("district");
    var dist=op.options[op.selectedIndex].value;
    console.log(dist);


    if(age>=18)
    {
        console.log("eligible");
    }
    else
    {
        console.log("noteligible");
    }
}
function addition()
{
    var num1=document.getElementById("one").value;
    var num2=document.getElementById("two").value;
    var op=operation.options[operation.selectedIndex].value;
    var x=parseInt(num1);
    var y=parseInt(num2);
  
    if(op=="addition");
    {num3=x+y;}
    else if(op=="subtraction");
    {num3=x-y;}
    else if(op==multiplication);
    {num3=x*y;}
    else(op=="division");
    {num3=x/y;}
    console.log(num3);
}



function compare()
{
    var num1=document.getElementById("opt1").value;
    var num2=document.getElementById('opt2').value;
    var num3=document.getElementById("opt3").value;
    var x=parseInt(num1);
    var y=parseInt(num2);
    var z=parseInt(num3);

    if(x>y)
    {
        if(x>z)
        {
            console.log(x)
        
        }
        else 
        {
            console.log(z)
        }


    }
    else
    {
     console.log(y)
    }

    
}