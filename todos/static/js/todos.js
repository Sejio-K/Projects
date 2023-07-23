function addNewLabel() {
  var newLabelInput = document.getElementById("id_new_label");
  var labelSelect = document.getElementById("id_label");
  var optionExists = Array.from(labelSelect.options).some(function(option) {
    return option.value.trim() === newLabelInput.value.trim(); // Обработка пробелов здесь
  });

  if (!optionExists && newLabelInput.value.trim() !== "") {
    var newOption = document.createElement("option");
    newOption.text = newLabelInput.value.trim(); // Обработка пробелов здесь
    newOption.value = newLabelInput.value.trim(); // Обработка пробелов здесь
    labelSelect.appendChild(newOption);
    newLabelInput.value = "";
  }
}

