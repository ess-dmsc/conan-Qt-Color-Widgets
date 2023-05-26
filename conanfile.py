from conan import ConanFile
from conan.tools.files import copy
from conan.tools.apple import is_apple_os
from conan.tools.cmake import CMakeToolchain, CMakeDeps, CMake, cmake_layout

class QtColorWidgetsConan(ConanFile):
    name = "qt-color-widgets"
    version = "conan_v2"
    license = "https://github.com/ess-dmsc/Qt-Color-Widgets/blob/master/COPYING"
    url = "https://github.com/ess-dmsc/Qt-Color-Widgets"
    description = "Improved QColorDialog and several other color-related widgets."
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared":False}

    # The folder name when the *.tar.gz release is extracted
    folder_name = "Qt-Color-Widgets"
    # The temporary build directory
    build_dir = f"./{folder_name}/build"

    def source(self):
        self.run("git clone https://github.com/ess-dmsc/Qt-Color-Widgets.git")
        self.run(f"cd Qt-Color-Widgets && git checkout {self.version} && cd ..")

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

        deps = CMakeDeps(self)
        deps.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

        # mkdir(self, self.build_dir)
        # with chdir(self, self.build_dir):
        #
        #     # cmake.configure(source_dir="..", build_dir=".")
        #     self.run("cmake --debug-output %s %s" % ("..", cmake.command_line))
        #     cmake.build(build_dir=".")
        #     os.system("make install DESTDIR=./install")

    def package(self):
        copy(self, "*", self.source_folder, join(self.package_folder, "include"), keep_path=False)
        copy(self, "*.dll", self.build_folder, join(self.package_folder, "bin"), keep_path=False)
        copy(self, "*.so", self.build_folder, join(self.package_folder, "lib"), keep_path=False)
        copy(self, "*.dylib", self.build_folder, join(self.package_folder, "lib"), keep_path=False)
        copy(self, "*.a", self.build_folder, join(self.package_folder, "lib"), keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["QtColorWidgets"]
