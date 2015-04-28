$(document).ready(function(){
	$.getJSON('resources/dogs.json', function(data){
		for (var i = 0 ; i < data.length ; i++) {
			var stuff_to_show = data[i]['Name'];
			$('#loc').append('<p>' + stuff_to_show + '</p>');
		}
	});
});