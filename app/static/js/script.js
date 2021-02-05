/* eslint-disable linebreak-style */
"use strict"
function modalToggle(modal, html) {
	html[0].classList.add("is-clipped")
	modal.classList.add("is-active")
	//document.getElementById('signup-first-field').focus();

	//Toggle modal off when close (X in top right corner) or cancel button is clicked
	let modal_close = modal.querySelectorAll(".modal-close, .cancel")
	for (const el of modal_close) {
		el.addEventListener("click", () => {
			html[0].classList.remove("is-clipped")
			modal.classList.remove("is-active")
		})
	}
}
document.addEventListener("DOMContentLoaded", () => {
	//Bulma Navbar-Menu Mobile Toggle
	// Get all "navbar-burger" elements
	const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll(".navbar-burger"), 0)

	// Check if there are any navbar burgers
	if ($navbarBurgers.length > 0) {

		// Add a click event on each of them
		$navbarBurgers.forEach( el => {
			el.addEventListener("click", () => {

				// Get the target from the "data-target" attribute
				const target = el.dataset.target
				const $target = document.getElementById(target)

				// Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
				el.classList.toggle("is-active")
				$target.classList.toggle("is-active")
			})
		})
	} 	// <-- Navbarmenu togle end


	const html = document.getElementsByTagName("html")
    
	const signup_button = document.getElementById("signup-button")
	const signup_modal = document.getElementById("signup-modal")
    
	const project_create_button = document.getElementById("project-create-button")
	const project_modal = document.getElementById("project-create-modal")

	const task_create_button = document.getElementById("task-create-button")
	const task_modal = document.getElementById("task-create-modal")

	const login_button = document.getElementById("login-button")
	const login_modal = document.getElementById("login-modal")

	const modal_group = [
		{button:login_button, modal:login_modal},
		{button:signup_button, modal:signup_modal},
		{button:project_create_button, modal:project_modal},
		{button:task_create_button, modal:task_modal}
	]

	for(const e of modal_group) {
		(function() {
			e.button.addEventListener("click", () => { modalToggle(e.modal, html) })
		}())
	}
})
