// Call the dataTables jQuery plugin
$(document).ready(function() {

  $('#dataTable').DataTable(
  {
  	bFilter: false,
  	"bPaginate": false,
  	"paging": false,
	"info": false,
  }
  	);
  $('.languageSelector').selectpicker({
    style: "btn-default btn-sm"
});
});