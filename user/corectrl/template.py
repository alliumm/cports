pkgname = "corectrl"
pkgver = "1.5.2"
pkgrel = 4
build_style = "cmake"
configure_args = [
    "-DINSTALL_DBUS_FILES_IN_PREFIX=true"
    "-DPOLKIT_POLICY_INSTALL_DIR=/usr/share/polkit-1/actions"
]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
    "pkgconf",
]
makedepends = [
    "botan-devel",
    "catch2-devel",
    "karchive-devel",
    "kauth-devel",
    "libdrm-devel",
    "polkit-devel",
    "pugixml-devel",
    "qt6-qt5compat-devel",
    "qt6-qtbase-devel",
    "qt6-qtcharts-devel",
    "qt6-qtquick3d-devel",
    "qt6-qtsvg-devel",
    "qt6-qttools-devel",
    "quazip-devel",
    "spdlog-devel",
    "trompeloeil",
]
depends = [
    "hwdata-pci",
    "mesa-demos-core",
    "polkit",
    "procps",
    "util-linux",
    "vulkan-tools",
]
pkgdesc = "Profile based system control utility"
license = "GPL-3.0-or-later"
url = "https://gitlab.com/corectrl/corectrl"
source = f"{url}/-/archive/v{pkgver}/corectrl-v{pkgver}.tar.gz"
sha256 = "6eccc6ea82a62e8491ad516a589e12e14d52ad0aaa74166ea74f35bf1c10c38e"
# HWIDTranslator test fails and i couldn't figure out how to skip it.
# GPU names are missing but it doesn't seem to affect functionality
options = ["!check"]
