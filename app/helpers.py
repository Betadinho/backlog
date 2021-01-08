# Flask creates a rule for the static endpoint a initialization
# this means that setting static_url_path and static_folder
# after initilzation do not change the result of url_for('static', filename=...)

# app is in instance of the Flask class

# Delete the old rule and substitute your own
# Note this looks like it could change from implementation
# to implementation but I see no other way
def delete_static_rule(new_path, app):
	# new static path, update the instance just to keep everything consistent
	app.static_url_path = new_path
	del app.url_map._rules_by_endpoint['static']
	app.add_url_rule(
	    f"{app.static_url_path}/<path:filename>",
	    endpoint="static",
	    host=None,
	    view_func=app.send_static_file,
	)
	return app
