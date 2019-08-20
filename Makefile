CUR_DIR = $(CURDIR)

venv:
	virtualenv -p `which python3` venv

source:
	source venv/bin/activate

exit:
	deactivate

develop: venv
	venv/bin/pip install -e . -r requirements/base.txt
	venv/bin/pip install -e . -r requirements/test.txt

install:
	pip3 install -e . -r requirements/base.txt
	pip3 install -e . -r requirements/test.txt

clean:
	-rm -rf venv
	-rm -rf .tox

test:
	tox

require:
	venv/bin/pip freeze > requirements.txt
