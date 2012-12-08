%define api 1.0
%define major 2
%define libname %mklibname %{name} %{api} %{major}
%define girname %mklibname %{name}-gir %{api}
%define develname %mklibname -d %{name}

Summary:	A collection of helpers for building UPnP AV applications
Name:		gupnp-av
Version:	0.10.3
Release:	1
Group:		System/Libraries
License:	LGPLv2+
URL:		http://www.gupnp.org/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gtk-doc)
BuildRequires:	pkgconfig(gupnp-1.0)

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
Requires:	%{libname} = %{version}-%{release}

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n %{develname}
Summary:	Development package for gupnp-av
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

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


%changelog
* Mon Aug 20 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.10.3-1
+ Revision: 815404
- update to new version 0.10.3

* Sun Apr 22 2012 Götz Waschk <waschk@mandriva.org> 0.10.2-1
+ Revision: 792674
- update to new version 0.10.2

* Mon Mar 12 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.10.1-2
+ Revision: 784454
- split out gir pkg
- converted BRs to pkgconfig provides
- fixed build
- rebuild
- cleaned up spec

* Tue Sep 06 2011 Götz Waschk <waschk@mandriva.org> 0.10.1-1
+ Revision: 698403
- new version

* Tue Aug 30 2011 Götz Waschk <waschk@mandriva.org> 0.10.0-1
+ Revision: 697460
- new version

* Sun Apr 10 2011 Götz Waschk <waschk@mandriva.org> 0.8.0-1
+ Revision: 652390
- update to new version 0.8.0

* Sat Dec 04 2010 Götz Waschk <waschk@mandriva.org> 0.7.1-1mdv2011.0
+ Revision: 609223
- update to new version 0.7.1

* Sat Oct 23 2010 Matthew Dawkins <mattydaw@mandriva.org> 0.6.2-1mdv2011.0
+ Revision: 587795
- new version 0.6.2

* Thu Sep 30 2010 Götz Waschk <waschk@mandriva.org> 0.6.1-1mdv2011.0
+ Revision: 582143
- update to new version 0.6.1

* Sun Sep 19 2010 Götz Waschk <waschk@mandriva.org> 0.6.0-1mdv2011.0
+ Revision: 579780
- update to new version 0.6.0

* Mon Sep 13 2010 Götz Waschk <waschk@mandriva.org> 0.5.9-2mdv2011.0
+ Revision: 577987
- rebuild for new g-i

* Mon Aug 16 2010 Götz Waschk <waschk@mandriva.org> 0.5.9-1mdv2011.0
+ Revision: 570280
- update to new version 0.5.9
- rebuild

* Wed Aug 04 2010 Götz Waschk <waschk@mandriva.org> 0.5.8-1mdv2011.0
+ Revision: 565698
- new version
- new source URL

* Sat Jul 31 2010 Funda Wang <fwang@mandriva.org> 0.5.7-2mdv2011.0
+ Revision: 563846
- rebuild for new gobject-introspection

* Sun Jul 11 2010 Götz Waschk <waschk@mandriva.org> 0.5.7-1mdv2011.0
+ Revision: 550675
- update to new version 0.5.7

* Mon Apr 12 2010 Götz Waschk <waschk@mandriva.org> 0.5.5-1mdv2010.1
+ Revision: 533732
- update build deps
- new version
- add introspection support

* Thu Feb 04 2010 Götz Waschk <waschk@mandriva.org> 0.5.4-1mdv2010.1
+ Revision: 500959
- update to new version 0.5.4

* Sun Nov 22 2009 Götz Waschk <waschk@mandriva.org> 0.5.2-1mdv2010.1
+ Revision: 469084
- update to new version 0.5.2

* Sun Sep 20 2009 Frederik Himpe <fhimpe@mandriva.org> 0.5.1-1mdv2010.0
+ Revision: 445564
- Update to new version 0.5.1 (new major)

* Wed Jun 17 2009 Götz Waschk <waschk@mandriva.org> 0.4.1-1mdv2010.0
+ Revision: 386876
- update to new version 0.4.1

* Fri Apr 24 2009 Götz Waschk <waschk@mandriva.org> 0.4-1mdv2010.0
+ Revision: 368987
- new version

* Fri Feb 06 2009 Götz Waschk <waschk@mandriva.org> 0.3.1-1mdv2009.1
+ Revision: 338042
- update to new version 0.3.1

* Thu Jan 15 2009 Götz Waschk <waschk@mandriva.org> 0.3-1mdv2009.1
+ Revision: 329665
- new version
- drop patch

* Tue Jan 13 2009 Götz Waschk <waschk@mandriva.org> 0.2.1-1mdv2009.1
+ Revision: 328910
- import gupnp-av


* Tue Jan 13 2009 Götz Waschk <waschk@mandriva.org> 0.2.1-1mdv2009.1
- fix format string
- adapt for Mandriva

* Thu Dec 18 2008 Peter Robinson <pbrobinson@gmail.com> 0.2.1-7
- Add gtk-doc build req

* Mon Dec 1 2008 Peter Robinson <pbrobinson@gmail.com> 0.2.1-6
- Fix directory ownership

* Sat Nov 22 2008 Peter Robinson <pbrobinson@gmail.com> 0.2.1-5
- Update package summary

* Mon Oct 20 2008 Peter Robinson <pbrobinson@gmail.com> 0.2.1-4
- Add some requires for the devel package

* Fri Aug 29 2008 Peter Robinson <pbrobinson@gmail.com> 0.2.1-3
- Some spec file cleanups

* Tue Jun 17 2008 Peter Robinson <pbrobinson@gmail.com> 0.2.1-2
- Fix build on rawhide

* Tue Jun 17 2008 Peter Robinson <pbrobinson@gmail.com> 0.2.1-1
- Initial release
