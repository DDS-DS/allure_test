# 时间 2020/12/7 21:02
import pytest,allure

class Test_Abc:
    @allure.step(title='第一个测试')
    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    def test_001(self):
        allure.attach("这是一个描述","试一下")
        assert 1

    @allure.issue('http://www.baidu.com')
    @pytest.allure.testcase("http://www.baidu.com/test_001")
    @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    def test_002(self):
        allure.attach("这是第二个描述",'....')
        assert 0

