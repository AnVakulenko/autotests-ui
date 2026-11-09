from playwright.sync_api import sync_playwright, expect
import pytest

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state):
        page = chromium_page_with_state

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        test_text = page.get_by_test_id('courses-list-toolbar-title-text')
        expect(test_text).to_be_visible()
        expect(test_text).to_have_text('Courses')

        test_text = page.get_by_test_id('courses-list-empty-view-title-text')
        expect(test_text).to_be_visible()
        expect(test_text).to_have_text('There is no results')
