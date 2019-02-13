#!/usr/bin/env python3
import pexpect

p = pexpect.spawn('cookiecutter .')

p.expect('subproject_name.*')
p.sendline('example')

p.expect('subpackage_name.*')
p.sendline('example')

# Runs until the cookiecutter is done; then exits.
p.interact()
