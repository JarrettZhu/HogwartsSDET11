from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestWework:
    """
    企业微信添加新成员
    todo：暂时未实现绕过登录功能，所以需要以Debugging模式启动chrome，登录后，用例直接复用已登录的浏览器进行操作
    需要从命令行启动chrome，并在后面加上 "--remote-debugging-port=9222"参数
    """
    def setup_method(self):
        # 添加浏览器启动参数
        options = webdriver.ChromeOptions()
        # 设置debug监听地址为本机9222端口
        options.debugger_address = '127.0.0.1:9222'
        # 实例化chrome对象
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.implicitly_wait(5)

    def wait(self, timeout, method) -> None:
        """
        封装显式等待方法
        :param timeout: 超时时间，单位：秒
        :param method: 等待方法
        :return: None
        """
        WebDriverWait(self.driver, timeout).until(method)

    def test_addsomeon(self):
        # 姓名输入框
        name_input_text = (By.CSS_SELECTOR, '.ww_compatibleTxt #username')
        # 别名输入框
        smallname_input_text = (By.CSS_SELECTOR, '.ww_compatibleTxt #memberAdd_english_name')
        # 账号输入框
        useraccount_input_text = (By.CSS_SELECTOR, '#memberAdd_acctid')
        # 性别-男-选择框
        sex_male_select = (By.CSS_SELECTOR, '.member_edit_sec:nth-child(1) .ww_label:nth-child(1) > .ww_radio')
        # 性别-女-选择框
        sex_female_select = (By.CSS_SELECTOR, '.member_edit_sec:nth-child(1) .ww_label:nth-child(2) > .ww_radio')
        # 手机区号下拉按钮
        # mobile_area_button = (By.CSS_SELECTOR, '.ww_telInput_zipCode_input .ww_telInput_zipCode_input_arrowWrap')
        # 手机区号框
        mobile_area_code = (By.CSS_SELECTOR, '.ww_telInput_zipCode_input > .qui_inputText')
        # 具体手机区号：中国 86
        mobile_area_code_china = (By.CSS_SELECTOR, '[data-value="86"]')
        # 手机号码输入框
        mobile_number_input_text = (By.CSS_SELECTOR, '.qui_inputText.ww_inputText.ww_telInput_mainNumber')
        # 部门修改按钮
        department_change_button = (By.CSS_SELECTOR, '.ww_groupSelBtn_add.js_show_party_selector')
        # 部门修改页面确认按钮
        department_change_page_confirm_button = (By.CSS_SELECTOR, '.qui_btn.ww_btn.ww_btn_Blue.js_submit')
        # 职务输入框
        position_input_text = (By.CSS_SELECTOR, '.member_edit_item_right #memberAdd_title')
        # 底部确认按钮
        final_confirm_button = (By.CSS_SELECTOR, '.member_colRight_operationBar:nth-child(3) > .ww_btn_Blue')
        self.driver.find_element(By.CSS_SELECTOR, '#main .index_service_cnt_itemWrap:nth-child(1)').click()
        self.driver.find_element(*name_input_text).send_keys("李家志")
        self.driver.find_element(*smallname_input_text).send_keys("骚B志")
        self.driver.find_element(*useraccount_input_text).send_keys("tester01")
        self.driver.find_element(*sex_female_select).click()
        self.driver.find_element(*mobile_area_code).click()
        self.driver.find_element(*mobile_area_code_china).click()
        self.driver.find_element(*mobile_number_input_text).send_keys('13342852851')
        self.driver.find_element(*department_change_button).click()
        self.wait(10, expected_conditions.visibility_of_element_located(department_change_page_confirm_button))
        # 加5秒死等查看效果
        sleep(5)
        self.driver.find_element(*department_change_page_confirm_button).click()
        self.driver.find_element(*position_input_text).send_keys('测试')
        self.driver.find_element(*final_confirm_button).click()

    def teardown_method(self):
        sleep(5)
        self.driver.quit()
