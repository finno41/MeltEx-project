function check(form_id) {
  document.getElementById(form_id).checked = true;
}

function check_all(form_ids) {
  for (form_id of form_ids) {
    document.getElementById(form_id).checked = true;
  }
}

function check_all_lists(list_of_ids) {
  for (form_ids of list_of_ids) {
    for (form_id of form_ids) {
      document.getElementById(form_id).checked = true;
    }
  }
}
