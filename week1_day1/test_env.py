import sys
import numpy as np
import torch

# 打印Python解释器路径（确认是VLA环境）
print("Python路径：", sys.executable)
# 打印包版本（确认安装成功）
print("NumPy版本：", np.__version__)
print("PyTorch版本：", torch.__version__)
print("VLA环境配置成功！")