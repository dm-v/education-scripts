# -*- coding: utf-8 -*-

import subprocess

script_name = 'shell_exec.py'

courses_list_file = '/tmp/courses.txt'
current_course_id_file = '/tmp/course.id.log'
cmd = '/edx/app/edxapp/venvs/edxapp/bin/python /edx/app/edxapp/edx-platform/manage.py cms shell --settings=aws < /edx/app/edxapp/scripts/%s' % script_name

courses = []

with open(courses_list_file, 'r') as f:
    course_id = f.readline()
    while course_id:
        print 'Start process course: ', course_id
        target_file = open(current_course_id_file, 'w')
        target_file.write(course_id)
        target_file.close()

        subprocess.call(cmd, shell=True)
        course_id = f.readline()
