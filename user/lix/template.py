pkgname = "lix"
pkgver = "2.96.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Ddefault_library=shared",
    "-Dlibexec-dir=/usr/lib",
    "-Dprofile-dir=/usr/lib/profile.d",
    # tests are skipped
    "-Denable-tests=false",
]
hostmakedepends = [
    "bash",
    "cargo-auditable",
    "cbindgen",
    "cmake",
    "doxygen",
    "jq",
    "lsof",
    "mdbook",
    "meson",
    "pkgconf",
    "python",
]
makedepends = [
    "boost-devel",
    "brotli-devel",
    "capnproto-devel",
    "curl-devel",
    "dinit-chimera",
    "gc-devel",
    "libarchive-devel",
    "libseccomp-devel",
    "libsodium-devel",
    "lowdown-devel",
    "nlohmann-json",
    "openssl3-devel",
    "pegtl",
    "pegtl-devel",
    "python-frontmatter",
    "python-pycapnp",
    "python-pyyaml",
    "sqlite-devel",
    "toml11",
]
pkgdesc = "Purely functional package manager"
license = "LGPL-2.1-or-later"
url = "https://git.lix.systems/lix-project/lix"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "3b1ce9dda9342738db2c68435f49af51be10e42821365387520709f6b4a0e8e0"
# tests require rapidcheck
options = ["!check"]


def post_patch(self):
    from cbuild.util import cargo

    cargo.Cargo(self, wrksrc=".").vendor()


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.env.update(renv)


def post_install(self):
    self.uninstall("usr/lib/systemd")
    # don't package html docs
    self.uninstall("usr/share/doc")

    self.install_license("COPYING")
    self.install_file(self.files_path / "nix.conf", "usr/share/nix")
    self.install_service(self.files_path / "nix-daemon")
    self.install_sysusers(self.files_path / "sysusers.conf", "nix-daemon")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf", "nix")


@subpackage("lix-devel")
def _(self):
    return self.default_devel()
