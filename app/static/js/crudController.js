var dragged;
var dropzones = document.getElementsByClassName('dropzone');
const  CSRFTOKEN = () => {
	//Check Dom for csrf token element
	try {
		return document.getElementsByName('CSRFTOKEN')[0].value;
	} catch (error) {
		return error;
	}
};

/* events fired on the draggable target */
// eslint-disable-next-line no-unused-vars
document.addEventListener('drag', function( event ) {
}, false);

document.addEventListener('dragstart', function( event ) {
	// store a ref. on the dragged elem
	dragged = event.target;
	// make it half transparent
	event.target.style.opacity = .5;
	// Get dropzone to the forground and set full height
	Array.from(dropzones).forEach(e => {
		e.style.zIndex = 10;
		e.style.height = '100vh';
	});
}, false);

document.addEventListener('dragend', function( event ) {
	// reset the transparency
	event.target.style.opacity = '';
	// reset dropzone z-index and height
	Array.from(dropzones).forEach(e => {
	e.style.zIndex = '';
	e.style.height = '';
	});
}, false);

/* events fired on the drop targets */
document.addEventListener('dragover', function( event ) {
	// prevent default to allow drop
	event.preventDefault();
}, false);

document.addEventListener('dragenter', function( event ) {
	// highlight potential drop target when the draggable element enters it
	if ( event.target.classList.contains('dropzone') ) {
		event.target.style.background = '#d81b60';
	}

}, false);

document.addEventListener('dragleave', function( event ) {
	// reset background of potential drop target when the draggable element leaves it
	if ( event.target.classList.contains('dropzone') ) {
		event.target.style.background = '';
	}

}, false);

document.addEventListener('drop', function( event ) {
	// prevent default action (open as link for some elements)
	event.preventDefault();
	// move dragged elem to the selected drop target
	if ( event.target.classList.contains('dropzone') ) {
		event.target.style.background = '';
		dragged.parentNode.removeChild( dragged );
		event.target.querySelector('.task-list').appendChild( dragged );
		let csrf = CSRFTOKEN();
		//Get Task id from Dragged
		let taskid = dragged.getElementsByTagName('param')[0].value;
		//Get Stageid from dropzone#
		let stageid = event.target.getElementsByTagName('param')['stageid'].value;
		// make request containing stage changes to server
		persistTaskStageChange(taskid=taskid, stageid=stageid, csrf=csrf);
	}
    
}, false);

// eslint-disable-next-line no-unused-vars
function taskController(taskid, cmd, csrf) {
	//const reload = window.location.href;
	const headers = new Headers({
		'X-CSRF-TOKEN': csrf
	});
	switch(cmd) {
	case 'del':
		//returns a promise that resolves with a Response object
		fetch(`/delete_task/${taskid}`, {
			method: 'DELETE',
			headers,
		})//returns a second promise that resolves with the result of parsing the response body text as JSON
			.then(response => response.json())
			.then(result => {
				console.log('Success: ', result);
			})
			.catch(error => {
				console.log('Error: ', error);
			});
			window.location.reload();
		break;
	case 'edit':
		//Do stuff
		break;
	case 'close':
		//Do stuff
		break;
			
	}
}
// eslint-disable-next-line no-unused-vars
function projectController(projectid, cmd, csrf) {
	//const reload = window.location.href;
	const headers = new Headers({
		'X-CSRF-TOKEN': csrf
	});
	switch(cmd) {
	case 'del':
		fetch(`/delete_project/${projectid}`, {
			method: 'DELETE',
			headers,
			})
			.then(response => response.json())
			.then(result => {
				console.log('Success: ', result);
				window.location.reload();
			})
			.catch(error => {
				console.log('Error: ', error);
				window.location.reload();
			});
		break;
	case 'edit':
		//Do stuff
		break;
	case 'close':
		//Do stuff
		break;
			
	}
}

// eslint-disable-next-line no-unused-vars
function persistTaskStageChange(taskid, stageid, csrf) {
	const headers = new Headers({
		'X-CSRF-TOKEN': csrf,
	});
	fetch(`/persiststage?taskid=${taskid}&stageid=${stageid}`, {
		method: 'POST',
		headers
		})
		.then(response => response.json())
		.then(result => {
			console.log('Success: ', result);
		})
		.catch(error => {
			console.log(error);
		});
}

