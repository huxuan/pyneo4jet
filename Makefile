# Clean Code
clean:
	find . -name '*.pyc' -print0 | xargs -0 rm -f
	find . -name '*~' -print0 | xargs -0 rm -f
	find . -name '.*.swp' -print0 | xargs -0 rm -f

# Clean Code and database
depclean: clean
	rm -rf database

# Pylint Code
pylint:
	find . -name "*.py" | xargs pylint

# Data Parser
data-parser:
	python -m data.parser
