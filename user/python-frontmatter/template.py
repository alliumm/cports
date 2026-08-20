pkgname = "python-frontmatter"
pkgver = "1.2.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python"]
checkdepends = [
    "python-pytest",
    "python-pyyaml",
]
pkgdesc = "Python frontmatter library"
license = "MIT"
url = "https://github.com/eyeseast/python-frontmatter"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "829cbe707f073e3db45f358ae14062dde3ff4f42a8bcbd4978a4cd01d5a20d30"
# tests require python toml
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
