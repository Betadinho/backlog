/* eslint-disable linebreak-style */
// eslint-disable-next-line no-unused-vars
function toggle_task_details(coll) { 
	coll.classList.toggle("active")
	var content = coll.closest(".expandable-container").getElementsByClassName("expandable-content")[0]
	if (content.style.maxHeight) {
		content.style.maxHeight = null
	} else {
		content.style.maxHeight = content.scrollHeight + "px"
	}
}

    