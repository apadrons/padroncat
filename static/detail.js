var mainImage = document.getElementById('mainImage');
var secondaryImages = [];

for (let i=1; i<=3 ; i++){
    let tempi = 'image-';
    tempi += i.toString();
    secondaryImages.push(document.getElementById(tempi));
    secondaryImages[i-1].onclick = function(){
        imageSwap(secondaryImages[i-1],mainImage);
    }
}




function imageSwap (secondaryImage,mainImage){
    var tempSel = secondaryImage.src;
    var tempMain = mainImage.src;

    mainImage.src = tempSel;
    secondaryImage.src = tempMain;


}