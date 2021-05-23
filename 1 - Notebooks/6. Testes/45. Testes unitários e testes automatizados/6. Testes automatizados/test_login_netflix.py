from selenium import webdriver
import time

@Test
public void login() throws Exception {
    browser = webdriver.Firefox()
    brower.get("https://www.netflix.com/br/login")
    time.sleep(10)
    username = browser.find_element_by_id("id_userLoginId")
    password = browser.find_element_by_id("id_password")
    username.sendKeys("usuarioNovo")
    password.senKeys("987654321")
    login_btn = browser.find_element_class_name("login_button")
    login_btn.submit()
    time.sleep(10)
    assert "Netflix" in driver.title
}
