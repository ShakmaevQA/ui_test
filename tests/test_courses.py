import pytest
from playwright.sync_api import Page, expect



class TestCourses:

    def test_empty_courses_list(self, chromium_page_with_state: Page):
        chromium_page_with_state.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

        courses_title = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
        expect(courses_title).to_be_visible()
        expect(courses_title).to_have_text('Courses')

        empty_icon_course = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
        expect(empty_icon_course).to_be_visible()

        empty_icon_title = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
        expect(empty_icon_title).to_be_visible()
        expect(empty_icon_title).to_have_text('There is no results')

        empty_icon_description = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
        expect(empty_icon_description).to_be_visible()
        expect(empty_icon_description).to_have_text('Results from the load test pipeline will be displayed here')
        