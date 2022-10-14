printcv:
	python cv_generator.py -p all

test:
	python cv_generator.py -p beans -pf ./profiles_template.yml -f ./life_tasks_template.yml