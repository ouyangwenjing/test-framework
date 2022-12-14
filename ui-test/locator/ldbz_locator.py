# 领导班子Tab页元素定位
class LdbzLocator:
    # 领导班子tab元素定位
    ldbz_tab = '//div[text()="领导班子"]'
    # 新增换届按钮元素定位
    hjxx_create = '//*[@id="pane-ldbz"]/div[1]/div[1]/button/span[contains(text(),"新增换届")]'

    # 换届信息届数元素
    hjxx_js = '//*[@placeholder="填写领导班子届数"]'
    # 换届信息任职年限元素
    hjxx_rznx = '//*[@placeholder="选择任职年限"]'
    # 任职年限3年元素
    rznx_1 = '//span[text()="3年"]'
    # 换届信息换届日期元素
    hjxx_hjrq = '//*[@placeholder="选择换届日期"]'
    # 换届日期当前月17号元素
    hjrq_1 = '//span[contains(text(), " 17")]'
    # 换届信息换届形式元素
    hjxx_hjxs = '//*[@placeholder="选择换届形式"]'
    # 换届形式党员大会元素
    hjxs_1 = '//span[text()="党员大会"]'
    # 新增换届确定按钮
    qd_button = '//*[@id="pane-ldbz"]/div/div[2]/div/div[3]/div/button[2]/span'
    # 新增换届取消按钮
    qx_button = '//*[@id="pane-ldbz"]/div/div[2]/div/div[3]/div/button[1]/span'

    # 新增换届提示弹窗
    hjxx_alert_p = '//div[@role="alert"]/p'
    # 新增换届后端返回msg提示
    hjxx_alert_h2 = '//div[@role="alert"]//h2'

    #删除换届信息按钮
    hjxx_deleted = '//*[@id="pane-ldbz"]/div/div[1]/div[1]/div[4]/div[2]/table/tbody/tr/td[7]/div/button[2]/span'
    #删除换届信息-弹窗确定按钮
    hjxx_deleted_confirm = '//div[@class="el-message-box__btns"]/button/span[contains(text(),"确定")]'




