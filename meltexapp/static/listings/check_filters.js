function check(form_id) {
  document.getElementById(form_id).checked = true;
}

function check_all(form_ids) {
  for (form_id of form_ids) {
    document.getElementById(form_id).checked = true;
  }
}

// function exampleFunction(...args) {
//   for (var i = 0; i < args.length; i++) {
//     console.log(args[i]);
//   }
// }

function check_all_lists(...args) {
  var form_id_lists = Array.from(args)
  for (form_ids of form_id_lists) {
    for (form_id of form_ids) {
      document.getElementById(form_id).checked = true;
    }
  }
}
