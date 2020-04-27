// Call the dataTables jQuery plugin
$(document).ready(function() {

  $('#dataTable').DataTable(
  {
  	"bPaginate": false,
  }
  	);
  $('.languageSelector').selectpicker({
    style: "btn-default btn-sm"
});
});