from conan import ConanFile
from conan.tools.apple import is_apple_os
from conan.tools.scm import Git
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout

class QtColorWidgetsConan(ConanFile):
    name = "qt-color-widgets"
    version = "9f4e052"
    license = "https://github.com/ess-dmsc/Qt-Color-Widgets/blob/master/COPYING"
    url = "https://github.com/ess-dmsc/Qt-Color-Widgets"
    description = "Improved QColorDialog and several other color-related widgets."
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared":False}
    generators = "CMakeDeps"

    # The folder name when the *.tar.gz release is extracted
    folder_name = "Qt-Color-Widgets"

    def source(self):
        git = Git(self)
        git.clone(url="https://github.com/ess-dmsc/Qt-Color-Widgets.git", target=".")
        git.checkout(self.version)

    def layout(self):
        cmake_layout(self)

    def generate(self):
        tc = CMakeToolchain(self)
        tc.preprocessor_definitions["BUILD_SHARED_LIBS"] = "OFF"
        tc.preprocessor_definitions["BUILD_STATIC_LIBS"] = "ON"
        tc.preprocessor_definitions["QTCOLORWIDGETS_DESIGNER_PLUGIN"] = "OFF"
        tc.preprocessor_definitions["CMAKE_INSTALL_PREFIX"] = ""

        if is_apple_os:
            tc.preprocessor_definitions["CMAKE_MACOSX_RPATH"] = "ON"
            tc.preprocessor_definitions["CMAKE_PREFIX_PATH"] = "/usr/local/opt/qt"
            tc.preprocessor_definitions["CMAKE_SHARED_LINKER_FLAGS"] = "-headerpad_max_install_names"

        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["QtColorWidgets"]
