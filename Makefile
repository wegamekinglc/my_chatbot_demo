train:
	rasa train --domain domain.yml --data data --config config.yml --out models

run-cmdline:
	rasa run actions --actions actions & rasa shell --endpoints endpoints.yml -m models --debug

run-x:
	rasa run actions --actions actions & rasa x -m models --endpoints endpoints.yml --debug
