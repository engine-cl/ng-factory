[![Build Status](https://travis-ci.org/engine-cl/ng-factory.svg)](https://travis-ci.org/engine-cl/ng-factory)
[![codecov.io](https://codecov.io/github/engine-cl/ng-factory/coverage.svg?branch=master)](https://codecov.io/github/engine-cl/ng-factory?branch=master)
[![Code Issues](https://www.quantifiedcode.com/api/v1/project/f57003898f714494b2a6f2bb66516a18/badge.svg)](https://www.quantifiedcode.com/app/project/f57003898f714494b2a6f2bb66516a18)
## Overview
Python 3 object factory pattern implementation.
The principal idea is keep it simple and readable, the main function provide a mechanism to factorize any object
with introspection and don't make the horrible code conditions like in factory examples:
```python
def factory(type):
    if type == 'MyClass': 
        return MyClass()
    if type == 'MyOtherClass': 
        return MyOtherClass()
``` 
 So for it this module factorize any class from any module and works only in python 3 
for python 2 you have pypi module named [Factory](https://pypi.python.org/pypi/Factory/) and maybe is better for you 
with more functionality and complexity.

## Installation
```bash
git clone https://github.com/engine-cl/ng_factory.git
cd ng-factory
python3 setup.py install
```

## Testing
```python
python test/factory.py
```
## Example
Create any module with your atomic class encapsulation with GOPS and then factorize object to inject the dependencies 
into the business logic like persistence layer or another layer.
```python
from ng_factory import factorize
class persistence(object):
    """ assumes all code needed to connect db and commit data transaction """
    def __init__(self, data):
        import database
        self._dbcon = database.get_connection()
        self.data = data
        
    def save(this):
        this._dbcon.commit(this.data.persist())

class DataObjectTypeOne(object):
    """ assumes all serializable function to format the data output """
    @staticmethod
    def persist():
        return self.get_save_format()

db = persistence(factorize(DataObjectTypeOne))
db.save()

```