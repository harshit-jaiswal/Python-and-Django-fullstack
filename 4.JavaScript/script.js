function hello()
{
    console.log("Hello World");
}
function sum(x,y)
{
    console.log(x+y);
}
function printName(name="harshit")
{
    console.log(`This is ${name}`);
}
function printMultiTable(x=1)
{
    var i;
    for(i=1;i<11;i++)
    console.log(x*i);
}

function printArry()
{
    var arr =[1,2,3,4];
    arr.forEach(console.log);//for each loop
    arr.pop();
    for(element of arr)//for of loop
    console.log(element);
}