// Create circle svg elements.
let moneyCircle = document.querySelectorAll(".circle");
for (const element of moneyCircle) {
    // https://stackoverflow.com/a/69877010
    element.innerHTML = `<div class="position-relative">
    <svg xmlns="http://www.w3.org/2000/svg" width="80" height="80"
        fill="currentColor" class="bi bi-circle" viewBox="0 0 16 16">
        <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0
            0 0 0 16z"/>
        </svg>
        <div class="d-flex justify-content-center align-items-center position-absolute w-100 h-100 p-3" style="top:0;left:0;">
            <h1 class="position-absolute" style='font-size:larger'></h1>
        </div>
    </div>`;

    console.log(moneyCircle);
    var moneyTexts = [1, 0.5, 0.25, 0.05];
    for (let i = 0; i < moneyCircle.length; i++) {
        let moneyTextBox = moneyCircle[i].querySelector("h1");
        console.log(moneyTextBox);
        moneyTextBox.innerHTML = moneyTexts[i];
    }
}