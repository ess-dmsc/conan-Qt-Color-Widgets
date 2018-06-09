from conans import ConanFile, CMake, tools


class QtColorWidgetsConan(ConanFile):
    name = "Qt-Color-Widgets"
    version = "fbeaae4"
    license = "https://github.com/ess-dmsc/Qt-Color-Widgets/blob/master/COPYING"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Qt-Color-Widgets here>"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    def source(self):
        self.run("git clone https://github.com/ess-dmsc/Qt-Color-Widgets.git")
        self.run("cd benchmark && git checkout fbeaae4 && cd ..")
        # This small hack might be useful to guarantee proper /MT /MD linkage in MSVC
        # if the packaged project doesn't have variables to set it properly
#        tools.replace_in_file("benchmark/CMakeLists.txt", "project (benchmark)", '''project (benchmark)
#include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
#conan_basic_setup()''')

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_dir="%s/benchmark" % self.source_folder)
        cmake.build()

        # Explicit way:
        # self.run('cmake %s/benchmark %s' % (self.source_folder, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include", src="benchmark/include")
        self.copy("*benchmark.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["benchmark"]
