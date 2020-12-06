ROOT_DIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))
DAY:=$(shell date +%-d)
YEAR:=$(shell date +%Y)
ZERODAY:=$(shell printf "%02d" $(DAY))

.PHONY: all
all:
	@$(MAKE) usage | less

.PHONY: usage
usage:
	@echo
	@echo 'make TARGET [option=value, ...]'
	@echo
	@echo 'ENVIRONMENT'
	@echo
	@echo '  make env'
	@echo '    - Rebuild development envionrment'
	@echo
	@echo 'CREATING FILES'
	@echo
	@echo '  edit [DAY=<day>, YEAR=<year>]'
	@echo '    - Create template if missing, and edit'
	@echo

.PHONY: edit
edit:
	@program="$(ROOT_DIR)/$(YEAR)/day$(ZERODAY)/day$(ZERODAY).py"; \
	if [ ! -f "$$program" ]; then \
		mkdir -p "$${program%/*}"; \
		$(MAKE) template > "$$program"; \
		chmod a+x "$$program"; \
	fi; \
	vim "$$program"

.PHONY: time
time:
	@time -p for pgm in $(ROOT_DIR)/$(YEAR)/day*/day*.py; do "$$pgm" -d; done

.PHONY: template
template:
	@sed "s/YEAR/$(YEAR)/g; s/DAY/$(DAY)/g" < $(ROOT_DIR)/common/template.py

.PHONY: env
env: env-destroy $(ROOT_DIR)/env

$(ROOT_DIR)/env:
	@$(MAKE) env-create env-update env-report

.PHONY: env-create
env-create:
	@if ! command -v python3 &>/dev/null; then \
		echo "Python 3 is not available, please install it."; \
		false; \
	fi
	@echo "Building development virtual env"
	python3 -m venv --clear "$(ROOT_DIR)/env"
	"$(ROOT_DIR)/env/bin/pip3" install --upgrade --no-cache-dir pip setuptools wheel
	@printf "#!/bin/sh\nexec /usr/bin/env python -m pydoc \"\$$@\"\n" > $(ROOT_DIR)/env/bin/pydoc
	@chmod a+x $(ROOT_DIR)/env/bin/pydoc

.PHONY: env-update
env-update:
	@for egg in "$(ROOT_DIR)"/common/*.egg-info; do \
		rm -rf "$$egg"; \
	done
	@echo "Updating virtual env with latest source distribution"
	"$(ROOT_DIR)/env/bin/pip3" install --editable $(ROOT_DIR)/common[test]

.PHONY: env-report
env-report:
	@echo
	@echo Python virtual environment built, to enable run the following:
	@echo
	@echo "  source $(ROOT_DIR)/env/bin/activate"
	@echo

.PHONY: env-destroy
env-destroy:
	@if [ -d env ]; then \
		echo "Removing previous virtual env"; \
		rm -rf $(ROOT_DIR)/env; \
	fi

