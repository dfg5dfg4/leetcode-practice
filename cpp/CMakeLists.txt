cmake_minimum_required(VERSION 3.10)
project(LeetCode_Solutions)

# 设置C++标准
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# 添加包含目录
include_directories(${PROJECT_SOURCE_DIR}/src)

# 查找所有源文件
file(GLOB SOURCES "src/*.cpp")

# 为每个源文件创建可执行文件
foreach(source_file ${SOURCES})
    # 获取文件名（不带扩展名）
    get_filename_component(executable_name ${source_file} NAME_WE)
    
    # 创建可执行文件
    add_executable(${executable_name} ${source_file})
endforeach()

# 添加测试支持（可选）
option(BUILD_TESTS "Build tests" ON)
if(BUILD_TESTS)
    enable_testing()
    # 可以在这里添加测试配置
endif()