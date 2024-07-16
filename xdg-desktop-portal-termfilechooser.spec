Name     : xdg-desktop-portal-termfilechooser
Version  : 71dc7ab06751e51de392b9a7af2b50018e40e062
Release  : 1
URL      : https://github.com/GermainZ/xdg-desktop-portal-termfilechooser
Source0  : https://github.com/GermainZ/xdg-desktop-portal-termfilechooser/archive/refs/heads/main.tar.gz
Summary  : No detailed summary available
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
pushd ..
cp -a xdg-desktop-portal-termfilechooser-main buildavx2
popd

%build
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1707785266
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dman-pages=disabled   builddir
ninja -v -C builddir
GOAMD64=v3
CFLAGS="$CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -march=x86-64-v3 " meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dman-pages=disabled   builddiravx2
ninja -v -C builddiravx2

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3  -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views  "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3  -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views  "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3  -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views  "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3  -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views  "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
GOAMD64=v3
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
GOAMD64=v2
DESTDIR=%{buildroot} ninja -C builddir install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/share/dbus-1/services/*.service
/usr/share/xdg-desktop-portal/portals/*.portal
/V3/usr/libexec/*
/usr/libexec/*
/usr/lib/systemd/user/*.service
/usr/share/xdg-desktop-portal-termfilechooser/ranger-wrapper.sh