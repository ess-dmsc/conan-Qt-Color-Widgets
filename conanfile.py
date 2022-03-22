import os
from conans import ConanFile, CMake, tools
from conans.util import files

class QtColorWidgetsConan(ConanFile):
    name = "Qt-Color-Widgets"
    version = "fadd2dd"
    license = "https://github.com/ess-dmsc/Qt-Color-Widgets/blob/master/COPYING"
    url = "https://github.com/ess-dmsc/Qt-Color-Widgets"
    description = "Improved QColorDialog and several other color-related widgets."
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    # The folder name when the *.tar.gz release is extracted
    folder_name = "Qt-Color-Widgets"
    # The temporary build directory
    build_dir = "./%s/build" % folder_name

    def source(self):
        self.run("git clone https://github.com/ess-dmsc/Qt-Color-Widgets.git")
        self.run("cd Qt-Color-Widgets && git checkout {} && cd ..".format(self.version))

    def build(self):
        files.mkdir(self.build_dir)
        with tools.chdir(self.build_dir):
            cmake = CMake(self)
            cmake.definitions["BUILD_SHARED_LIBS"] = "OFF"
            cmake.definitions["BUILD_STATIC_LIBS"] = "ON"
            cmake.definitions["QTCOLORWIDGETS_DESIGNER_PLUGIN"] = "OFF"
            cmake.definitions["CMAKE_INSTALL_PREFIX"] = ""

            if tools.os_info.is_macos:
                cmake.definitions["CMAKE_MACOSX_RPATH"] = "ON"
                cmake.definitions["CMAKE_PREFIX_PATH"] = "/usr/local/opt/qt"
                cmake.definitions["CMAKE_SHARED_LINKER_FLAGS"] = "-headerpad_max_install_names"

            # cmake.configure(source_dir="..", build_dir=".")
            self.run("cmake --debug-output %s %s" % ("..", cmake.command_line))
            cmake.build(build_dir=".")
            os.system("make install DESTDIR=./install")

    def package(self):
        self.copy("*", dst="include", src=self.build_dir+"/install/include")
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["QtColorWidgets"]
