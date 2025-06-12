# LeetCode 练习项目

这个项目包含了使用Java、C++和Python解决LeetCode题目的代码和环境配置。项目结构设计为支持多种编程语言，方便进行算法练习和比较不同语言的实现方式。

## 项目结构

```
leetcode/
├── java/              # Java 解决方案
│   ├── pom.xml        # Maven 配置文件
│   └── src/           # Java 源代码
│       └── TwoSum.java
├── cpp/               # C++ 解决方案
│   ├── CMakeLists.txt # CMake 配置文件
│   └── src/           # C++ 源代码
│       └── two_sum.cpp
├── python/            # Python 解决方案
│   ├── requirements.txt # Python 依赖
│   └── src/           # Python 源代码
│       ├── two_sum.py
│       └── test_two_sum.py
└── README.md          # 项目说明
```

## 环境配置

### Java 环境

需要安装 JDK 11 或更高版本和 Maven。

```bash
# 编译 Java 代码
cd java
mvn compile

# 运行特定的类
mvn exec:java -Dexec.mainClass="TwoSum"

# 运行测试（如果有）
mvn test
```

### C++ 环境

需要安装 CMake 和 C++ 编译器（如 GCC 或 Clang）。

```bash
# 创建构建目录并配置
cd cpp
mkdir -p build && cd build
cmake ..

# 编译
make

# 运行特定的可执行文件
./two_sum
```

### Python 环境

建议使用虚拟环境。

```bash
# 创建并激活虚拟环境
cd python
python3 -m venv venv  # 在Linux系统上使用python3
# 或 python -m venv venv  # 在Windows或已配置python命令的系统上
source venv/bin/activate  # Linux/Mac
# 或 venv\Scripts\activate  # Windows

# 安装依赖
pip install -r requirements.txt

# 运行 Python 代码
python src/two_sum.py

# 运行测试
python -m unittest src/test_two_sum.py
# 或使用 pytest
pytest src/test_two_sum.py
```

## 添加新的解决方案

### Java

1. 在 `java/src` 目录下创建新的 Java 类文件
2. 实现解决方案和测试代码

### C++

1. 在 `cpp/src` 目录下创建新的 .cpp 文件
2. CMake 配置会自动将其添加为可执行文件

### Python

1. 在 `python/src` 目录下创建新的 .py 文件
2. 可以创建对应的测试文件 `test_文件名.py`

## 常用算法与数据结构

在解决 LeetCode 问题时，以下是一些常用的算法和数据结构：

- 数组和字符串操作
- 链表
- 栈和队列
- 哈希表
- 树和图
- 堆（优先队列）
- 动态规划
- 贪心算法
- 回溯算法
- 二分查找
- 排序算法

## 学习资源

- [LeetCode 官网](https://leetcode.com/)
- [LeetCode 中文站](https://leetcode.cn/)
- [算法可视化](https://visualgo.net/)
- [Big-O 复杂度速查表](https://www.bigocheatsheet.com/)