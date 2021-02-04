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


	let html = document.getElementsByTagName('html');
	let signup_button = document.getElementById('signup-button');
	let signup_modal = document.getElementById('signup-modal');

	let login_button = document.getElementById('login-button');
	let login_modal = document.getElementById('login-modal');
    //let logout_button = document.getElementsByClassName('logout-button');
    //let logout_modal = document.getElementsByClassName('logout-modal');

    //Signup modal toggle
	signup_button.addEventListener('click', () => {
		html[0].classList.add('is-clipped');
        signup_modal.classList.add('is-active');
        document.getElementById('signup-first-field').focus();

		//Toggle modal off when close (X in top right corner) or cancel button is clicked
        var modal_close = signup_modal.querySelectorAll('.modal-close, .cancel-signup');
        for(e of modal_close) {
            e.addEventListener('click', () => {
                html[0].classList.remove('is-clipped');
                signup_modal.classList.remove('is-active');
            });
        };  
        
        
	});

	//Login modal toggle
	login_button.addEventListener('click', () => {
		//Toggle Modal to be visible
		html[0].classList.add('is-clipped');
        login_modal.classList.add('is-active');
        document.getElementById('login-first-field').focus();

		//Toggle modal off when close is clicked
		var modal_close = login_modal.querySelectorAll('.modal-close, .cancel-login');
		for(e of modal_close) {
            e.addEventListener('click', () => {
                html[0].classList.remove('is-clipped');
                login_modal.classList.remove('is-active');
            });
        };
	});

	//logout modal toggle
	/*logout_button.addEventListener('click', () => {
		html[0].classList.add('is-clipped');
		logout_modal.classList.toggle('is-active');
	});*/

});
