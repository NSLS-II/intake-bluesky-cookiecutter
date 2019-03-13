#!/usr/bin/env python3
import pexpect

p = pexpect.spawn('cookiecutter .')

p.expect('subproject_name.*')
p.sendline('example')

p.expect('subpackage_name.*')
p.sendline('example')

p.expect('pypi_username.*')
p.sendline('test')

p.expect('github_orgname.*')
p.sendline('test')

# Runs until the cookiecutter is done; then exits.
p.interact()
