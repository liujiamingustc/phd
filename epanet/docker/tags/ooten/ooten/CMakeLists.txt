file(GLOB_RECURSE files *.c *.cpp)
add_library(ooten ${files})

add_executable(example1 example1.cpp)
target_link_libraries(example1 ooten)
