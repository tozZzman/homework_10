from .base_page import BasePage
from .locators import RegisterationUserLocators
import allure


class RegistrationUserPage(BasePage):
    @allure.step('Регистрация нового пользователя')
    def registration_user(self):
        self.logger.info('Регистрация нового пользователя')
        self.enter_text(*RegisterationUserLocators.FIRST_NAME, text=RegisterationUserLocators.NAME)
        self.enter_text(*RegisterationUserLocators.LAST_NAME, text=RegisterationUserLocators.NAME)
        self.enter_text(*RegisterationUserLocators.EMAIL,
                        text=RegisterationUserLocators.NAME[:8] + '@' + RegisterationUserLocators.NAME[:8] + '.com')
        self.enter_text(*RegisterationUserLocators.TELEPHONE, text='89996669999')
        self.enter_text(*RegisterationUserLocators.PASSWORD, text=RegisterationUserLocators.PASS)
        self.enter_text(*RegisterationUserLocators.PASSWORD_CONFIRM, text=RegisterationUserLocators.PASS)
        self.click_to_element(*RegisterationUserLocators.PRIVACY)
        self.click_to_element(*RegisterationUserLocators.CONTINUE_BUTTON)
