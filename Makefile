install_dependencies:
	pip3 install -r requirements.txt

uninstall_dependancies:
	pip3 uninstall -r requirements.txt

start_front_end:
	python3 web_app/server.py

start_back_end:
	python3 src/main.py