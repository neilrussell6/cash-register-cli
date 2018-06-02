Cash Register
===

> A Cash Register CLI app

setup
---

### Virtual env

setup a virtual environment:
```bash
sudo apt-get install -y python3-venv
python3 -m venv venv
source venv/bin/activate
```

optional: add an alias to ``.bash_aliases``
```bash
alias activate="source venv/bin/activate/"
```

### Initialize

```make init```

this will setup pip, install dependencies and install script locally
so that it can be run with the ``cash-register`` command.

testing
---

Run all tests like this:
```bash
make test
 ```

commands
---

To create a new bill run:
```bash
cash-register bill
```
And follow the prompts
