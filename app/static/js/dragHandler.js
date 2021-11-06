import { persistTaskStageChange } from './crudController.js';
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

