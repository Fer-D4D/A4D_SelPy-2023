import time

from Team.Fer.lets_build_a_framework_from_scratch.core.new_common import TinyCore, ImprovedTinyCore
from Team.Fer.lets_build_a_framework_from_scratch.core.utils import timer

lets_automate = ImprovedTinyCore()

lets_automate.set_chrome_driver()

ADVANTAGE_CREATE_NEW_ACCOUNT_BUTTON = "//*[@id='hrefUserIcon']"
ADVANTAGE_USERNAME_FORM_FIELD = "//*[@name='usernamed']"
WAITING_TIME = 1


@timer
def using_manual_wait():
    print("Going manual wait:")
    lets_automate.launch_site("http://advantageonlineshopping.com/")
    time.sleep(3)
    lets_automate.do_click(ADVANTAGE_CREATE_NEW_ACCOUNT_BUTTON)
    time.sleep(1)
    lets_automate.type_in_text_field(ADVANTAGE_USERNAME_FORM_FIELD, "hp c")
    time.sleep(.5)
    lets_automate.force_text_value(ADVANTAGE_USERNAME_FORM_FIELD, "hp e")
    time.sleep(WAITING_TIME)
    lets_automate.tear_down()


using_manual_wait()

lets_automate = ImprovedTinyCore()
lets_automate.set_chrome_driver()


@timer
def using_implicit_wait():
    print("Going implicit wait:")
    lets_automate.set_implicit_wait(5)
    lets_automate.launch_site("http://advantageonlineshopping.com/")
    lets_automate.do_click(ADVANTAGE_CREATE_NEW_ACCOUNT_BUTTON)
    lets_automate.type_in_text_field(ADVANTAGE_USERNAME_FORM_FIELD, "hp c")
    lets_automate.force_text_value(ADVANTAGE_USERNAME_FORM_FIELD, "hp e")
    time.sleep(WAITING_TIME)
    lets_automate.tear_down()


using_implicit_wait()

lets_automate = ImprovedTinyCore()
lets_automate.set_chrome_driver()


@timer
def using_explicit_wait():
    print("Going explicit wait:")
    lets_automate.launch_site("http://advantageonlineshopping.com/")
    lets_automate.explicit_wait_n_do_click(ADVANTAGE_CREATE_NEW_ACCOUNT_BUTTON)
    lets_automate.explicit_wait_n_type_in_text_field(ADVANTAGE_USERNAME_FORM_FIELD, "hp c")
    lets_automate.explicit_wait_n_force_text_value(ADVANTAGE_USERNAME_FORM_FIELD, "hp e")
    time.sleep(WAITING_TIME)
    lets_automate.tear_down()


using_explicit_wait()

lets_automate = ImprovedTinyCore()
lets_automate.set_chrome_driver()


@timer
def using_efficient_wait():
    print("Going efficient wait:")
    lets_automate.launch_site("http://advantageonlineshopping.com/")
    lets_automate.fluent_wait_n_do_click(ADVANTAGE_CREATE_NEW_ACCOUNT_BUTTON)
    lets_automate.fluent_wait_n_type_in_text_field(ADVANTAGE_USERNAME_FORM_FIELD, "hp c")
    lets_automate.fluent_wait_n_force_text_value(ADVANTAGE_USERNAME_FORM_FIELD, "hp e")
    time.sleep(WAITING_TIME)
    lets_automate.tear_down()


using_efficient_wait()
