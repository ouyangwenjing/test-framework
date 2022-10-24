# 菜单栏元素定位
class DzzLocator:
    # 组织管理元素定位
    org_menu = "//*[@id='app']/div/div[1]/div[2]/div[1]/div/ul/div[3]/li//span[text()='组织管理']"
    # 党组织管理元素定位
    dzz_menu = "//*[@id='app']/div/div[1]/div[2]/div[1]/div/ul/div[3]/li/ul/div/a/li/span[text()='党组织管理']"
    # 搜索党组织元素定位
    dzz_search = "//*[@id='app']/div[1]/div[2]/section/div/div/div[1]/div[1]/div/input"
    # 党组织搜索结果元素定位
    dzz_search_result = "/html/body/div[3]/div[1]/div[1]/ul/li[1]"
    # 党组织列表页中党组织名称元素定位
    result_dzz_name = "//*[@id='app']/div/div[2]/section/div/div/div[2]/div[2]/div[3]/table/tbody/tr/td[3]/div/span"

