cmake_minimum_required(VERSION 3.0)
project(ooten)

# common settings
enable_testing()

# C++ settings
set(CMAKE_CXX_STANDARD 14)
include_directories(${PROJECT_SOURCE_DIR}/ooten)

# Add subdirectories
add_subdirectory(ooten)