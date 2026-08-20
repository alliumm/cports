pkgname = "python-pycapnp"
pkgver = "2.2.4"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "pkgconf",
    "python-build",
    "python-cython",
    "python-installer",
    "python-pkgconfig",
    "python-setuptools",
    "python-wheel",
]
makedepends = [
    "capnproto-devel",
    "python-devel",
]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Python Cap'n Proto bindings"
license = "BSD-2-Clause"
url = "https://github.com/capnproto/pycapnp"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "663d553169457ddeff55c9c62b7304bf25aacf87605e047d91d972eea868ef71"
# ModuleNotFoundError: No module named 'capnp.lib.capnp'
# don't know how to fix this
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.md")
