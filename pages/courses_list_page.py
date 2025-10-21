from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class CoursesListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
        self.create_courses_button = page.get_by_test_id('courses-list-toolbar-create-course-button')

        self.empty_view_icon = page.get_by_test_id('courses-list-empty-view-icon')
        self.empty_view_title = page.get_by_test_id('courses-list-empty-view-title-text')
        self.empty_view_description = page.get_by_test_id('courses-list-empty-view-description-text')

    def check_visible_title(self):
        expect(self.courses_title).to_be_visible()
        expect(self.courses_title).to_have_text('Courses')

    def check_visible_courses_button(self):
        expect(self.courses_title).to_be_visible()

    def click_create_course_button(self):
        self.create_courses_button.click()

    def check_visible_empty_view_icon(self):
        expect(self.empty_view_icon).to_be_visible()

    def check_visible_empty_view_title(self):
        expect(self.empty_view_title).to_be_visible()
        expect(self.empty_view_title).to_have_text('There is no results')

    def check_visible_empty_view_description(self):
        expect(self.empty_view_description).to_be_visible()
        expect(self.empty_view_description).to_have_text('Results from the load test pipeline will be displayed here')


    



