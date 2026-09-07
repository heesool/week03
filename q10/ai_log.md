核心提示：要求空白 name 以 SystemExit(2) 结束，保持正常功能，不修改测试，并运行 unittest。

智能体改动：在 cli.py 中增加参数类型检查，name 为空白时抛出 argparse.ArgumentTypeError。

人工检查：检查 diff，确认仅修改实现所需代码，测试文件未修改。

再次验证：重新运行测试，所有测试通过。

