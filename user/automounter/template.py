pkgname = "automounter"
pkgver = "0.1.3"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo", "pkgconf"]
makedepends = [
    "dinit-dbus-dinit",
    "rust-std",
    "udev-devel",
]
depends = [
    "dinit-dbus",
    "udev",
    "udisks",
]
pkgdesc = "Silly lil automounter"
license = "AGPL-3.0-only"
url = "https://codeberg.org/alliumm/automounter"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "f7452b3176e72a36f8b074fa129a6a9b83b8bbf9c0613df2e4f3b04d8e994959"


def post_install(self):
    self.install_license("LICENSE")
    self.install_service(self.files_path / "automounter.user")
