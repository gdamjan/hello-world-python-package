# hello-world-python-package

Install with either:

```
git clone https://github.com/gdamjan/hello-world-python-package.git
cd hello-world-python-package
pip install --user .
```
or directly
```
pip install --user git+https://github.com/gdamjan/hello-world-python-package.git#egg=cool_lib
```

## PLEASE

* don't try to play games with sys.path - that's surely wrong, and ends in tears
* the same is true for PYTHONPATH too
* use [PEP-370](https://www.python.org/dev/peps/pep-0370/) instead of virtualenv, it's a standard feature and not a hack around the `python` executable. Quickest Howto about pep-370, use `pip install --user`, and optionally set the `PYTHONUSERBASE` environment variable to choose another directory than `~/.local/`.

Thanks!


## Other resources:

* http://python-packaging.readthedocs.org/en/latest/
* https://pip.pypa.io/en/stable/
* https://chriswarrick.com/blog/2014/09/15/python-apps-the-right-way-entry_points-and-scripts/
