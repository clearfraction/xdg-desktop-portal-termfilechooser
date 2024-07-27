Name     : xdg-desktop-portal-termfilechooser
Version  : a3736ca9b3e9c5b19afabfc99f81fbde70a7e066
Release  : 1
URL      : https://github.com/boydaihungst/xdg-desktop-portal-termfilechooser
Source0  : https://github.com/boydaihungst/xdg-desktop-portal-termfilechooser/archive/refs/heads/main.tar.gz
Summary  : xdg-desktop-portal backend for choosing files with your favorite file chooser.
Group    : Development/Tools
License  : MIT
BuildRequires : buildreq-meson
BuildRequires : pkgconfig(gbm)
BuildRequires : pkgconfig(inih)
BuildRequires : pkgconfig(libpipewire-0.3)
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(scdoc)
BuildRequires : pkgconfig(systemd)
BuildRequires : pkgconfig(wayland-client)
BuildRequires : pkgconfig(wayland-protocols)

%description
xdg-desktop-portal backend for choosing files with your favorite file chooser. By default, it will use the ranger file manager, but this is customizable. Based on xdg-desktop-portal-wlr (xpdw).



%prep
%setup -q -n xdg-desktop-portal-termfilechooser-main
cd %{_builddir}/xdg-desktop-portal-termfilechooser-main


%build
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1707785266
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3  -ffat-lto-objects -flto=auto  "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3  -ffat-lto-objects -flto=auto  "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3  -ffat-lto-objects -flto=auto  "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dman-pages=disabled   builddir
ninja -v -C builddir


%install
DESTDIR=%{buildroot} ninja -C builddir install
mv contrib/{fzf-wrapper.sh,lf-wrapper.sh,vifm-wrapper.sh,yazi-wrapper.sh} %{buildroot}/usr/share/xdg-desktop-portal-termfilechooser/

%files
%defattr(-,root,root,-)
/usr/share/dbus-1/services/*.service
/usr/share/xdg-desktop-portal/portals/*.portal
/usr/libexec/*
/usr/lib/systemd/user/*.service
/usr/share/xdg-desktop-portal-termfilechooser/ranger-wrapper.sh
/usr/share/xdg-desktop-portal-termfilechooser/fzf-wrapper.sh
/usr/share/xdg-desktop-portal-termfilechooser/lf-wrapper.sh
/usr/share/xdg-desktop-portal-termfilechooser/yazi-wrapper.sh
/usr/share/xdg-desktop-portal-termfilechooser/vifm-wrapper.sh
