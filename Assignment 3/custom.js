// Create circle svg elements.
// let moneyCircle = document.querySelectorAll(".circle");
// var moneyTexts = [1, 0.5, 0.25, 0.05];
// for (let i = 0; i < moneyCircle.length; i++) {
//     // https://stackoverflow.com/a/69877010
//     /* Inserts a circle svg element into the flex-column and adds the 
//     money value to the center of the circle. */
//     moneyCircle[i].innerHTML = `<div class="position-relative">
//     <svg xmlns="http://www.w3.org/2000/svg" width="80" height="80"
//         fill="currentColor" class="bi bi-circle" viewBox="0 0 16 16">
//         <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0
//             0 0 0 16z"/>
//         </svg>
//         <div class="d-flex justify-content-center align-items-center position-absolute w-100 h-100 p-1" style="top:0;left:0;">
//             <h1 class="position-absolute" style='font-size: xx-large;'>${moneyTexts[i]}</h1>
//         </div>
//     </div>`;
// }

let image = document.getElementById("instruction-img");
document.getElementById("large").onclick = function(){
    image.setAttribute("src", "https://media.tenor.com/8rExDsHkqhYAAAAd/jinx.gif")
}
document.getElementById("medium").onclick = function(){
    image.setAttribute("src", "https://media.tenor.com/naVSbnJjxxIAAAAC/cat.gif")
}
document.getElementById("small").onclick = function(){
    image.setAttribute("src", "https://media.discordapp.net/attachments/940836266889576488/991556419570630747/8DEAD03-D1EF-4CCA-8F4A-B0A77270D35E-1.gif")
}