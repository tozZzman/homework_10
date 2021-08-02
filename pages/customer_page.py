from .base_page import BasePage
from .locators import CustomersPageLocators
from selenium.webdriver.common.by import By
import allure


class CustomersPage(BasePage):
    @allure.step('Удаление продавца')
    def remove_customer(self, name):
        self.click_to_element(By.XPATH, CustomersPageLocators.CHECKBOX_PRODUCT.format(name))
        self.click_to_element(*CustomersPageLocators.DEL_BUTTON)
        self.browser.switch_to_alert().accept()
        self.waiting_for_text_present(By.CSS_SELECTOR, CustomersPageLocators.SUCCESS_MESSAGE,
                                      text='Success: You have modified customers!')
