%define url_ver %(echo %{version}|cut -d. -f1,2)

%define api	1.0
%define major	3
%define libname	%mklibname %{name} %{api} %{major}
%define girname	%mklibname %{name}-gir %{api}
%define devname	%mklibname -d %{name}

Summary:	A collection of helpers for building UPnP AV applications
Name:		gupnp-av
Version:	0.14.4
Release:	1
Group:		System/Libraries
License:	LGPLv2+
Url:		https://www.gupnp.org/
Source0:	https://ftp.gnome.org/pub/GNOME/sources/gupnp-av/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gtk-doc)
BuildRequires:	pkgconfig(gupnp-1.6)
BuildRequires:  pkgconfig(vapigen)
BuildRequires:  vala-tools
BuildRequires:  meson

%description
GUPnP is an object-oriented open source framework for creating UPnP
devices and control points, written in C using GObject and libsoup.
The GUPnP API is intended to be easy to use, efficient and flexible.

GUPnP-AV is a collection of helpers for building AV (audio/video)
applications using GUPnP.

%package -n %{libname}
Summary:	 A collection of helpers for building UPnP AV applications
Group:		System/Libraries

%description -n %{libname}
GUPnP is an object-oriented open source framework for creating UPnP
devices and control points, written in C using GObject and libsoup.
The GUPnP API is intended to be easy to use, efficient and flexible.

GUPnP-AV is a collection of helpers for building AV (audio/video)
applications using GUPnP.

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n %{devname}
Summary:	Development package for gupnp-av
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Files for development with gupnp-av.

%prep
%setup -q
%autopatch -p1

%build
%meson  \
        -Dgtk_doc=true
%meson_build

%install
%meson_install

%files -n %{libname}
%{_libdir}/libgupnp-av-%{api}.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/GUPnPAV-%{api}.typelib

%files -n %{devname}
%doc AUTHORS COPYING README.md
%{_datadir}/gtk-doc/html/gupnp-av/
%{_includedir}/gupnp-av-%{api}
%{_libdir}/pkgconfig/gupnp-av-%{api}.pc
%{_libdir}/libgupnp-av-%{api}.so
%{_datadir}/gir-1.0/GUPnPAV-%{api}.gir
%{_datadir}/%{name}
%{_datadir}/vala/vapi/*

