#!/usr/bin/python3


import yaml
import os

file = os.stat('test.yml').st_size

finame = input('first name ')
liname = input('last name ')
iage = int(input('age '))


if file == 0:
  person = dict(users=[dict(fname=finame, lname=liname, age=iage),])
  with open('test.yml', 'a') as outfile:
    yaml.dump(person, sort_keys=False, stream=outfile, default_flow_style=False, indent=4)

    
else:
  persons = [dict(fname=finame, lname=liname, age=iage),]
  with open('test.yml', 'a') as outfile:
    yaml.dump(persons, sort_keys=False, stream=outfile, default_flow_style=False, indent=4)
