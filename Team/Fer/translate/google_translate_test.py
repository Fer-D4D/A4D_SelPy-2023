from Team.Fer.translate.main_page import MainPage


class TestData:
    BROWSER = "chrome"
    VIEWER_MODE = "OFF"  # Turning this ON add a small pause in between each test step
    VERBOSE_MODE = "ON"  # By turning this ON you will get some useful information about the test run
    HIGHLIGHT_MODE = "OFF"  # Turning this ON will highlight the element being used
    TEST_SUMMARY = "YouTube Simple Searching test"
    ENV_DETAILS = "PROD V34"
    TESTED_BY = "Fernando Perez"


main_page = MainPage(TestData.BROWSER,
                     TestData.VIEWER_MODE,
                     TestData.VERBOSE_MODE,
                     TestData.HIGHLIGHT_MODE)

main_page.set_ss_fail_mode("OFF")

test_driver = main_page.get_driver()

main_page.fill_translate_form()

