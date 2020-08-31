from selenium import webdriver
import time


def visit_shimo():
    try:
        browser = webdriver.Chrome()

        browser.get('https://shimo.im')
        time.sleep(1)
        browser.maximize_window()
        time.sleep(1)

        btm1 = browser.find_element_by_xpath('//*[@id="homepage-header"]/nav/div[3]/a[2]/button')
        btm1.click()
        time.sleep(1)

        browser.find_element_by_name('mobileOrEmail').send_keys('test_298121@163.com')
        browser.find_element_by_name('password').send_keys('98123081082')
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="root"]//button').click()
        time.sleep(1)

        cookies = browser.get_cookies()
        print(cookies)
        time.sleep(3)

    except Exception as e:
        print(e)
    finally:
        browser.close()


if __name__ == '__main__':
    visit_shimo()