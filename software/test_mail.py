import allure
from MailPage import MailPageActions

SUBJ_PAYLOAD = 'Кот'
LETTER_TEXT_PAYLOAD = 'Коллеги, привет, посмотрите на кота'
FAKE_URL_BEFORE_START_TEST = 'www.google.com/'


@allure.feature('GOOGLE')
@allure.story('Авторизация на почтовом сервере и рассылка писем')
def test_mail_server(browser, env):
    with allure.step("Инициализация страницы почты"):
        mail_steps = MailPageActions(browser)
        mail_steps.go_to_site(url=mail_steps.fake_url)
        mail_steps.go_to_site(url=mail_steps.base_url)

    with allure.step("Авторизация"):
        get_current_page = mail_steps.get_page_status_code(browser.current_url)
        mail_steps.input_login_or_phone(login_or_phone=env.login)
        mail_steps.assertions.assertion_status_code(get_current_page, 200)
        mail_steps.click_to_next_button()
        mail_steps.input_password(password=env.password)
        mail_steps.click_to_next_button()
        mail_steps.click_if_exception_not_now_button()
    # exception button here. Проблема теста кроется здесь. Гугл возвращает ошибку с подозрением на безопасность

    # here code to accept mail by smartphone. Гугл просит подтвердить действия с мобильного телефона. Я думаю, из-за
    # Отсутствия полной тестовой инфраструктуры - тест обречен на провал. Дальнейшие действия я писал, если бы это
    # используя свою Личную УЗ, я ее не могу предоставить в ТЗ, к сожалению.

    with allure.step("Отправка письма"):
        consumers_list = [env.consumer_1_real, env.consumer_2_fake]
        mail_steps.input_mails_of_consumers(list_of_mails=consumers_list)
        mail_steps.input_subject(payload=SUBJ_PAYLOAD)
        mail_steps.input_letter_text(payload=LETTER_TEXT_PAYLOAD)
        mail_steps.send_attachment()
        mail_steps.assertions.element_is_visible(mail_steps.get_attached_element())
        mail_steps.click_to_send_letter()

    with allure.step("Проверка успешности отправки писем"):
        mail_steps.try_to_find_alert_about_failed_send(mail=env.consumer_1_real)
        mail_steps.try_to_find_alert_about_failed_send(mail=env.consumer_2_fake)

