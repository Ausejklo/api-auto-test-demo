import unittest
import requests
import time

# 简易接口自动化测试框架，测试公开免费JSON测试接口
class TestPublicApi(unittest.TestCase):
    base_url = "https://jsonplaceholder.typicode.com"

    @classmethod
    def setUpClass(cls):
        """所有用例执行前初始化"""
        cls.log_file = open("test_log.txt", "a", encoding="utf-8")
        cls.log_file.write(f"\n=====测试开始 {time.strftime('%Y-%m-%d %H:%M:%S')}=====\n")

    def write_log(self, content):
        self.log_file.write(f"{time.strftime('%H:%M:%S')} | {content}\n")

    def test_get_post_list(self):
        """用例1：GET获取帖子列表接口"""
        resp = requests.get(f"{self.base_url}/posts", timeout=10)
        self.write_log(f"GET /posts status_code:{resp.status_code}")
        self.assertEqual(resp.status_code, 200)
        self.assertGreater(len(resp.json()), 0)

    def test_get_single_post(self):
        """用例2：GET获取单条帖子，正常id"""
        resp = requests.get(f"{self.base_url}/posts/1", timeout=10)
        self.write_log(f"GET /posts/1 status_code:{resp.status_code}")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()["id"],1)

    def test_post_create(self):
        """用例3：POST新建资源接口"""
        body = {"title":"test_title","body":"test_body","userId":1}
        resp = requests.post(f"{self.base_url}/posts", json=body, timeout=10)
        self.write_log(f"POST /posts status_code:{resp.status_code}")
        self.assertEqual(resp.status_code,201)

    def test_404_case(self):
        """用例4：异常场景，不存在资源，断言404"""
        resp = requests.get(f"{self.base_url}/posts/99999", timeout=10)
        self.write_log(f"GET /posts/99999 status_code:{resp.status_code}")
        self.assertEqual(resp.status_code,404)

    @classmethod
    def tearDownClass(cls):
        """全部用例结束关闭日志"""
        cls.log_file.write(f"=====测试结束 {time.strftime('%Y-%m-%d %H:%M:%S')}=====\n")
        cls.log_file.close()

if __name__ == '__main__':
    unittest.main()
