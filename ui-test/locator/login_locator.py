# 登录界面元素定位
class LoginLocator:
    # 账号元素定位
    username_input = "//*[@id='app']/div[1]/div[2]/div/div/div[2]/form/div[1]/div[1]/div/div/input"
    # 密码元素定位
    password_input = "//*[@id='app']/div[1]/div[2]/div/div/div[2]/form/div[1]/div[2]/div/div/input"
    # 验证码元素定位
    code_input = "//*[@id='app']/div[1]/div[2]/div/div/div[2]/form/div[1]/div[3]/div/div[1]/input"
    # 登录按钮定位
    login_btn = "//*[@id='app']/div[1]/div[2]/div/div/div[2]/form/div[2]/div/button"
    # 错误提示定位
    err_alert = "//div[@role='alert']/p"
    # 必填项校验提醒
    required_text = "//div[@class='el-form-item__error']"

