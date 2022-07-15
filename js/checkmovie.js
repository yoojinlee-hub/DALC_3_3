//스와이퍼 click event //ERROR
function checkClick(){
    var color = ["#F3B743","#CFD8DC"]
    var x = document.getElementsByClassName('check1')
    
    if(x.style.backgroundColor === color[0]){
        x.style.backgroundColor = color[1];
    }
        
    else if(x.style.backgroundColor === color[1])
    {
        x.style.backgroundColor = color[0];
    }
        
}