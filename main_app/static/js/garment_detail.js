const fileInput = document.getElementById('file-input')
const fileName = document.getElementById('file-name')
const unavailableButton = document.getElementById('unavailable_button')
const availableButton = document.getElementById('available_button')
const outOfStockDisplay = document.getElementById('out_of_stock_display')

unavailableButton.addEventListener("click", outOfStock)
availableButton.addEventListener("click", backInStock)

function outOfStock(){
  outOfStockDisplay.hidden=false
  unavailableButton.hidden=true
  availableButton.hidden=false
}

function backInStock(){
  outOfStockDisplay.hidden=true
  availableButton.hidden=true
  unavailableButton.hidden=false
}


fileInput.addEventListener('change', evt => {
  const fileToUpload = evt.target.files[0].name
  if(fileToUpload) {
    fileName.innerText = fileToUpload
  } else {
    fileName.innerText = ""
  }
})