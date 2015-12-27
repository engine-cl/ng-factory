[![Build Status](https://travis-ci.org/engine-cl/ng-factory.svg)](https://travis-ci.org/engine-cl/ng-factory)
[![codecov.io](https://codecov.io/github/engine-cl/ng-factory/coverage.svg?branch=master)](https://codecov.io/github/engine-cl/ng-factory?branch=master)
[![Code Issues](https://www.quantifiedcode.com/api/v1/project/f57003898f714494b2a6f2bb66516a18/badge.svg)](https://www.quantifiedcode.com/app/project/f57003898f714494b2a6f2bb66516a18)
## python 3.x generic factory
Python 3 factory pattern implementation.


## Documentation
The principal idea is keep it simple and readable, the main function is provide a mechanism to factorize object
with introspection and don't make the horrible factory if type == 'MyClass': return MyClass() so for it this module
factorize any class from any module and works only in python 3 for python 2 you have pypi module named factory and
maybe is better for you with more functionality and complexity.


## Example
```python
from ng_factory import factorize
try:
    f = factorize(module='collections', object_type='named_tuple')
except NonExistentModuleError as e:
    print("{}".format(e)

```