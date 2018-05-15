style:
	pycodestyle *.py

test:
	pytest

check: test style
