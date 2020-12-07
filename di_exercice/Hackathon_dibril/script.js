
function openNav(){
    document.getElementById("sideNavigation").style.width = "250px";
    document.getElementById("main").style.marginLeft = "250px";
}
 
function closeNav() {
    document.getElementById("sideNavigation").style.width = "0";
    document.getElementById("main").style.marginLeft = "0";
}

function show_div(id){
    let divs = document.querySelectorAll("#main .culture")
    for(let d of divs){
        d.style.display=`none`;
    }
    let div = document.getElementsByClassName(id);
    div[0].style.display = `block`;

}