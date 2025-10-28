import pytest
from playwright.sync_api import Page, expect
from pages.course_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage

class TestCourses:


    @pytest.mark.courses
    @pytest.mark.regression
    def test_create_course(self, course_list_page: CoursesListPage, create_course_page: CreateCoursePage):
        create_course_page.open('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')
        #1
        create_course_page.check_visible_create_course_title()
        create_course_page.check_visible_create_course_button()
        #2
        create_course_page.check_disabled_create_course_button()
        #3
        create_course_page.check_visible_image_preview_empty_view()
        #4
        create_course_page.check_visible_image_upload_view(is_image_uploaded=False)

        #5
        create_course_page.check_visible_create_course_form(
            title="", max_score="0", min_score="0", description="", estimated_time=""
        )
        #6
        create_course_page.check_visible_exercises_title()
        #7
        create_course_page.check_visible_create_exercise_button()
        #8
        create_course_page.check_visible_exercises_empty_view()
        #9
        create_course_page.upload_preview_image('/Users/timur/PycharmProjects/ui_test/testdata/files/image.jpg')
        #10
        create_course_page.check_visible_image_upload_view()
        #11
        create_course_page.fill_create_course_form(
            title="Playwright",
            estimated_time="2 weeks",
            description="Playwright",
            max_score="100",
            min_score="10"
        )
        #12
        create_course_page.click_create_course_button()
        #13
        course_list_page.check_visible_courses_title()
        course_list_page.check_visible_create_course_button()
        course_list_page.check_visible_course_card(
            index=0, title="Playwright", max_score="100", min_score="10", estimated_time="2 weeks"
        )

    @pytest.mark.courses
    @pytest.mark.regression
    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        courses_list_page.open("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        courses_list_page.navbar.check_visible('username')
        courses_list_page.sidebar.check_visible()

        courses_list_page.check_visible_courses_title()
        courses_list_page.check_visible_create_course_button()
        courses_list_page.check_visible_empty_view()

