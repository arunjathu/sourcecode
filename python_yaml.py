#!/usr/bin/python3

import yaml
import os
import subprocess

finame = input('first name ')
liname = input('last name ')
iage = int(input('age '))

if os.path.isfile('test.yml'):
    file = os.stat('test.yml').st_size

    if file == 0:
        person = dict(users=[dict(userid=1,fname=finame, lname=liname, age=iage),])
        with open('test.yml', 'a') as outfile:
            yaml.dump(person, stream=outfile, default_flow_style=False, sort_keys=False, indent=4)


    else:
        with open('test.yml', 'a+') as outfile:
               pt=yaml.load(outfile,Loader=yaml.FullLoader)
               num=len(pt['users'])

        persons = [dict(userid=num+1,fname=finame, lname=liname, age=iage),]
        with open('test.yml', 'a') as outfile:
            yaml.dump(persons, stream=outfile, default_flow_style=False, sort_keys=False, indent=4)



else:
    os.mknod("test.yml")

    person = dict(users=[dict(userid=1,fname=finame, lname=liname, age=iage),])
    with open('test.yml', 'a') as outfile:
        yaml.dump(person, stream=outfile, default_flow_style=False, sort_keys=False, indent=4)
