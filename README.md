# conan-Qt-Color-Widgets

[![Build Status](https://jenkins.esss.dk/dm/job/ess-dmsc/job/conan-Qt-Color-Widgets/job/master/badge/icon)](https://jenkins.esss.dk/dm/job/ess-dmsc/job/conan-Qt-Color-Widgets/job/master/)

Conan package recipe for [QtColorWidgets](https://github.com/ess-dmsc/Qt-Color-Widgets), an improved QColorDialog and several other color-related widgets.

This repository tracks the recipe for generating the conan package. You should not have to run these steps yourself but instead simply fetch the package from the the conan remote server as described below.

## Using the package

See the DMSC [conan-configuration repository](https://github.com/ess-dmsc/conan-configuration) for how to configure your remote.

In `conanfile.txt`:

```
Qt-Color-Widgets/9f4e052@ess-dmsc/stable
```

In CMake:
```
target_link_libraries(my_target
  PRIVATE QtColorWidgets
)
```

## Updating the recipe

If you are a contributor and wish to update this recipe to use the latest version of the target library:

* make a branch
* change `channel` in [Jenkinsfile](Jenkinsfile) from "stable" to "testing"
* in [conanfile.py](conanfile.py) change `version=` to the hash (first 7 hex letters) of the commit that you want to package
* push and massage until the job succeeds on [Jenkins](https://jenkins.esss.dk/dm/job/ess-dmsc/job/conan-Qt-Color-Widgets/)
* ideally, test new version of package with actual projects that use it
* update the conan package name in code example, under the ["Using the package"](#using-the-package) section above
* change `channel` back to "stable" in [Jenkinsfile](Jenkinsfile)
* make a merge request
