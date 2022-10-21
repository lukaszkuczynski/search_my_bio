prod:
	python cv_generator.py -p platform

test:
	python cv_generator.py -p beans -pf ./profiles_template.yml -f ./life_tasks_template.yml