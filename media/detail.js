let mainImage = document.getElementById.('mainImage');
let secondaryImage = [];

for (let i=0; i<3 ; i++){
    let tempi = 'image-';
    tempi += i.toString();
    secondaryImage.push(document.getElementById(tempi));
}

console.log(secondaryImage);