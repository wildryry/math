
function helloWorld() {
    
    console.log("hello world")
    const button = document.getElementById("pageButton")
    const para = document.getElementById("output")
    const para2 = document.getElementById("output2")
    const para3 = document.getElementById("output3")
    //button.setAttribute("value","your a gay")
    
    if (para2.innerHTML == "////////////////////////////////////////////////////////////////////////////////////////////////////") {
        para2.innerHTML = ""
        
        para3.innerHTML = para.innerHTML
        
        para.innerHTML = "0"

    }
    
    for (i=0; i < 1; i++) {
        para.innerHTML = Math.round(Math.random() * 10) + parseInt(para.innerHTML)
        para2.innerHTML += "/"
    }
    
    
   

}
function reset() {
    const para = document.getElementById("output")
    const para2 = document.getElementById("output2")
    para.innerHTML ="1"
    para2.innerHTML =""
}