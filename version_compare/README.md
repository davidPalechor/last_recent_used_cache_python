# Version Compare
Compares two version strings and returns a tuple with the items organized from the oldest one to the newest one.

## Usage

```shell script
>>> from version_compare.compare import compare
>>> compare('3.0.1-rc.1', '3.0.1-beta')
('3.0.1-beta', '3.0.1-rc.1')
```

- The two version strings received as a parameter should be a valid version string based on the basics for [Semantic Versioning](https://semver.org/). e.g.

    ***Invalid***
    
    `a.3.2-beta`
    
    ***Valid***
    
    `1.3.2-beta`
    
### Issues

- The package can process a limited number of pre-release tags such as `alpha`, `beta` and `rc`.
- Concatenated pre-release tags such as `1.0.1-alpha.beta` are not allowed yet.
- Versioning including build metadata is not supported. e.g `1.0.0-alpha+001`.
