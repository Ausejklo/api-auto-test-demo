# api-auto-test-demo
> Python + requests + unittest 简易接口自动化测试Demo
AI协作开发，面向软件测试方向。

## 项目功能
1. 对公开测试接口实现GET/POST请求自动化用例
2. 包含正常场景、异常404边界场景
3. 自动生成运行日志写入 test_log.txt
4. 使用unittest做断言校验响应码、返回数据

## 环境依赖
pip install -r requirements.txt

## 运行方式
python test_api.py

## AI协作说明
- 使用Cursor做代码生成、调试排错
- DeepSeek‑V3协助设计测试用例、梳理异常边界
- 本人负责：测试点设计、接口校验逻辑审查、优化日志输出，修正AI生成代码的逻辑缺陷。
