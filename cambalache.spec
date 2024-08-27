Name:    cambalache
Version: 0.90.4
Release: %autorelease
License: LGPLv2.1
URL:     https://gitlab.gnome.org/jpu/cambalache
Source0: https://gitlab.gnome.org/jpu/cambalache/-/archive/%{version}/%{name}-%{version}.tar.gz
Summary: Cambalache is a new RAD tool for Gtk 4 and 3 with a clear MVC design and data model first philosophy.

%global uuid ar.xjuan.Cambalache

BuildRequires: gcc
BuildRequires: python3
BuildRequires: meson
BuildRequires: gtk3
BuildRequires: gtk3-devel
BuildRequires: gtk4
BuildRequires: gtk4-devel
BuildRequires: gtksourceview5
BuildRequires: webkit2gtk4.1
BuildRequires: webkitgtk6.0
BuildRequires: libadwaita
BuildRequires: libadwaita-devel
BuildRequires: libhandy
BuildRequires: libhandy-devel
BuildRequires: python3-gobject
BuildRequires: python3-gobject-devel
BuildRequires: python3-lxml
BuildRequires: cmake
BuildRequires: wlroots
BuildRequires: desktop-file-utils
BuildRequires: python3-devel

%description
Cambalache is a new RAD tool for Gtk 4 and 3 with a clear MVC design and data model first philosophy.
This translates to a wide feature coverage with minimal/none developer intervention for basic support.
To support multiple Gtk versions it renders the workspace out of process using
the Gdk broadway backend.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%clean
rm -rf %{buildroot}

%files
%{_bindir}/cambalache
%{_datadir}/cambalache
%{python3_sitelib}/cambalache
%{_datadir}/metainfo/%{uuid}.metainfo.xml
%{_datadir}/applications/%{uuid}.desktop
%{_datadir}/glib-2.0/schemas/%{uuid}.gschema.xml
%{_datadir}/icons/hicolor/*/*/%{uuid}*
%{_datadir}/locale/*/LC_MESSAGES/*
%{_datadir}/mime/packages/%{uuid}.mime.xml
%{_libdir}/girepository-1.0/CambalachePrivate-3.0.typelib
%{_libdir}/girepository-1.0/CambalachePrivate-4.0.typelib
%{_libdir}/libcambalacheprivate-3.so
%{_libdir}/libcambalacheprivate-4.so
%{_datadir}/gir-1.0/CambalachePrivate-3.0.gir
%{_datadir}/gir-1.0/CambalachePrivate-4.0.gir
