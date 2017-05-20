$(document).ready(function () {
	$('#search-choice-button').click(function () {
		var use_img_url = 'Use Image URL';
		var choose_file = 'Choose Image';
		if ($(this).attr('value') == use_img_url) {
			$('#img').attr('type', 'text');
			$('#search-choice-button').attr('value', choose_file);
		} else if ($(this).attr('value') == choose_file) {
			$('#img').attr('type', 'file');
			$('#search-choice-button').attr('value', use_img_url);
		}
		
	});
});