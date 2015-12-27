[![Build Status](https://travis-ci.org/engine-cl/ng-factory.svg)](https://travis-ci.org/engine-cl/ng-factory)
[![codecov.io](https://codecov.io/github/engine-cl/ng-factory/coverage.svg?branch=master)](https://codecov.io/github/engine-cl/ng-factory?branch=master)
[![Code Issues](https://www.quantifiedcode.com/api/v1/project/f57003898f714494b2a6f2bb66516a18/badge.svg)](https://www.quantifiedcode.com/app/project/f57003898f714494b2a6f2bb66516a18)
## python 3.x generic factory
Python 3 factory pattern implementation.


## Overview
The principal idea is keep it simple and readable, the main function provide a mechanism to factorize any object
with introspection and don't make the horrible code conditions like in factory examples:
```python
if type == 'MyClass': 
    return MyClass()
if type == 'MyOtherClass': 
    return MyOtherClass()
``` 
 So for it this module factorize any class from any module and works only in python 3 
for python 2 you have pypi module named [Factory](https://pypi.python.org/pypi/Factory/) and maybe is better for you 
with more functionality and complexity.

## Install
```shell
git clone https://github.com/engine-cl/ng_factory.git
cd ng-factory
python3 setup.py install
```
## Example
```python
from ng_factory import factorize
try:
    my_counter = factorize(module='collections', object_type='Counter')
except NonExistentModuleError as e:
    print("{}".format(e))
```