#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from common.browser_common import BrowserCommon


# Page 项目无关页面类封装基本页面操作
class PageCommon(BrowserCommon):

    ############################## 基本方法再封装 ##############################
    # 依据 xpath 找到指定元素
    def find_element_by_xpath(self, xpath):
        """
        通过 xpath 找元素
        :param xpath: 元素定位
        :return: 原生通过 xpath 找元素方法
        """
        return self.driver.find_element_by_xpath(xpath)

    # 找到指定元素
    def find_element(self, *args):
        """
        找元素
        :param args: 定位与通过什么定位
        :return: 原生找元素方法
        """
        return self.driver.find_element(*args)

    # 依据 xpath 找到指定的一批元素
    def find_elements_by_xpath(self, xpath):
        """
        通过 xpath 找多元素
        :param xpath: 多元素定位
        :return: 原生通过 xpath 找多元素方法
        """
        return self.driver.find_elements_by_xpath(xpath)

    # 找到指定的一批元素
    def find_elements(self, *args):
        """
        找多元素
        :param args: 定位与通过什么定位
        :return: 原生找多元素方法
        """
        return self.driver.find_elements(*args)

    ############################## 单个元素操作 ##############################
    # 点击元素
    def click_element(self, xpath):
        """
        点击元素
        :param xpath: 元素定位
        :return: 返回原生点击事件
        """
        # 显示等待元素可点击
        WebDriverWait(self.driver, 10, 0.1).until(expected_conditions.element_to_be_clickable(("xpath", xpath)))
        # # 点击元素
        self.driver.find_element(By.XPATH, xpath).click()
        # element = self.driver.find_element(By.XPATH, xpath)
        # self.driver.execute_script("arguments[0].click();", element)

    # 输入框输入数据
    def input(self, xpath, value):
        """
        输入值
        :param xpath: 元素定位
        :param value: 输入值
        :return: 返回 send_keys 原生方法
        """
        # 显示等待元素可点击
        WebDriverWait(self.driver, 10, 0.1).until(expected_conditions.element_to_be_clickable(("xpath", xpath)))
        # 输入框输入数据
        self.driver.find_element(By.XPATH, xpath).send_keys(value)

    def clear(self, xpath):
        # 清空输入框
        self.driver.find_element(By.XPATH, xpath).clear()

    def locator_element(self, loc):
        # 定位元素
        return self.driver.find_element(loc)

    # 获取弹窗提示text
    def alert_text(self, xpath):
        return self.find_element(By.XPATH, xpath).text

    def isElementPresent(self, by, value):
        try:
            self.driver.find_element(by=by, value=value)
        except NoSuchElementException:
            # 打印异常信息
            print(NoSuchElementException)
            # 发生异常，说明页面中未找到该元素，返回False
            return False
        else:
            # 无异常，说明在页面中找到了该元素，返回True
            return True
