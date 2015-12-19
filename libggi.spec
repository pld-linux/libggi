#
# Conditional build:
%bcond_with	directfb	# DirectFB drivers support for fbdev [outdated, patch incomplete]
%bcond_with	glide		# Glide support
%bcond_with	kgicon		# KGICon support
%bcond_without	aalib		# aalib support
%bcond_with	svga		# svgalib support
%bcond_with	static_modules	# build static library AND make all modules builtin (also in shared lib)
#
Summary:	GGI - Generic Graphics Interface
Summary(pl.UTF-8):	GGI - Generic Graphics Interface
Name:		libggi
Version:	2.2.2
Release:	9
Epoch:		1
License:	BSD-like
Group:		Libraries
Source0:	http://www.ggi-project.org/ftp/ggi/v2.2/%{name}-%{version}.src.tar.bz2
# Source0-md5:	51d92ea810dad5360f6f0d02dd8b84a4
Patch0:		%{name}-ppc.patch
Patch1:		ac.patch
Patch2:		link.patch
Patch3:		%{name}-directfb.patch
Patch4:		%{name}-glide.patch
Patch5:		%{name}-security.patch
URL:		http://www.ggi-project.org/
%{?with_directfb:BuildRequires:	DirectFB-devel >= 1.4.15}
%{?with_glide:BuildRequires:	Glide2x-devel}
%{?with_aalib:BuildRequires:	aalib-devel}
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	libgii-devel >= 1.0.2
BuildRequires:	libtool >= 2:2.0
BuildRequires:	ncurses-devel
%{?with_svga:BuildRequires:	svgalib-devel}
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXxf86dga-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
Requires:	libgii >= 1.0.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LibGGI, the dynamic GGI (General Graphics Interface) library is a
flexible drawing library.

It provides an opaque interface to the display's acceleration
functions. It was originally intended to allow user programs to
interface with KGI, the GGI Kernel Graphics Interface, but other
display types can be easily used by loading the appropriate "display
target" (e.g. X, memory).

%description -l pl.UTF-8
LibGGI, dynamiczne GGI (General Graphics Interface - Generalny
Interfejs Graficzny) jest biblioteką obsługi grafiki.

Dostarcza ona jednolity interfejs do akcelerowanych funkcji
wyświetlania. Oryginalnie biblioteka została stworzona do
współdziałania z KGI (GGI Kernel Graphic Interface) ale inne
sterowniki wyświetlania mogą być łatwo używane.

%package X11
Summary:	X11 targets for LibGGI
Summary(pl.UTF-8):	Obsługa X11 dla LibGGI
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description X11
LibGGI targets for displaing in X:
 - x - graphics via X-protocol
 - xlib - graphics via X-library
 - dga - graphics via XFree86 DGA extension

%description X11 -l pl.UTF-8
Moduły LibGGI do obsługi grafiki w XWindow:
 - x - grafika poprzez protokół X
 - xlib - grafika poprzez bibliotekę xlib
 - dga - grafika poprzez rozszerzenie X DGA

%package aa
Summary:	aalib target for LibGGI
Summary(pl.UTF-8):	Obsługa aalib dla LibGGI
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description aa
LibGGI target for displaying graphics using ascii-art-library.

%description aa -l pl.UTF-8
Moduł LibGGI do obsługi grafiki poprzez bibliotekę ascii-art.

%package directfb
Summary:	DirectFB drivers support for LibGGI fbdev target
Summary(pl.UTF-8):	Obsługa sterowników DirectFB w sterowniku fbdev LibGGI
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description directfb
DirectFB drivers support for LibGGI fbdev target.

%description directfb -l pl.UTF-8
Obsługa sterowników DirectFB w sterowniku LibGGI fbdev.

%package glide
Summary:	Glide (3DFX) target for LibGGI
Summary(pl.UTF-8):	Obsługa Glide (3DFX) dla LibGGI
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description glide
GGI Glide target.

%description glide -l pl.UTF-8
Moduł do obsługi grafiki poprzez Glide.

%package svgalib
Summary:	SVGALib target for LibGGI
Summary(pl.UTF-8):	Obsługa SVGALib dla LibGGI
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description svgalib
LibGGI target for displaying via SVGALib.

%description svgalib -l pl.UTF-8
Moduł LibGGI do obsługi grafiki poprzez bibliotekę SVGALib.

%package programs
Summary:	Utilities and demos for GGI
Summary(pl.UTF-8):	Programy narzędziowe i przykładowe dla LibGGI
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	libggi-demos

%description programs
Various utilities and demos for GGI.

%description programs -l pl.UTF-8
Różne programy oraz dema dla GGI

%package devel
Summary:	Development part of LibGGI
Summary(pl.UTF-8):	Część dla programistów biblioteki LibGGI
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	libgii-devel >= 1.0.2
%if %{with static_modules}
%{?with_aalib:Requires:	aalib-devel}
%{?with_glide:Requires:	glide-devel}
Requires:	ncurses-devel
%{?with_svga:Requires:	svgalib-devel}
Requires:	xorg-lib-libX11-devel
Requires:	xorg-lib-libXext-devel
Requires:	xorg-lib-libXxf86dga-devel
Requires:	xorg-lib-libXxf86vm-devel
%endif

%description devel
Development part of LibGGI.

%description devel -l pl.UTF-8
Pliki potrzebne do programowania z wykorzystaniem LibGGI.

%package static
Summary:	Static libggi library
Summary(pl.UTF-8):	Statyczna biblioteka libggi
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libggi library.

%description static -l pl.UTF-8
Statyczna biblioteka libggi.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%{__rm} acinclude.m4 m4/{libtool,lt*}.m4

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__autoconf}
%{__automake}
CPPFLAGS="%{rpmcppflags} %{?with_glide:-I/usr/include/glide} %{?with_directfb:-I/usr/include/directfb -I/usr/include/directfb-internal}"
%configure \
	%{!?with_aalib:--disable-aa} \
	%{!?debug:--disable-debug} \
	%{!?with_glide:--disable-glide} \
	%{!?with_kgicon:--disable-kgi} \
	%{!?with_directfb:--disable-directfb}%{?with_directfb:--with-directfb=%{_libdir}/directfb-1.4-6/gfxdrivers} \
	%{!?with_static_modules:--disable-static} \
	%{!?with_svga:--disable-svga --disable-vgagl}
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

%{__rm} $RPM_BUILD_ROOT%{_libdir}/ggi/{default,default/fbdev,display,helper}/*.la

# displays not supported on Linux
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man7/display-{directx,quartz,vgl}.7

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc FAQ NEWS README doc/*.txt
%dir %{_sysconfdir}/ggi
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ggi/libggi.conf
%dir %{_sysconfdir}/ggi/targets
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ggi/targets/fbdev.conf
%attr(755,root,root) %{_libdir}/libggi.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libggi.so.2
%dir %{_libdir}/ggi/default
%dir %{_libdir}/ggi/default/fbdev
%attr(755,root,root) %{_libdir}/ggi/default/fbdev/fbdev_m2164w.so
%attr(755,root,root) %{_libdir}/ggi/default/fbdev/fbdev_mach64.so
%attr(755,root,root) %{_libdir}/ggi/default/fbdev/fbdev_mga_g400.so
%attr(755,root,root) %{_libdir}/ggi/default/color.so
%attr(755,root,root) %{_libdir}/ggi/default/ilbm.so
%attr(755,root,root) %{_libdir}/ggi/default/iplanar_2p.so
%attr(755,root,root) %{_libdir}/ggi/default/linear_1.so
%attr(755,root,root) %{_libdir}/ggi/default/linear_16.so
%attr(755,root,root) %{_libdir}/ggi/default/linear_1_r.so
%attr(755,root,root) %{_libdir}/ggi/default/linear_2.so
%attr(755,root,root) %{_libdir}/ggi/default/linear_24.so
%attr(755,root,root) %{_libdir}/ggi/default/linear_32.so
%attr(755,root,root) %{_libdir}/ggi/default/linear_4.so
%attr(755,root,root) %{_libdir}/ggi/default/linear_4_r.so
%attr(755,root,root) %{_libdir}/ggi/default/linear_8.so
%attr(755,root,root) %{_libdir}/ggi/default/planar.so
%attr(755,root,root) %{_libdir}/ggi/default/pseudo_stubs.so
%attr(755,root,root) %{_libdir}/ggi/default/stubs.so
%attr(755,root,root) %{_libdir}/ggi/default/text_16.so
%attr(755,root,root) %{_libdir}/ggi/default/text_32.so
%dir %{_libdir}/ggi/display
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
%{_mandir}/man7/display-auto.7*
%{_mandir}/man7/display-fbdev.7*
%{_mandir}/man7/display-file.7*
%{_mandir}/man7/display-mansync.7*
%{_mandir}/man7/display-memory.7*
%{_mandir}/man7/display-monotext.7*
%{_mandir}/man7/display-multi.7*
%{_mandir}/man7/display-palemu.7*
%{_mandir}/man7/display-sub.7*
%{_mandir}/man7/display-tele.7*
%{_mandir}/man7/display-terminfo.7*
%{_mandir}/man7/display-tile.7*
%{_mandir}/man7/display-trueemu.7*
%{_mandir}/man7/display-vcsa.7*
%{_mandir}/man7/libggi.7*

%files X11
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ggi/display/X.so
%dir %{_libdir}/ggi/helper
%attr(755,root,root) %{_libdir}/ggi/helper/helper_x_dbe.so
%attr(755,root,root) %{_libdir}/ggi/helper/helper_x_dga.so
%attr(755,root,root) %{_libdir}/ggi/helper/helper_x_evi.so
%attr(755,root,root) %{_libdir}/ggi/helper/helper_x_shm.so
%attr(755,root,root) %{_libdir}/ggi/helper/helper_x_vidmode.so
%{_mandir}/man7/display-x.7*

%if %{with aalib}
%files aa
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ggi/display/aa.so
%{_mandir}/man7/display-aa.7*
%endif

%if %{with directfb}
%files directfb
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ggi/default/fbdev/fbdev_directfb.so
%attr(755,root,root) %{_libdir}/ggi/default/fbdev/fbdev_directfbglobal.so
%endif

%if %{with glide}
%files glide
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ggi/display/glide.so
%{_mandir}/man7/display-glide.7*
%endif

%if %{with svga}
%files svgalib
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ggi/display/svgalib.so
%attr(755,root,root) %{_libdir}/ggi/display/vgagl.so
%{_mandir}/man7/display-svgalib.7*
%endif

%files programs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cube3d
%attr(755,root,root) %{_bindir}/flying_ggis
%attr(755,root,root) %{_bindir}/ggiteleserver
%attr(755,root,root) %{_bindir}/monitest
%attr(755,root,root) %{_bindir}/slimy
%attr(755,root,root) %{_bindir}/stars
%{_mandir}/man1/cube3d.1*
%{_mandir}/man1/demo.1*
%{_mandir}/man1/ggi-demo.1*
%{_mandir}/man1/ggiteleserver.1*
%{_mandir}/man1/monitest.1*

%files devel
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_libdir}/libggi.so
%{_libdir}/libggi.la
%{_includedir}/ggi/*.h
%{_includedir}/ggi/display
%{_includedir}/ggi/internal/*.h
%{_mandir}/man3/ggi*.3*
%{_mandir}/man7/ggidev-triple-int.7*
%{_examplesdir}/%{name}-%{version}

%if %{with static_modules}
%files static
%defattr(644,root,root,755)
%{_libdir}/libggi.a
%endif
