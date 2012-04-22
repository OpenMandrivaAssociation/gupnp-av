%define api 1.0
%define major 2
%define libname %mklibname %{name} %{api} %{major}
%define girname %mklibname %{name}-gir %{api}
%define develname %mklibname -d %{name}

Summary:	A collection of helpers for building UPnP AV applications
Name:		gupnp-av
Version:	0.10.2
Release:	1
Group:		System/Libraries
License:	LGPLv2+
URL:		http://www.gupnp.org/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(gtk-doc)
BuildRequires: pkgconfig(gupnp-1.0)

%description
GUPnP is an object-oriented open source framework for creating UPnP
devices and control points, written in C using GObject and libsoup.
The GUPnP API is intended to be easy to use, efficient and flexible.

GUPnP-AV is a collection of helpers for building AV (audio/video) 
applications using GUPnP.

%package -n %{libname}
Summary: A collection of helpers for building UPnP AV applications
Group: System/Libraries

%description -n %{libname}
GUPnP is an object-oriented open source framework for creating UPnP
devices and control points, written in C using GObject and libsoup.
The GUPnP API is intended to be easy to use, efficient and flexible.

GUPnP-AV is a collection of helpers for building AV (audio/video) 
applications using GUPnP.

%package -n %{girname}
Summary: GObject Introspection interface description for %{name}
Group: System/Libraries
Requires: %{libname} = %{version}-%{release}
 	
%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n %{develname}
Summary: Development package for gupnp-av
Group: Development/C
Requires: %{libname} = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}

%description -n %{develname}
Files for development with gupnp-av.

%prep
%setup -q
%apply_patches
autoreconf -fi

%build
%configure2_5x --disable-static
%make LIBS='-lgmodule-2.0'

%install
%makeinstall_std

%files -n %{libname}
%doc AUTHORS COPYING README
%{_libdir}/libgupnp-av-%{api}.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/GUPnPAV-%{api}.typelib

%files -n %{develname}
%{_datadir}/gtk-doc/html/gupnp-av/
%{_includedir}/gupnp-av-%{api}
%{_libdir}/pkgconfig/gupnp-av-%{api}.pc
%{_libdir}/libgupnp-av-%{api}.so
%{_datadir}/gir-1.0/GUPnPAV-%{api}.gir

