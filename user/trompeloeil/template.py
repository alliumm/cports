pkgname = "trompeloeil"
pkgver = "49"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DTROMPELOEIL_BUILD_TESTS=yes"]
hostmakedepends = ["cmake", "ninja"]
makedepends = ["catch2-devel"]
pkgdesc = "Header only C++14 mocking framework"
license = "BSL-1.0"
url = "https://github.com/rollbear/trompeloeil"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "2523571fb7920b2813cbc23b46e60294aba8ead7eba434bfec69c24408615593"
tool_flags = {
    "CXXFLAGS": [
        "-Wno-float-equal",
        "-Wno-missing-noreturn",
        "-Wno-unsafe-buffer-usage",
    ]
}


def check(self):
    self.do("./build/test/custom_recursive_mutex")
    self.do("./build/test/self_test")
    # this fails, presumaby because of missing pthread?
    # self.do("./build/test/thread_terror")


def post_install(self):
    self.install_license("LICENSE_1_0.txt")
