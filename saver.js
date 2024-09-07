let images = [];
let current=0;

const selected=[];

fetch('image_paths.json').then(response=>response.json())
.then(data=>{images=data; loadImage();})
.catch(error=>console.error('Error with paths'));

function loadImage(){
    const box=document.getElementById('image-holder');

    if(current <images.length){
        const img=document.createElement('img');
        img.src=images[current];
        box.appendChild(img)
    }
}