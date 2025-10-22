from selene import browser
from selene import be, have, command
from pathlib import Path

class RegistrationPage:
    def __init__(self):
        self.resources_path = Path(__file__).parents[1] / 'resources'

    def open(self):
        browser.open('/automation-practice-form')
        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")
        return self

    @property
    def should_registered_user_with(self):
        return browser.element('.table').all('td').even

    def get_modal_popup(self):
        return browser.element('.modal-title')

    def fill_firstname(self, value):
        browser.element('#firstName').should(be.visible).type(value)
        return self

    def fill_lastname(self, value):
        browser.element('#lastName').should(be.visible).type(value)
        return self

    def fill_useremail(self, value):
        browser.element('#userEmail').should(be.visible).type(value)
        return self

    def select_gender(self, value):
        variants = {'Male': '1', 'Female': '2', 'Other': '3'}
        browser.element(f'[for="gender-radio-{variants[value]}"]').click()
        return self

    def fill_user_phone_number(self, value):
        browser.element('#userNumber').type(value)
        return self

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click()
        browser.all('.react-datepicker__month-select option').element_by(have.exact_text(month)).click()
        browser.element('.react-datepicker__year-select').click()
        browser.all('.react-datepicker__year-select option').element_by(have.exact_text(year)).click()
        browser.element(f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)').click()
        return self

    def select_subject(self, value):
        browser.element('#subjectsInput').type(value).press_enter()
        return self

    def select_hobby(self, value):
        mapping = {'Sports': '1', 'Reading': '2', 'Music': '3'}
        browser.element(f'[for="hobbies-checkbox-{mapping[value]}"]').click()
        return self

    def upload_file(self, filename):
        file_path = self.resources_path / filename
        browser.element('#uploadPicture').set_value(str(file_path))
        return self

    def fill_current_address(self, value):
        browser.element('#currentAddress').type(value)
        return self

    def select_state(self, value):
        browser.element('#state').perform(command.js.scroll_into_view).click()
        browser.all('[id^="react-select-3-option-"]').element_by(have.exact_text(value)).click()
        return self

    def select_city(self, value):
        browser.element('#city').click()
        browser.all('[id^="react-select-4-option-"]').element_by(have.exact_text(value)).click()
        return self

    def click_submit_button(self):
        browser.element('#submit').perform(command.js.click)
        return self