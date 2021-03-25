# `makeh` - Online documentation for GNU Makefiles
<p align="center">
  <a href="https://pypi.org/project/makeh">
    <img alt="PyPI" src="https://img.shields.io/pypi/v/makeh">
  </a>
</p>

Possibly re-inventing a wheel.  
Looks like [this project](https://github.com/ryanvolpe/makehelp) also does something similar.

## Usage

 - Requires `poetry` and Python3.8 or higher

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
- [ ] Show summary of project
- [ ] Detailed help for targets `e.g. makeh clean`
- [ ] target-specific variables
- [ ] "examples" section
- [ ] "static" generator (based on the feature from aforementioned project)
- [ ] Support for colors
