# `makeh` - Online documentation for GNU Makefiles
![Travis (.org)](https://img.shields.io/travis/gunziptarball/makeh)
![PyPI](https://img.shields.io/pypi/v/makeh)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/makeh)

Possibly re-inventing a wheel.  
Looks like [this project](https://github.com/ryanvolpe/makehelp) also does something similar.

## Usage

```shell
pip install makeh
cd $SOME_PROJECT_WITH_A_MAKEFILE
makeh
# documentation will appear
```

...yes I acknowledge the irony of this project not having its own Makefile.  
Har-har.

## Feature Wishlist

- [x] List variables (including defaults)
- [x] Support for Python3.5+  
- [ ] Show summary of project
- [ ] Detailed help for targets `e.g. makeh clean`
- [ ] target-specific variables
- [ ] "examples" section
- [ ] "static" generator (based on the feature from aforementioned project)
- [ ] Support for colors
