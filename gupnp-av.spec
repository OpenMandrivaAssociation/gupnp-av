%define api 1.0
%define major 2
%define libname %mklibname %name %api %major
%define develname %mklibname -d %name
Name:           gupnp-av
Version:        0.5.5
Release:        %mkrel 1
Summary:        A collection of helpers for building UPnP AV applications

Group:          System/Libraries
License:        LGPLv2+
URL:            http://www.gupnp.org/
Source0:        http://www.gupnp.org/sources/%{name}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gtk-doc
BuildRequires: gupnp-devel
BuildRequires: gobject-introspection-devel
#gw TODO: remove this
BuildRequires: gir-repository

%description
GUPnP is an object-oriented open source framework for creating UPnP
devices and control points, written in C using GObject and libsoup.
The GUPnP API is intended to be easy to use, efficient and flexible.

GUPnP-AV is a collection of helpers for building AV (audio/video) 
applications using GUPnP.

%package -n %libname
Summary: A collection of helpers for building UPnP AV applications
Group: System/Libraries

%description -n %libname
GUPnP is an object-oriented open source framework for creating UPnP
devices and control points, written in C using GObject and libsoup.
The GUPnP API is intended to be easy to use, efficient and flexible.

GUPnP-AV is a collection of helpers for building AV (audio/video) 
applications using GUPnP.


%package -n %develname
Summary: Development package for gupnp-av
Group: Development/C
Requires: %libname = %{version}-%{release}
Provides: %name-devel = %version-%release
Provides: lib%name-devel = %version-%release

%description -n %develname
Files for development with gupnp-av.

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdvver < 200900
%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig
%endif

%files -n %libname
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
%{_libdir}/libgupnp-av-%api.so.%{major}*
%_libdir/girepository-1.0/GUPnPAV-%api.typelib

%files -n %develname
%defattr(-,root,root,-)
%{_datadir}/gtk-doc/html/gupnp-av/
%{_includedir}/gupnp-av-%api
%{_libdir}/pkgconfig/gupnp-av-%api.pc
%{_libdir}/libgupnp-av-%api.so
%{_libdir}/libgupnp-av-%api.la
%_datadir/gir-1.0/GUPnPAV-%api.gir
