from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class CoursesListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        # Заголовок и кнопка добавления курса
        self.courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
        self.create_courses_button = page.get_by_test_id('courses-list-toolbar-create-course-button')

        # Пустой блок при отсутствии курсов
        self.empty_view_icon = page.get_by_test_id('courses-list-empty-view-icon')
        self.empty_view_title = page.get_by_test_id('courses-list-empty-view-title-text')
        self.empty_view_description = page.get_by_test_id('courses-list-empty-view-description-text')

        # Карточка курса
        self.courses_widget_title = page.get_by_test_id('course-widget-title-text')
        self.courses_preview_title = page.get_by_test_id('course-preview-image')
        self.courses_max_score_text = page.get_by_test_id('course-max-score-info-row-view-text')
        self.courses_min_score_text = page.get_by_test_id('course-min-score-info-row-view-text')
        self.courses_estimated_time = page.get_by_test_id('course-estimated-time-info-row-view-text')

        # Кнопка редактирования карточки курса и выпадающий список
        self.courses_view_menu_button = page.get_by_test_id('course-view-menu-button')
        self.courses_edit_button = page.get_by_test_id('course-view-edit-menu-item')
        self.courses_delete_button = page.get_by_test_id('course-view-delete-menu-item')

    def check_visible_title(self):
        expect(self.courses_title).to_be_visible()
        expect(self.courses_title).to_have_text('Courses')

    def check_visible_empty_view(self):
        expect(self.empty_view_icon).to_be_visible()

        expect(self.empty_view_title).to_be_visible()
        expect(self.empty_view_title).to_have_text('There is no results')

        expect(self.empty_view_description).to_be_visible()
        expect(self.empty_view_description).to_have_text('Results from the load test pipeline will be displayed here')


    def check_visible_courses_title(self,
                                    index: int,
                                    title: str,
                                    max_score: str,
                                    min_score: str,
                                    estimated_time: str):

        expect(self.courses_title.nth(index)).to_be_visible()
        expect(self.courses_title.nth(index)).to_have_text(title)

        expect(self.courses_max_score_text.nth(index)).to_be_visible()
        expect(self.courses_max_score_text.nth(index)).to_have_text(f'Max score: {max_score}')

        expect(self.courses_min_score_text.nth(index)).to_be_visible()
        expect(self.courses_min_score_text.nth(index)).to_have_text(f'Min score: {min_score}')

        expect(self.courses_estimated_time.nth(index)).to_be_visible()
        expect(self.courses_estimated_time.nth(index)).to_have_text(f'Estimated time: {estimated_time}')


    def check_visible_menu_button(self, index: int):
        expect(self.courses_view_menu_button.nth(index)).to_be_visible()

    def click_courses_view_menu_button(self, index: int):
        self.courses_view_menu_button.nth(index).click()

    def check_courses_edit_button(self, index: int):
        expect(self.courses_edit_button.nth(index)).to_be_visible()

    def click_courses_edit_button(self, index: int):
        self.courses_edit_button.nth(index).click()

    def check_courses_delete_button(self, index: int):
        expect(self.courses_delete_button.nth(index)).to_be_visible()

    def click_courses_delete_button(self, index: int):
        self.courses_delete_button.nth(index).click()










