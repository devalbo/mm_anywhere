
var runningLive = false;

getLatestImage = function(data) {
	$('#acq-image-div').load(serverUrl + "snap-image",
		function(response, status, xhr) {
			if (runningLive) {
				$.timer(function() {
					getLatestImage();
				}).once(500);
			}
        });
}

registerEnterKey = function(selectorStr) {
    $(selectorStr).keyup(function(e) {
        if (e.which == 13) // Enter key
            $(this).blur();
    });
    $(selectorStr).keypress(function(e) { return e.which != 13; });
}