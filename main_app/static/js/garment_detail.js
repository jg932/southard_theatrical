const fileInput = document.getElementById('file-input')
const fileName = document.getElementById('file-name')
const availableButton = document.getElementById('available_button')
const outOfStockDisplay = document.getElementById('out_of_stock_display')

availableButton.addEventListener("click", outOfStock)

function outOfStock(){
  outOfStockDisplay.hidden=false
}


fileInput.addEventListener('change', evt => {
  const fileToUpload = evt.target.files[0].name
  if(fileToUpload) {
    fileName.innerText = fileToUpload
  } else {
    fileName.innerText = ""
  }
})