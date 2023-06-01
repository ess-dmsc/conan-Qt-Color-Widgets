cmake_minimum_required(VERSION 3.15)
project(PackageTest CXX)

#For Qt
if(APPLE AND EXISTS /usr/local/opt/qt)
  # Homebrew installs Qt5 (up to at least 5.9.1) in
  # /usr/local/opt/qt, ensure it can be found by CMake since
  # it is not in the default /usr/local prefix.
  list(APPEND CMAKE_PREFIX_PATH "/usr/local/opt/qt")
endif()
set(CMAKE_INCLUDE_CURRENT_DIR ON)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)
find_package(Qt5 COMPONENTS Widgets PrintSupport REQUIRED)

add_executable(example example.cpp)

# Add the path used by conan to install the header files
target_include_directories(example PUBLIC
  ${CMAKE_INCLUDE_PATH})

# Add the path used by conan to install the library files
target_link_directories(example PUBLIC
  ${CMAKE_LIBRARY_PATH})

target_link_libraries(example
    ${CONAN_LIBS}
    QtColorWidgets
    Qt5::Widgets
    Qt5::PrintSupport)

# CTest is a testing tool that can be used to test your project.
# enable_testing()
# add_test(NAME example
#          WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
#          COMMAND example)
