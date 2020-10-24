function showSnackbar() {
  var snackBar = document.getElementById("snackbar");

  snackBar.className = "show-bar";

  setTimeout(function () {
    snackBar.className = snackBar.className.replace("show-bar", "");
  }, 5000);
}

// function post() {
//   var form = document.getElementById("add-carrinho");
//   form.submit();
// }
// function post(path = '/busca', method='post') {

//   // The rest of this code assumes you are not using a library.
//   // It can be made less wordy if you use one.
//   const form = document.createElement('form');
//   form.method = method;
//   form.action = path;

//   const hiddenField = document.createElement('input');
//   hiddenField.type = 'hidden';
//   hiddenField.name = 'desfazer';
//   hiddenField.value = true;

//   form.appendChild(hiddenField);

//   document.body.appendChild(form);
//   form.submit();
// }
