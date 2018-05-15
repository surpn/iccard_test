from time import sleep

from common.runner import TestRunner
from common.sendemail import sendemail
from common.utils import newest_file

# 加载测试用例
run = TestRunner(test_dir="test_case/test_interface", title="iccard_test", description="test")
run.run()
sleep(1)
# 发送邮件
mail_file = newest_file("result/report")
print(mail_file)
sendemail(subject="iccard_test", context="test", mail_file=mail_file)
