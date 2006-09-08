#
# Conditional build:
%bcond_with	glide	# with Glide support
%bcond_with	kgicon	# with KGICon support
%bcond_without	aalib	# without aalib support
%bcond_without	svga	# without svgalib support
#
Summary:	GGI - Generic Graphics Interface
Summary(pl):	GGI - Generic Graphics Interface
Name:		libggi
Version:	2.1.2
Release:	2
Epoch:		1
License:	BSD-like
Group:		Libraries
Source0:	http://www.ggi-project.org/ftp/ggi/v2.1/%{name}-%{version}.src.tar.bz2
# Source0-md5:	f29e844011425ab14706e31a4cdee181
Patch0:		%{name}-ppc.patch
Patch1:		%{name}-gcc4.1.patch
Patch2:		%{name}-gcc4.patch
Patch3:		%{name}-glibc24.patch
URL:		http://www.ggi-project.org/
%{?with_aalib:BuildRequires:	aalib-devel}
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_glide:BuildRequires:	glide-devel}
BuildRequires:	libgii-devel >= 0.9.2
BuildRequires:	libtool >= 1:1.4.2-9
BuildRequires:	ncurses-devel
%{?with_svga:BuildRequires:	svgalib-devel}
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXxf86dga-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
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
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description aa
LibGGI target for displaying graphics using ascii-art-library.

%description aa -l pl
Modu³ LibGGI do obs³ugi grafiki poprzez bibliotekê ascii-art.

%package svgalib
Summary:	SVGALib target for LibGGI
Summary(pl):	Obs³uga SVGALib dla LibGGI
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description svgalib
LibGGI target for displaying via SVGALib.

%description svgalib -l pl
Modu³ LibGGI do obs³ugi grafiki poprzez bibliotekê SVGALib.

%package X11
Summary:	X11 targets for LibGGI
Summary(pl):	Obs³uga X11 dla LibGGI
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

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
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description glide
GGI Glide target.

%description glide -l pl
Modu³ do obs³ugi grafiki poprzez Glide.

%package programs
Summary:	Utilities and demos for GGI
Summary(pl):	Programy narzêdziowe i przyk³adowe dla LibGGI
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	libggi-demos

%description programs
Various utilities and demos for GGI.

%description programs -l pl
Ró¿ne programy oraz dema dla GGI

%package devel
Summary:	Development part of LibGGI
Summary(pl):	Czê¶æ dla programistów biblioteki LibGGI
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	libgii-devel >= 0.9.2

%description devel
Development part of LibGGI.

%description devel -l pl
Pliki potrzebne do programowania z wykorzystaniem LibGGI.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p0
%patch3 -p1

rm -f m4/{libtool,ltdl}.m4

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__autoconf}
%{__automake}
CPPFLAGS="-I/usr/include/glide -I/usr/include/directfb -I/usr/include/directfb-internal"
%configure \
	%{!?debug:--disable-debug} \
	%{!?with_glide:--disable-glide} \
	%{!?with_kgicon:--disable-genkgi} \
	--disable-directfb \
	%{!?with_svga:--disable-svga --disable-vgagl} \
	%{!?with_aalib:--disable-aa} \
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

rm -f $RPM_BUILD_ROOT%{_libdir}/ggi/{default,default/fbdev/*,display,helper}/*.la

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

%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ggi/*.conf
%dir %{_sysconfdir}/ggi/targets
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ggi/targets/*.conf

%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_libdir}/ggi/default/fbdev/*/*.so
%attr(755,root,root) %{_libdir}/ggi/default/*.so
%attr(755,root,root) %{_libdir}/ggi/display/auto.so
%attr(755,root,root) %{_libdir}/ggi/display/fbdev.so
%attr(755,root,root) %{_libdir}/ggi/display/file.so
%attr(755,root,root) %{_libdir}/ggi/display/ipc.so
%ifarch ppc
%attr(755,root,root) %{_libdir}/ggi/display/lcd823.so
%endif
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

%if %{with aalib}
%files aa
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ggi/display/aa.so
%endif

%if %{with svga}
%files svgalib
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ggi/display/svga*.so
%attr(755,root,root) %{_libdir}/ggi/display/vgagl.so
%endif

%files X11
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ggi/display/X*.so
%attr(755,root,root) %{_libdir}/ggi/display/xf86dga.so
%dir %{_libdir}/ggi/helper
%attr(755,root,root) %{_libdir}/ggi/helper/helper_x_*.so

%if %{with glide}
%files glide
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ggi/display/glide.so
%endif

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
