from Team.lau.test.Week2.enrollment_base import enrollment_form

enrollment = enrollment_form()
enrollment.create_driver()

enrollment.validate_name_error()
#enrollment.do_enrollment()
enrollment.delay_time(3)