from Team.Fer.YouTube.main_page import MainPage
from Team.Fer.YouTube.results_page import ResultsPage
from Team.Fer.YouTube.video_page import VideoPage


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

results_page = ResultsPage(test_driver,
                           TestData.VIEWER_MODE,
                           TestData.VERBOSE_MODE,
                           TestData.HIGHLIGHT_MODE)

video_page = VideoPage(test_driver,
                       TestData.VIEWER_MODE,
                       TestData.VERBOSE_MODE,
                       TestData.HIGHLIGHT_MODE)


def test_youtube():
    main_page.start_test_doc()
    main_page.add_cover_page(TestData.TEST_SUMMARY, TestData.ENV_DETAILS, TestData.TESTED_BY)
    main_page.fill_search_form()
    main_page.document_assert_results(True, "User lands on YouTube page and fill search field")
    main_page.proceed_to_search()
    results_page.check_results()
    main_page.document_assert_results(True, "User do de search and results page is loaded")
    results_page.proceed_to_target_video()
    video_page.check_page()
    main_page.document_assert_results(True, "Target Video is played")
    main_page.save_doc_results(f"{TestData.TEST_SUMMARY}-Test Run_{main_page.update_test_run():03d}")
