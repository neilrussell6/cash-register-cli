cash-register
===

> This is some boilerplate for CLI apps

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

```make init name='Your AppName'```

this will setup pip, install dependencies and deploy the app locally
so that it can be run with the ``your-app-name`` command.

### Change GIT remote origin

```bash
git remote set-url origin YOUR_REPO_URL
```

testing
---

Pytest is included as the testing framework,
and configured to expect tests mingled with source files,
and named like: ``NAME_tests.py`. 

Run all tests like this:
```bash
make test
 ```
 
An example CLI test is included.

example setup and usage
---

We want to create a Something Cool CLI app,

so we run:
```bash
make init name='something-cool'
```

This
 - compiles and installs dependencies
 - installs a something-cool script within the virtual environment
 - and adds either 'something-cool' or 'Something Cool' in all the relevant places within the codebase.

So now we can check our CLI works:
```bash
something-cool --version
```

which should output:
```
something-cool, version 0.1.0
```

so now we have a ``something-cool`` CLI
which will have an example command ``say``,
which we can use as follows:
```bash
something-cool say --help  # show help for say command
something-cool say  # run say command, will prompt for options
something-cool say --what="Goodbye" --who="everybody" # run say command with options provided
```

Resources
---

[Click documentation](http://click.pocoo.org/5/)
