pkgname = "lact"
pkgver = "0.9.1"
pkgrel = 0
build_style = "cargo"
prepare_after_patch = True
hostmakedepends = [
    "cargo",
    "pkgconf",
]
makedepends = [
    "gtk4-devel",
    "libadwaita-devel",
    "libdisplay-info-devel",
    "libdrm-devel",
]
depends = [
    "clinfo",
    "hwdata-pci",
    "vulkan-tools",
]
pkgdesc = "Linux GPU Configuration and Monitoring Tool"
license = "MIT"
url = "https://github.com/ilya-zlobintsev/LACT"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "cb6790ffb99104ffb93502c82e19b9e8d07ec7c1eadf131948694d48eba49789"

self.make_check_args = [
    "--",
    "--skip=tests::apply_settings",  # doesn't work in container
]


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/lact")
    self.install_file(
        "res/io.github.ilya_zlobintsev.LACT.desktop", "usr/share/applications"
    )
    self.install_file(
        "res/io.github.ilya_zlobintsev.LACT.png", "usr/share/icons"
    )
    self.install_file(
        "res/io.github.ilya_zlobintsev.LACT.svg",
        "usr/share/icons/hicolor/scalable/apps",
    )
    self.install_service(self.files_path / "lactd")
    self.install_license("LICENSE")
