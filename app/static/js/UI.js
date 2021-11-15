/* eslint-disable linebreak-style */
/* eslint-disable indent */
'use strict';
document.addEventListener('DOMContentLoaded', () => {
	//Bulma Navbar-Menu Mobile Toggle
	// Get all "navbar-burger" elements
	const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);
	
	// Check if there are any navbar burgers
	if ($navbarBurgers.length > 0) {
		
		// Add a click event on each of them
		$navbarBurgers.forEach( el => {
			el.addEventListener('click', () => {
				
				// Get the target from the "data-target" attribute
				const target = el.dataset.target;
				const $target = document.getElementById(target);
				
				// Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
				el.classList.toggle('is-active');
				$target.classList.toggle('is-active');
			});
		});
	} 	// <-- Navbarmenu togle end
	    
	const signup_button = document.getElementById('signup-button');
	const signup_modal = document.getElementById('signup-modal');
    
	const login_button = document.getElementById('login-button');
	const login_modal = document.getElementById('login-modal');
	
	const project_create_button = document.getElementById('project-create-button');
	const project_create_modal = document.getElementById('project-create-modal');
	
	const task_create_button = document.getElementById('task-create-button');
	const task_create_modal = document.getElementById('task-create-modal');
	
	const task_edit_button = document.getElementById('task-edit-button');
	const task_edit_modal = document.getElementById('task-edit-modal');
	
	const stage_add_button = document.getElementById('stage-add-button');
	const stage_add_modal = document.getElementById('stage-add-modal');
	
	const modal_group = [
		{name:'login', button:login_button, modal:login_modal},
		{name:'signup', button:signup_button, modal:signup_modal},
		{name:'createproject', button:project_create_button, modal:project_create_modal},
		{name:'createtask', button:task_create_button, modal:task_create_modal},
		{name:'edittask', button:task_edit_button, modal:task_edit_modal},
		{name:'addstage', button:stage_add_button, modal:stage_add_modal}
	];
	
	for(const e of modal_group) {
		(function() {
			if(e.button) {
				e.button.addEventListener('click', () => { toggleSpecificModal({modal:e.modal}); });
            }
		}());
	}
});

function toggleSpecificModal({targetid=null, action=null, modal=null, target=null}) {
	switch (true) {
		case (target == 'p') && (action == 'd') :
			modal = document.getElementById('project-delete-modal'+targetid);
			break;
		case (target == 'p') && (action == 'e') :
			modal = document.getElementById('project-edit-modal'+targetid);
			break;
		case (target == 't') && (action == 'd') :
			modal = document.getElementById('task-delete-modal'+targetid);
			break;
		case (target == 't') && (action == 'e') :
			modal = document.getElementById('task-edit-modal'+targetid);
			break;
		default:
			modal = modal;
			break;
	}
	let html = document.getElementsByTagName('html')[0];
	html.classList.add('is-clipped');
	modal.classList.add('is-active');
	
	//Toggle modal off when close (X in top right corner) or cancel button is clicked
	let modal_close = modal.querySelectorAll('.modal-close, .cancel');
	for (const el of modal_close) {
		el.addEventListener('click', () => {
			html.classList.remove('is-clipped');
			modal.classList.remove('is-active');
		});
	}
}

// eslint-disable-next-line no-unused-vars
function toggle_task_details(coll) { 
	coll.classList.toggle('active');
	var content = coll.closest('.expandable-container').getElementsByClassName('expandable-content')[0];
	if (content.style.maxHeight) {
		content.style.maxHeight = null;
	} else {
		content.style.maxHeight = content.scrollHeight + 'px';
	}
}