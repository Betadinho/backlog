// eslint-disable-next-line no-unused-vars
function taskController(taskid, cmd, csrf) {
	//const reload = window.location.href;
	const headers = new Headers({
		'X-CSRF-TOKEN': csrf
	});
	switch(cmd) {
	case 'del':
		fetch(`/delete_task/${taskid}`, {
			method: 'DELETE',
			headers,
		})
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
	const headers = new Headers({
		'X-CSRF-TOKEN': csrf
	});
	//let reload = window.location.href;
	switch(cmd) {
	case 'del':
		fetch(`/delete_project/${projectid}`, {
			method: 'DELETE',
			headers,
		})
			.then(response => response.json())
			.then(result => {
				console.log('Success: ', result);
			})
			.catch(error => {
				console.log(error);
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