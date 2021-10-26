// eslint-disable-next-line no-unused-vars
function taskController(taskid, cmd, csrf) {
	const headers = new Headers({
		'X-CSRF-TOKEN': csrf
	});
	switch(cmd) {
	case 'del':
		//Execute Ajax call to deleteTas route sending the id of the item
		fetch(`/delete_task/${taskid}`, {
			method: 'DELETE',
			headers,
		})
			.then(response => response.json())
			.then(result => {
				console.log('Success: ', result);
				//let obj = document.getElementById('task'+taskid);
				//obj.remove();
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