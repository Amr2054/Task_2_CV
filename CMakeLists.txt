cmake_minimum_required(VERSION 3.12)
project(CvTask2)
cmake_policy(SET CMP0148 NEW)
set(CMAKE_CXX_STANDARD 17)
set(PYBIND11_FINDPYTHON ON)
# Path to your OpenCV installation
find_package(OpenCV REQUIRED)
find_package(Python3 COMPONENTS Interpreter Development REQUIRED)

#execute_process(
#    COMMAND python -m pybind11 --cmakedir
#    OUTPUT_VARIABLE PYBIND11_CMAKE_DIR
#    OUTPUT_STRIP_TRAILING_WHITESPACE
#)

execute_process(
        COMMAND "${Python3_EXECUTABLE}" -c "import pybind11; print(pybind11.get_cmake_dir())"
        OUTPUT_VARIABLE pybind11_DIR
        OUTPUT_STRIP_TRAILING_WHITESPACE
)

list(APPEND CMAKE_PREFIX_PATH "${PYBIND11_CMAKE_DIR}")
find_package(pybind11 REQUIRED)

find_package(OpenCV REQUIRED COMPONENTS core imgproc imgcodecs)

file(GLOB SRC_FILES "core/*.cpp")
pybind11_add_module(CppModule ${SRC_FILES})

target_link_libraries(CppModule PRIVATE ${OpenCV_LIBS})

set_target_properties(CppModule PROPERTIES
    LIBRARY_OUTPUT_DIRECTORY "${CMAKE_SOURCE_DIR}/core"
    RUNTIME_OUTPUT_DIRECTORY "${CMAKE_SOURCE_DIR}/core"
    LIBRARY_OUTPUT_DIRECTORY_RELEASE "${CMAKE_SOURCE_DIR}/core"
    RUNTIME_OUTPUT_DIRECTORY_RELEASE "${CMAKE_SOURCE_DIR}/core"
    LIBRARY_OUTPUT_DIRECTORY_DEBUG "${CMAKE_SOURCE_DIR}/core"
    RUNTIME_OUTPUT_DIRECTORY_DEBUG "${CMAKE_SOURCE_DIR}/core"
    OUTPUT_NAME "CppModule"
)

target_include_directories(CppModule PRIVATE utils)