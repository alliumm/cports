pkgname = "sway-workspace-balancer"
pkgver = "0.1.6"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo"]
makedepends = ["rust-std"]
depends = ["sway"]
pkgdesc = (
    "Sway IPC daemon that automatically balances workspaces across outputs"
)
license = "AGPL-3.0-only"
url = "https://codeberg.org/alliumm/sway-workspace-balancer"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "fd05c1713800204d4ca96c27c091246cb370a966d1e0b88a689788755eec7a9d"


def post_install(self):
    self.install_license("LICENSE")
