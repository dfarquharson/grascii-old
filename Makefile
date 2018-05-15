style:
	pycodestyle *.py

test:
	pytest --cov-report term \
		--cov . \
		--cov-branch

coverage-html:
	pytest --cov-report html \
		--cov . \
		--cov-branch

check: test style
