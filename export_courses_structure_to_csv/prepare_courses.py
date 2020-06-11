from openedx.core.djangoapps.content.course_overviews.models import CourseOverview

courses_list_file = '/tmp/courses.txt'

courses = CourseOverview.objects.all()

print 'Prepare course list'

with open(courses_list_file, 'w') as f:
    for course in courses:
        run = course.id.run
        if '2018' in run or '2019' in run or '2020' in run:
            f.write(str(course.id) + '\n')
