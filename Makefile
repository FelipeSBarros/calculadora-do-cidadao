clean:
	@rm -rf .coverage
	@rm -rf .eggs
	@rm -rf .mypy_cache
	@rm -rf .pytest_cache
	@rm -rf .ropeproject
	@rm -rf .tox
	@rm -rf calculadora_do_cidadao.egg-info
	@rm -rf dist
	@find . -iname "*.pyc" | xargs rm -rf
	@find . -iname "__pycache__" | xargs rm -rf
