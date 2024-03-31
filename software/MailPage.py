import pytest
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from Base import BasePage
from allure import step
import time


class MailPageLocators:

    @staticmethod
    def check_the_success_of_sending_letter(mail=None):
        text = f"Сообщение не доставлено, так как адрес {mail} не найден или не принимает входящие письма."
        return f'//*[contains(text(), f"{text}"'

    LOCATOR_LOGIN_OR_PHONE_INPUT = (By.CSS_SELECTOR, 'input[type="email"][name="identifier"]')
    LOCATOR_NEXT_BUTTON = (By.XPATH, '//span[contains(text(), "Далее")]')  # тест проводился на рус.локали. При
    # небходимости могу заменить xpath на поиск по CSS
    LOCATOR_PASSWORD_INPUT = (By.XPATH, '//span[contains(text(), "Введите пароль")]')
    LOCATOR_BUTTON_EXCEPTION_TRYING = (By.XPATH, '//span[contains(text(), "Повторить попытку")]')
    LOCATOR_BUTTON_EXCEPTION_NOT_NOW = (By.XPATH, '//span[contains(text(), "Не сейчас")]')
    LOCATOR_CALL_MENU_TO_SEND_LETTER = (By.CSS_SELECTOR, '.T-I.T-I-KE.L3')
    LOCATOR_AREA_TO_CONSUMER_MAIL_INPUT = (By.CSS_SELECTOR, '.agP.aFw:nth-child(1)[id=":wq"]')
    LOCATOR_AREA_LETTER_SUBJECT = (By.CSS_SELECTOR, 'input[name="subjectbox"][id=":z6"]')
    LOCATOR_AREA_LETTER_PAYLOAD = (By.CSS_SELECTOR, '.Am.aiL.Al.editable.LW-avf.tS-tW[id=":ok"]')
    LOCATOR_ATTACHMENT_BUTTON = (By.CSS_SELECTOR, '(//input[@type="file"])[3]')
    LOCATOR_SEND_LETTER_BUTTON = (By.CSS_SELECTOR, '(.T-I.J-J5-Ji.aoO.v7.T-I-atl.L3[id=":qn"]')
    LOCATOR_ATTACHED_ELEMENT = (By.CSS_SELECTOR, '[id=":1cv"]')
    LOCATOR_TEXT_IF_EXCEPTION_WITH_MAIL = (By.XPATH, check_the_success_of_sending_letter())


class MailPageActions(BasePage):

    @step('Ввод почты или телефона')
    def input_login_or_phone(self, login_or_phone):
        try:
            input_element = self.find_element(MailPageLocators.LOCATOR_LOGIN_OR_PHONE_INPUT)
            input_element.send_keys(login_or_phone)
        except NoSuchElementException as e:
            print(f"Не найдено поле ввода почты или номер телефона: {e}")
        except ElementNotInteractableException as e:
            print(f"Поле ввода почты или телефона недоступно для ввода {e}")

    @step('Нажать кнопку "Далее"')
    def click_to_next_button(self):
        return self.find_element(MailPageLocators.LOCATOR_NEXT_BUTTON).click()

    @step('Ввод пароля')
    def input_password(self, password):
        return self.find_element(MailPageLocators.LOCATOR_PASSWORD_INPUT).send_keys(f'{password}')

    @step('Нажать "Повторить попытку"')
    def click_if_exception_try(self):
        return self.find_element(MailPageLocators.LOCATOR_BUTTON_EXCEPTION_TRYING).click()

    @step('Нажать "Не сейчас"')
    def click_if_exception_not_now_button(self):
        with pytest.raises(NoSuchElementException):
            button_element = self.find_element(MailPageLocators.LOCATOR_BUTTON_EXCEPTION_NOT_NOW)
            button_element.click()  # Элемент не всегда появлялся, поэтому пришлось добавить исключение

    @step('Нажать "Отправить письмо"')
    def click_to_send_letter(self):
        return self.find_element(MailPageLocators.LOCATOR_CALL_MENU_TO_SEND_LETTER).click()

    @step('Ввод список получателей')
    def input_mails_of_consumers(self, list_of_mails=None):
        return self.find_element(MailPageLocators.LOCATOR_AREA_TO_CONSUMER_MAIL_INPUT).send_keys(list_of_mails)

    @step('Ввод темы письма')
    def input_subject(self, payload=None):
        return self.find_element(MailPageLocators.LOCATOR_AREA_LETTER_SUBJECT).send_keys(payload)

    @step('Ввод текста письма')
    def input_letter_text(self, payload=None):
        return self.find_element(MailPageLocators.LOCATOR_AREA_LETTER_PAYLOAD).send_keys(payload)

    @step('Приложить файл')
    def send_attachment(self, file_path=None):
        if file_path is None: file_path = r'software/artifacts/cat.jpg'
        return self.find_element(MailPageLocators.LOCATOR_ATTACHMENT_BUTTON).send_keys(file_path)

    @step('Отправить письмо')
    def send_the_letter_finally(self):
        return self.find_element(MailPageLocators.LOCATOR_SEND_LETTER_BUTTON).click()

    @step('Поиск приложенных файлов в письме')
    def get_attached_element(self):
        return self.find_element(MailPageLocators.LOCATOR_ATTACHED_ELEMENT)

    @step('Три попытки найти уведомление об отправке на несуществующий email')
    def try_to_find_alert_about_failed_send(self, mail=None):
        max_retry = 3
        for attempt in range(max_retry):
            try:
                element = self.find_element(MailPageLocators.check_the_success_of_sending_letter(mail))
                return element
            except NoSuchElementException:
                print("Уведомление не было найдено")
                time.sleep(2)  # т.к. соединение может быть неустойчивым, ожидание приходится делать явным
        print("Уведомлений о неудачной отправке нет")
        return None
