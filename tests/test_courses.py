import pytest
from pages.course_list_page import CourseListPage
from pages.create_course_page import CreateCoursePage

class TestCourses:


    @pytest.mark.courses
    @pytest.mark.regression
    def test_create_course(self, course_list_page_with_state: CourseListPage, create_course_page_with_state: CreateCoursePage):
        create_course_page_with_state.open('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')
        #1
        create_course_page_with_state.check_visible_create_course_title()
        create_course_page_with_state.check_visible_create_course_button()
        #2
        create_course_page_with_state.check_disabled_create_course_button()
        #3
        create_course_page_with_state.check_visible_image_preview_empty_view()
        #4
        create_course_page_with_state.check_visible_image_upload_view(is_image_uploaded=False)

        #5
        create_course_page_with_state.check_visible_create_course_form(
            title="", max_score="0", min_score="0", description="", estimated_time=""
        )
        #6
        create_course_page_with_state.check_visible_exercises_title()
        #7
        create_course_page_with_state.check_visible_create_exercise_button()
        #8
        create_course_page_with_state.check_visible_exercises_empty_view()
        #9
        create_course_page_with_state.upload_preview_image('/Users/timur/PycharmProjects/ui_test/testdata/files/image.jpg')
        #10
        create_course_page_with_state.check_visible_image_upload_view()
        #11
        create_course_page_with_state.fill_create_course_form(
            title="Playwright",
            estimated_time="2 weeks",
            description="Playwright",
            max_score="100",
            min_score="10"
        )
        #12
        create_course_page_with_state.click_create_course_button()
        #13
        course_list_page_with_state.check_visible_courses_title()
        course_list_page_with_state.check_visible_create_course_button()
        course_list_page_with_state.course_view.check_visible(
            index=0, title="Playwright", max_score="100", min_score="10", estimated_time="2 weeks"
        )

    @pytest.mark.courses
    @pytest.mark.regression
    def test_empty_courses_list(self, course_list_page_with_state: CourseListPage):
        course_list_page_with_state.open("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        course_list_page_with_state.navbar.check_visible('username')
        course_list_page_with_state.sidebar.check_visible()

        course_list_page_with_state.check_visible_courses_title()
        course_list_page_with_state.check_visible_create_course_button()
        course_list_page_with_state.check_visible_empty_view()

