#!/usr/bin/python3


import yaml
import os

file = os.stat('test.yml').st_size

finame = input('first name ')
liname = input('last name ')
iage = int(input('age '))


person = dict(users=[dict(fname=finame, lname=liname, age=iage),])


persons = [dict(fname=finame, lname=liname, age=iage),]

if file == 0:
  with open('test.yml', 'a') as outfile:
    yaml.dump(person, sort_keys=False, stream=outfile, default_flow_style=False, indent=4)
else:
  with open('test.yml', 'a') as outfile:
    yaml.dump(persons, sort_keys=False, stream=outfile, default_flow_style=False, indent=4)
