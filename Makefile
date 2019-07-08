train:
	rasa train --domain domain.yml --data data --config config.yml --out models

run-cmdline:
	rasa run actions --actions actions & 
	rasa shell --endpoints endpoints.yml -m models --debug
