var dragging = false;
var path = "";

// Adapted from https://stackoverflow.com/questions/4127118/can-you-detect-dragging-in-jquery
$("#canvas")
.mousedown(function(event){
	// Start dragging
	dragging = true;

	// Start path by moving to current mouse position
	// Adapted from https://stackoverflow.com/questions/23897002/getting-mouse-position-within-svg
	path += "M " + event.offsetX + " " + event.offsetY + " ";
})

.mousemove(function(event){
	if (dragging){
		// Add to path a line to current mouse position
		path += "L " + event.offsetX + " " + event.offsetY + " ";
		
		// Add the path to the SVG
		$("#path").attr("d", path)
	}
})

.mouseup(function(){
	dragging = false;
})

$("#clear").click(function(){
	$("#path").attr("d", "")
	path = ""
})