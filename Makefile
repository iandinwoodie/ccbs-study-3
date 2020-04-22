CCBS = python3 -m ccbs
PIP = pip3
REQ = requirements.txt
COMMANDS = help pull push init freeze

default: help

help:
	@echo "Please do 'make COMMAND' where COMMAND is one of these:"
	@echo "  $(COMMANDS)"

push pull:
	$(CCBS) $@ owner
	$(CCBS) $@ dog

init:
	$(PIP) install -r $(REQ)

freeze:
	$(PIP) freeze --all | grep -v -e "pkg-resources" -e "setuptools" -e "pip" > $(REQ)

.PHONY: default help $(COMMANDS)
