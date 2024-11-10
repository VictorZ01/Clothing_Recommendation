
let images = [];
let current=0;

const selected=[];
const ar = [];
fetch('image_paths.json')
.then(response=>response.json())
.then(data=>{images=data; loadImage();})
.catch(error=>console.error('Error with paths',error));

function loadImage(){
    const box=document.getElementById('image-holder');
    box.innerHTML= '';
    if(current <images.length){
        const img=document.createElement('img');
        img.src=images[current];
        box.appendChild(img)
    }
    else{
        console.log('Nothing');
    }
}

function nextImage() {

    current ++ ;
    ar.push('0');
    localStorage.setItem('ratings', JSON.stringify(ar));
    loadImage();
    
}

function Recommend() {
    current ++ ;
    ar.push('1');
    localStorage.setItem('ratings', JSON.stringify(ar));
    loadImage();
}

  function downloadCSV() {
    let csvContent = "data:text/csv;charset=utf-8,Rating\n";
    ar.forEach(rating => {
        csvContent += `${rating}\n`;
    });

    const encodedUri = encodeURI(csvContent);
    const link = document.createElement("a");
    link.setAttribute("href", encodedUri);
    link.setAttribute("download", "ratings.csv");
    document.body.appendChild(link);

    link.click();
    document.body.removeChild(link);
}