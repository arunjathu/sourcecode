#!/usr/bin/python

import yaml
import os
import subprocess

finame = raw_input('first name ')
liname = raw_input('last name ')
iage = int(raw_input('age '))

if os.path.isfile('test.yml'):
    file = os.stat('test.yml').st_size

    if file == 0:
        person = dict(users=[dict(unique=1,fname=finame, lname=liname, age=iage),])
        with open('test.yml', 'a') as outfile:
            yaml.dump(person, stream=outfile, default_flow_style=False, indent=4)


    else:
        with open('test.yml', 'a+') as outfile:
               pt=yaml.safe_load(outfile)
               num=len(pt['users'])

        persons = [dict(unique=num+1,fname=finame, lname=liname, age=iage),]
        with open('test.yml', 'a') as outfile:
            yaml.dump(persons, stream=outfile, default_flow_style=False, indent=4)



else:
    os.mknod("test.yml")

    person = dict(users=[dict(unique=1,fname=finame, lname=liname, age=iage),])
    with open('test.yml', 'a') as outfile:
        yaml.dump(person, stream=outfile, default_flow_style=False, indent=4)
