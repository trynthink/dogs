$(document).ready(function(){

	// Declare variables for JSON database keys
	var theBreed;
	var theStates;

	// Declare variable for sum of entries
	var total = 0;

	// Display the total in the appropriate location on the page
	$('#number').text(total)

	// Detect selected radio button - Breed
	$('#dog_breed').on('change', function(){
		theBreed = $('input[name=options]:checked', '#dog_breed').val();
	});

	// Detect selections in list - State(s)
	$('#US_states').on('click', function (){
		theStates = $('#US_states').val();
	});

	// NEED TO PUT IN PLACE SOME ERROR HANDLING ON THE BUTTON CLICK
	// IF NOT ALL THE SELECTIONS HAVE BEEN MADE

	// Query database and update total when button is clicked
	$('#update').on('click', function(){
		// Reset total
		total = 0;
		
		// Sum the totals for all states selected
		$.getJSON('resources/grouped_dogs.json', function(data){
			for (var i = 0 ; i < theStates.length ; i++) {
				total = total + data[theBreed][theStates[i]]['Age'];
			}
			
			// Update total number displayed
			$('#number').text(total)
		});
	});

});