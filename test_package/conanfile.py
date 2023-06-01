# from os.path import join

from conan import ConanFile
# from conan.tools.files import copy
from conan.tools.cmake import CMake, cmake_layout
from conan.tools.build import can_run


import os

class QtColorWidgetsTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps", "CMakeToolchain"

    def requirements(self):
        self.requires(self.tested_reference_str)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def layout(self):
        cmake_layout(self)

    # def imports(self):
    #     copy(self, "*.dll", self.build_folder, join(self.package_folder, "bin"), keep_path=False)
    #     copy(self, "*.so", self.build_folder, join(self.package_folder, "lib"), keep_path=False)
    #     copy(self, "*.dylib", self.build_folder, join(self.package_folder, "lib"), keep_path=False)
    #     copy(self, "*.a", self.build_folder, join(self.package_folder, "lib"), keep_path=False)

    def test(self):
        if can_run(self):
            cmd = os.path.join(self.cpp.build.bindir, "example -platform offscreen")
            self.run(cmd, env="conanrun")
