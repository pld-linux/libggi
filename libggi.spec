Summary:	GGI - Generic Graphics Interface	
Summary(pl):	GGI - Generic Graphics Interface
Name:		libggi
Version:	2.0b2.1
Release:	1
Group:		Libraries
Group(pl):	Biblioteki
Copyright:	GPL
Source0:	ftp://ftp.ggi-project.org/pub/ggi/ggi/current/%{name}-%{version}.tar.bz2
URL:		http://www.ggi-project.org/
BuildRequires:	libgii-devel
BuildRequires:	XFree86-devel
BuildRequires:	aalib-devel
BuildRequires:	svgalib-devel
#BuildPrereq:   glide-devel
BuildRequires:    kgicon-devel
BuildRoot:   	/tmp/%{name}-%{version}-root

%description
LibGGI, the dynamic GGI (General Graphics Interface) library is a flexible
drawing library.

It provides an opaque interface to the display's acceleration functions. It
was originally intended to allow user programs to interface with KGI, the
GGI Kernel Graphics Interface, but other display types can be easily used by
loading the appropriate "display target" (e.g. X, memory).

%description -l pl

%package aa
Summary:	aalib target for LibGII
Summary(pl):	obs³uga aalib dla LibGII
Group:		Libraries
Group(pl):	Biblioteki
Requires:	%{name} = %{version}

%description aa
LibGGI target for displaying graphics using ascii-art-library

%package svgalib
Summary:	SVGALib target for LibGII
Summary(pl):	obs³uga SVGALib dla LibGII
Group:		Libraries
Group(pl):	Biblioteki
Requires:	%{name} = %{version}

%description svgalib
LibGGI target for displaying via SVGALib

%package X11
Summary:	X11 targets for LibGII
Summary(pl):	Obs³uga X11 dla LibGII
Group:		Libraries
Group(pl):	Biblioteki
Requires:	%{name} = %{version}

%description X11
LibGGI targets for displaing in X:
  x - graphics via X-protocol
  xlib - graphics via X-library
  dga - graphics via XFree86 DGA extension

#%package glide
#Summary:	Glide (3DFX) target for LibGII
#Summary(pl):	Obs³uga Glide (3DFX) dla LibGII
#Group:		Libraries
#Group(pl):	Biblioteki
#Requires:	%{name} = %{version}

#%description glide

%package programs
Summary:	Utilities and demos for GGI
Summary(pl):	Programy narzêdziowe i przyk³adowe dla LibGGI
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description programs
Various utilities and demos for GGI

%package devel
Summary:	Development part of LibGII
Summary(pl):	Czê¶æ dla programistów biblioteki LibGII
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Development part of LibGII.

%description devel -l pl
Pliki potrzebne do programowania z wykorzystaniem LibGII.

%prep
%setup  -q

%build
LDFLAGS="-s" ; export LDFLAGS
%configure \
	--disable-debug \
	--disable-glide \
	--sysconfdir=%{_sysconfdir}
make

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/usr/src/examples/%{name}

make install \
	DESTDIR="$RPM_BUILD_ROOT"

install programs/demos/*.c $RPM_BUILD_ROOT/usr/src/examples/%{name}

# demos which are nice, but not installed by make install
install programs/demos/.libs/flying_ggis $RPM_BUILD_ROOT%{_bindir}
install programs/demos/.libs/slimy $RPM_BUILD_ROOT%{_bindir}
install programs/demos/.libs/stars $RPM_BUILD_ROOT%{_bindir}

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man*/* \
	README ChangeLog NEWS doc/*.txt

%pre

%preun

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz NEWS.gz
%dir %{_libdir}/ggi
%dir %{_libdir}/ggi/default
%dir %{_libdir}/ggi/default/fbdev
%dir %{_libdir}/ggi/default/fbdev/*
%dir %{_libdir}/ggi/display

%{_sysconfdir}/ggi
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_libdir}/ggi/default/fbdev/*/*.so
%attr(755,root,root) %{_libdir}/ggi/default/*.so
%attr(755,root,root) %{_libdir}/ggi/display/fbdev.so
%attr(755,root,root) %{_libdir}/ggi/display/file.so
%attr(755,root,root) %{_libdir}/ggi/display/lin_vtsw.so
%attr(755,root,root) %{_libdir}/ggi/display/mansync.so
%attr(755,root,root) %{_libdir}/ggi/display/memory.so
%attr(755,root,root) %{_libdir}/ggi/display/monotext.so
%attr(755,root,root) %{_libdir}/ggi/display/multi.so
%attr(755,root,root) %{_libdir}/ggi/display/palemu.so
%attr(755,root,root) %{_libdir}/ggi/display/sub.so
%attr(755,root,root) %{_libdir}/ggi/display/tele.so
%attr(755,root,root) %{_libdir}/ggi/display/terminfo.so
%attr(755,root,root) %{_libdir}/ggi/display/tile.so
%attr(755,root,root) %{_libdir}/ggi/display/trueemu.so
%attr(755,root,root) %{_libdir}/ggi/display/vcsa.so

%{_mandir}/man7/*

%files aa
%attr(755,root,root) %{_libdir}/ggi/display/aa.so

%files svgalib
%attr(755,root,root) %{_libdir}/ggi/display/svgalib.so

%files X11
%attr(755,root,root) %{_libdir}/ggi/display/X*.so
%attr(755,root,root) %{_libdir}/ggi/display/xf86dga.so

#%files glide
#%attr(755,root,root) %{_libdir}/ggi/display/glide.so

%files programs
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man6/*

%files devel
%defattr(644,root,root,755)
%doc doc/*.txt* ChangeLog.gz
%doc /usr/src/examples/%{name}

%{_includedir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/ggi/*/*.la
%attr(755,root,root) %{_libdir}/ggi/default/fbdev/*/*.la

%{_mandir}/man3/*
