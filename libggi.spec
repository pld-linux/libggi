#
# Conditional build:
# _with_glide	    - with Glide support
# _with_kgicon	    - with KGICon support
# _without_aalib    - without aalib support
# _without_svgalib  - without svgalib support
#
Summary:	GGI - Generic Graphics Interface
Summary(pl):	GGI - Generic Graphics Interface
Name:		libggi
Version:	2.0.3
Release:	1
Epoch:		1
License:	BSD-like
Group:		Libraries
Source0:	http://www.ggi-project.org/ftp/ggi/current/%{name}-%{version}.src.tar.bz2
# Source0-md5:	89a723c041a123110cad167d37f1a192
Patch0:		%{name}-amfix.patch
Patch1:		%{name}-gcc33.patch
URL:		http://www.ggi-project.org/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
%{!?_without_aalib:BuildRequires:	aalib-devel}
BuildRequires:	libgii-devel
BuildRequires:	libtool >= 1:1.4.2-9
BuildRequires:	ncurses-devel
%ifarch %{ix86} alpha
%{!?_without_svgalib:BuildRequires:	svgalib-devel}
%endif
%{?_with_glide:BuildRequires:	glide-devel}
%{?_with_kgicon:BuildRequires:	kgicon-devel}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LibGGI, the dynamic GGI (General Graphics Interface) library is a
flexible drawing library.

It provides an opaque interface to the display's acceleration
functions. It was originally intended to allow user programs to
interface with KGI, the GGI Kernel Graphics Interface, but other
display types can be easily used by loading the appropriate "display
target" (e.g. X, memory).

%description -l pl
LibGGI, dynamiczne GGI (General Graphics Interface - Generalny
Interfejs Graficzny) jest bibliotek± obs³ugi grafiki.

Dostarcza ona jednolity interfejs do akcelerowanych funkcji
wy¶wietlania. Oryginalnie biblioteka zosta³a stworzona do
wspó³dzia³ania z KGI (GGI Kernel Graphic Interface) ale inne
sterowniki wy¶wietlania mog± byæ ³atwo u¿ywane.

%package aa
Summary:	aalib target for LibGGI
Summary(pl):	Obs³uga aalib dla LibGGI
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}

%description aa
LibGGI target for displaying graphics using ascii-art-library.

%description aa -l pl
Modu³ LibGGI do obs³ugi grafiki poprzez bibliotekê ascii-art.

%package svgalib
Summary:	SVGALib target for LibGGI
Summary(pl):	Obs³uga SVGALib dla LibGGI
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}

%description svgalib
LibGGI target for displaying via SVGALib.

%description svgalib -l pl
Modu³ LibGGI do obs³ugi grafiki poprzez bibliotekê SVGALib.

%package X11
Summary:	X11 targets for LibGGI
Summary(pl):	Obs³uga X11 dla LibGGI
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}

%description X11
LibGGI targets for displaing in X:
 - x - graphics via X-protocol
 - xlib - graphics via X-library
 - dga - graphics via XFree86 DGA extension

%description X11 -l pl
Modu³y LibGGI do obs³ugi grafiki w XWindow:
 - x - grafika poprzez protokó³ X
 - xlib - grafika poprzez bibliotekê xlib
 - dga - grafika poprzez rozszerzenie X DGA

%package glide
Summary:	Glide (3DFX) target for LibGGI
Summary(pl):	Obs³uga Glide (3DFX) dla LibGGI
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}

%description glide
GGI Glide target.

%description glide -l pl
Modu³ do obs³ugi grafiki poprzez Glide.

%package programs
Summary:	Utilities and demos for GGI
Summary(pl):	Programy narzêdziowe i przyk³adowe dla LibGGI
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}
Obsoletes:	libggi-demos

%description programs
Various utilities and demos for GGI.

%description programs -l pl
Ró¿ne programy oraz dema dla GGI

%package devel
Summary:	Development part of LibGGI
Summary(pl):	Czê¶æ dla programistów biblioteki LibGGI
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}
Requires:	libgii-devel

%description devel
Development part of LibGGI.

%description devel -l pl
Pliki potrzebne do programowania z wykorzystaniem LibGGI.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
rm -f m4/libtool.m4
head -114 acinclude.m4 | tail +71 > m4/gii.m4
cat m4/*.m4 > acinclude.m4
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
CPPFLAGS="-I/usr/include/glide -I/usr/include/directfb -I/usr/include/directfb-internal"
%configure \
	%{?!debug:--disable-debug} \
	%{?!_with_glide:--disable-glide} \
	%{?!_with_kgicon:--disable-genkgi} \
	--disable-directfb \
	%{?_without_svgalib:--disable-svga} \
	%{?_without_aalib:--disable-aa} \
%ifnarch %{ix86} alpha
	--disable-svga \
	--disable-vgagl \
%endif
	--sysconfdir=%{_sysconfdir} \
	--enable-threads
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT"

install programs/demos/*.c $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install programs/demos/Makefile $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install config.h $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# demos which are nice, but not installed by make install
install programs/demos/.libs/flying_ggis $RPM_BUILD_ROOT%{_bindir}
install programs/demos/.libs/slimy $RPM_BUILD_ROOT%{_bindir}
install programs/demos/.libs/stars $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README NEWS doc/*.txt
%dir %{_libdir}/ggi/default
%dir %{_libdir}/ggi/default/fbdev
%dir %{_libdir}/ggi/default/fbdev/*
%dir %{_libdir}/ggi/display

%{_sysconfdir}/ggi/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_libdir}/ggi/default/fbdev/*/*.so
%attr(755,root,root) %{_libdir}/ggi/default/*.so
%attr(755,root,root) %{_libdir}/ggi/display/fbdev.so
%attr(755,root,root) %{_libdir}/ggi/display/file.so
%attr(755,root,root) %{_libdir}/ggi/display/linvtsw.so
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

%if %{!?_without_aalib:1}0
%files aa
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ggi/display/aa.so
%endif

%if %{!?_without_svgalib:1}0
%ifarch %{ix86} alpha
%files svgalib
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ggi/display/svga*.so
%attr(755,root,root) %{_libdir}/ggi/display/vgagl.so
%endif
%endif

%files X11
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ggi/display/X*.so
%attr(755,root,root) %{_libdir}/ggi/display/xf86dga.so
%dir %{_libdir}/ggi/helper
%attr(755,root,root) %{_libdir}/ggi/helper/helper_x_*.so

%{?!_with_glide:#}%files glide
%{?!_with_glide:#}%attr(755,root,root) %{_libdir}/ggi/display/glide.so

%files programs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%doc ChangeLog
%{_includedir}/ggi/*.h
%{_includedir}/ggi/display
%{_includedir}/ggi/internal/*.h
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
