from time import sleep

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
def test_check_button_basket(browser):
    browser.get(link)
    sleep(30)
    assert browser.find_element_by_css_selector("button.btn.btn-lg.btn-primary.btn-add-to-basket"), 'button not found'