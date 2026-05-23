cmake_minimum_required(VERSION 3.12)
project(trading_engine)

# 设置C++标准
# English: Set the C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# 查找依赖包
# English: Find required dependencies
find_package(pybind11 REQUIRED)  # Python接口
# English: Python interface
find_package(spdlog REQUIRED)    # 日志
# English: Logging
find_package(nlohmann_json REQUIRED)  # JSON处理
# English: JSON processing
find_package(Boost REQUIRED COMPONENTS system)  # Boost

# 添加头文件路径
# English: Add include directories
include_directories(${CMAKE_SOURCE_DIR}/include)

# 收集源文件
# English: Collect source files
file(GLOB_RECURSE SOURCES "src/*.cpp")

# 创建可执行文件
# English: Create executable target
add_executable(trading_engine ${SOURCES})

# 链接依赖库
# English: Link dependency libraries
target_link_libraries(trading_engine
    PRIVATE
        pybind11::embed
        spdlog::spdlog
        nlohmann_json::nlohmann_json
        Boost::system
        pthread
) 