from pages.registeration_page import RegistrationUserPage
from pages.locators import HomePageLocators, RegisterationUserLocators
import allure


@allure.title('Регистрация нового пользователя')
def test_registration_new_user(browser, url, remove_user):
    client = RegistrationUserPage(browser)
    client.open(url=url)
    client.click_to_element(*HomePageLocators.MY_ACCOUNT)
    client.click_to_element(*HomePageLocators.CHECK_REGISTER)
    client.registration_user()
    client.waiting_for_text_present(*RegisterationUserLocators.SUCCESS_MESSAGE)
