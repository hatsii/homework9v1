import os
import sys

from Pages.registration_page import RegistrationPage
from Data.user import test_user

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

def test_form_filling(open_registration_page):
    registration_form = RegistrationPage()

    registration_form.reg_user_form(test_user)
    registration_form.click_submit_button()
    registration_form.assert_info_user(test_user)