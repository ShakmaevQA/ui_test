from operator import index

from playwright.sync_api import Page
from pages.base_page import BasePage

class CreateCoursesPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        # Заголовок панели инструментов и кнопка создания курса
        self.create_course_title = page.get_by_test_id('create-course-toolbar-title-text')
        self.create_course_button = page.get_by_test_id('create-course-toolbar-create-course-button')

        # Пустое состояние превью курса, предварительное отображение превью курса
        self.preview_image_view_icon = page.get_by_test_id('create-course-preview-empty-view-icon')
        self.preview_image_view_title = page.get_by_test_id('create-course-preview-empty-view-title-text')
        self.preview_image_view_description = page.get_by_test_id('create-course-preview-empty-view-description-text')
        self.preview_image = page.get_by_test_id('create-course-preview-image-upload-widget-preview-image')


        # Кнопка загрузки изобразения, кнопка удаления изображения, блок с информацией о загружаемой картинке
        self.preview_image_upload_button = page.get_by_test_id('')
        self.preview_image_remove_button = page.get_by_test_id('')
        self.preview_image_upload_icon = page.get_by_test_id('')
        self.preview_image_upload_title = page.get_by_test_id('')
        self.preview_image_upload_description = page.get_by_test_id('')

        # Поля для заполнения: Title, Estimated time, Description, Max score, Min score
        self.create_course_title_input = page.get_by_test_id('create-course-form-title-input').locator('input')
        self.create_course_estimated_input = page.get_by_test_id('create-course-form-estimated-time-input').locator('input')
        self.create_course_description_input = page.get_by_test_id('create-course-form-description-input').locator('input')
        self.create_course_max_score = page.get_by_test_id('create-course-form-max-score-input').locator('input')
        self.create_course_min_score = page.get_by_test_id('create-course-form-min-score-input').locator('input')

        # Заголовок, кнопка создания задания, кнопка удаления задания
        self.create_exercises_title = page.get_by_test_id('create-course-exercises-box-toolbar-title-text')
        self.create_exercises_button = page.get_by_test_id('create-course-exercises-box-toolbar-create-exercise-button')
        self.create_exercises_delete_button = page.get_by_test_id('create-course-exercise-0-box-toolbar-delete-exercise-button')

        # Пустое состояние блока создания заказа
        self.exercises_empty_view_icon = page.get_by_test_id('create-course-exercises-empty-view-icon')
        self.exercises_empty_view_title = page.get_by_test_id('create-course-exercises-empty-view-title-text')

