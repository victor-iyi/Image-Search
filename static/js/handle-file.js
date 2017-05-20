$(document).ready(function () {
	$('#img').on('change', function (e) {
		var file = $(this)[0].files;
		if (file.length == 1) {
			var filename = e.target.value.split('\\').pop();
			$('#img-url').attr('value', filename);
		}
	});
});

$(document).ready(function () {
	$('#open-camera').on('change', function (e) {
		var file = $(this)[0].files;
		if (file.length == 1) {
			var filename = e.target.value.split('\\').pop();
			$('#img-url').attr('value', filename);
		}
	});
});