test:
	@python3 ./src/test.py
push:
	@git add --all && git commit -m "$(MSG)" && git push

# 快速提交
git:
	@$(MAKE) push MSG="$(filter-out $@,$(MAKECMDGOALS))"