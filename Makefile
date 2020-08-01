init:
    pip install -r requirements.txt

test:
	python -m unittest discover -v

roll:
	python .\dice\dice.py -s 6 -a 10 -t 4

run:
	python .\dice\app.py

.PHONY: init test