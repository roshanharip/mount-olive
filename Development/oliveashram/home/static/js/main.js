function myLabel() {
    if (document.getElementById("navbar").style.display == "block" ){
        document.getElementById("navbar").style.display = "none";
        documnet.getElementById("aboutus").style.display = "block";
    documnet.getElementById("content3").style.display = "block";
    }else{
    document.getElementById("navbar").style.display = "block";
    documnet.getElementById("aboutus").style.display = "none";
    documnet.getElementById("content3").style.display = "none";
    }
}
