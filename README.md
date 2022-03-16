# conan-Qt-Color-Widgets

[![Build Status](https://jenkins.esss.dk/dm/job/ess-dmsc/job/conan-Qt-Color-Widgets/job/master/badge/icon)](https://jenkins.esss.dk/dm/job/ess-dmsc/job/conan-Qt-Color-Widgets/job/master/)

Conan package recipe for [QtColorWidgets](https://github.com/ess-dmsc/Qt-Color-Widgets), an improved QColorDialog and several other color-related widgets.

This repository tracks the recipe for generating the conan package. You should not have to run these steps yourself but instead simply fetch the package from the the conan remote server as described below.

## Using

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

## Updating

If you are a contributor and wish to update this recipe to use the latest version of the target library:

* make a branch
* switch `channel` in [Jenkinsfile](Jenkinsfile) from `stable` to `testing`
* change the commit hash to point to new version:
  * in [conanfile.py](conanfile.py) at `version=`
  * in this README, under the ["Using"](#using) section above
* push and massage until the job succeeds on [Jenkins](https://jenkins.esss.dk/dm/job/ess-dmsc/job/conan-qplot/)
* ideally, test new version of package with actual projects that use it
* switch `channel` back to `stable` and make a merge request
