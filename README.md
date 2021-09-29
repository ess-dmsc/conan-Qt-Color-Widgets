# Qt-Color-Widgets conan package

[![Build Status](https://jenkins.esss.dk/dm/job/ess-dmsc/job/conan-Qt-Color-Widgets/job/master/badge/icon)](https://jenkins.esss.dk/dm/job/ess-dmsc/job/conan-Qt-Color-Widgets/job/master/)

Conan package recipe for [Qt-Color-Widgets](https://github.com/ess-dmsc/Qt-Color-Widgets).

## Updating
To update to new version:
* make a branch 
* switch `channel` in [Jenkinsfile](Jenkinsfile) from `stable` to `testing`
* in [conanfile.py](conanfile.py), change the commit hash to point to new version:
  * in `version=`; and
  * under `def source(self):`
* push and massage until the job succeefds on [Jenkins](https://jenkins.esss.dk/dm/job/ess-dmsc/job/conan-Qt-Color-Widgets/)
* switch `channel` back to `stable` and make a merge request
