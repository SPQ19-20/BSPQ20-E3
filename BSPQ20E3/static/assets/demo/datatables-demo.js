// Call the dataTables jQuery plugin
$(document).ready(function() {

  $('#dataTable').DataTable(
  {
  	'iDisplayLength': 25
  }
  	);
  $('.languageSelector').selectpicker({
    style: "btn-default btn-sm"
});
});