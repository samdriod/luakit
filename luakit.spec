Name:           luakit
Version:        2.4.0
Release:        1%{?dist}
Summary:        Fast, small, webkit-based browser framework extensible with Lua

License:        GPLv3
URL:            https://luakit.github.io/
Source0:        https://github.com/luakit/luakit/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(webkit2gtk-4.1)
BuildRequires:  pkgconfig(javascriptcoregtk-4.1)
BuildRequires:  pkgconfig(sqlite3)

# Upstream defaults to LuaJIT (USE_LUAJIT ?= 1) and discovers it via pkg-config.
BuildRequires:  pkgconfig(luajit)
BuildRequires:  lua-filesystem

%description
Luakit is a highly configurable browser framework based on the WebKit web content engine
and the GTK+ toolkit. It is very fast, extensible with Lua, and licensed under the GNU
GPLv3 license.

%prep
%autosetup

%build
# Luakit does not use a configure script, just a Makefile.
# We set PREFIX to /usr so it installs in the correct system directories.
# DEVELOPMENT_PATHS=0 ensures system paths (/usr, /etc/xdg) are used.
make %{?_smp_mflags} PREFIX=/usr DEVELOPMENT_PATHS=0

%install
# DESTDIR is the temporary virtual filesystem COPR uses to package the RPM.
make install DESTDIR=%{buildroot} PREFIX=/usr

%files
/usr/bin/luakit
/usr/lib/luakit/luakit.so
/usr/share/luakit/
/usr/share/applications/luakit.desktop
/usr/share/man/man1/luakit.1*
/usr/share/pixmaps/luakit.png
/usr/share/pixmaps/luakit.svg
%config(noreplace) /etc/xdg/luakit/*.lua

%changelog
* Thu May 14 2026 COPR Builder <copr@fedoraproject.org> - 2.4.0-1
- Automated build via COPR
