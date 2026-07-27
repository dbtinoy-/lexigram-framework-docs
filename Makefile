.DEFAULT_GOAL := help

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
	  awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-18s\033[0m %s\n", $$1, $$2}'

.PHONY: publish
publish:  ## Generate docs, commit, push. Usage: make publish m="commit message"
	@if [ -z "$(m)" ]; then echo "ERROR: m=\"commit message\" is required"; exit 1; fi
	python scripts/sync-readmes.py
	python scripts/generate-api.py
	git add -A
	git commit -m "$(m)"
	git push

.PHONY: publish-public
publish-public:  ## Publish sanitized public mirror (dry run). Usage: make publish-public m="msg"
	@if [ -z "$(m)" ]; then echo "ERROR: m=\"commit message\" is required"; exit 1; fi
	COMMIT_MSG="$(m)" bash scripts/publish_public.sh $(FLAGS)

.PHONY: publish-public-reset
publish-public-reset:  ## Force-push public mirror with single initial commit
	COMMIT_MSG="Initial public release — Lexigram (MIT)" bash scripts/publish_public.sh --reset --push

.PHONY: publish-public-force
publish-public-force:  ## Force-push public mirror with custom message. Usage: make publish-public-force m="msg"
	@if [ -z "$(m)" ]; then echo "ERROR: m=\"commit message\" is required"; exit 1; fi
	COMMIT_MSG="$(m)" bash scripts/publish_public.sh --reset --push
