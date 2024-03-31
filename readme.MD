Этот тест работает только, если заменить тестовые данные на реальные (config.py). Реальных данных я не генерировал, т.к. для авторизации в гугл необходимо добавлять номер телефона. 
+ Есть некоторая проблема в виде перехвата запросов гуглом и блокировка теста за "небезопасностью браузера". К сожалению, не хватило времени решить данную проблему.


**for allure report:**
0. (FOR_WINDOWS) **JAVA_HOME** in env_variable ((**JAVA 8**), setx JAVA_HOME <"path_to_java.exe">) ; **Scoop** (
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser ;
Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression
) ; **allure** ( scoop install allure ) ; **nodejs** (scoop install nodejs )

1.Запуск тестов с генерацией отчета: pytest -s -v /software/test_mail.py --alluredir=software/allure-reports
2.Запуск сервера с отчетом: allure serve allure-reports
