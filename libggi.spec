# _with_glide - Build Glide support
# _with_kgicon - Build KGICon support
Summary:	GGI - Generic Graphics Interface	
Summary(pl):	GGI - Generic Graphics Interface
Name:		libggi
Version:	2.0b4
Release:	1
License:	BSD-like
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	ftp://ftp.ggi-project.org/pub/ggi/ggi/current/%{name}-%{version}.src.tar.bz2
Patch0:		%{name}-time.patch
Patch1:		%{name}-svga.patch
URL:		http://www.ggi-project.org/
BuildRequires:	libgii-devel
BuildRequires:	XFree86-devel
BuildRequires:	aalib-devel
BuildRequires:	ncurses-devel
%ifarch %{ix86}
BuildRequires:	svgalib-devel
%endif
%{?_with_glide:BuildRequires: glide-devel}
%{?_with_kgicon:BuildRequires: kgicon-devel}
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
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	%{name} = %{version}

%description aa
LibGGI target for displaying graphics using ascii-art-library.

%description -l pl aa
Modu³ LibGGI do obs³ugi grafiki poprzez bibliotekê ascii-art.

%ifarch %{ix86}
%package svgalib
Summary:	SVGALib target for LibGGI
Summary(pl):	Obs³uga SVGALib dla LibGGI
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	%{name} = %{version}

%description svgalib
LibGGI target for displaying via SVGALib.

%description -l pl svgalib
Modu³ LibGGI do obs³ugi grafiki poprzez bibliotekê SVGALib.
%endif

%package X11
Summary:	X11 targets for LibGGI
Summary(pl):	Obs³uga X11 dla LibGGI
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	%{name} = %{version}

%description X11
LibGGI targets for displaing in X:
 - x - graphics via X-protocol
 - xlib - graphics via X-library
 - dga - graphics via XFree86 DGA extension

%description -l pl X11
Modu³y LibGGI do obs³ugi grafiki w XWindow:
 - x - grafika poprzez protokó³ X
 - xlib - grafika poprzez bibliotekê xlib
 - dga - grafika poprzez rozszerzenie X DGA

%package glide
Summary:	Glide (3DFX) target for LibGGI
Summary(pl):	Obs³uga Glide (3DFX) dla LibGGI
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	%{name} = %{version}

%description glide
GGI Glide target.

%description -l pl glide
Modu³ do obs³ugi grafiki poprzez Glide.

%package programs
Summary:	Utilities and demos for GGI
Summary(pl):	Programy narzêdziowe i przyk³adowe dla LibGGI
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}
Obsoletes:	libggi-demos

%description programs
Various utilities and demos for GGI.

%description -l pl programs
Ró¿ne programy oraz dema dla GGI

%package devel
Summary:	Development part of LibGGI
Summary(pl):	Czê¶æ dla programistów biblioteki LibGGI
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Development part of LibGGI.

%description devel -l pl
Pliki potrzebne do programowania z wykorzystaniem LibGGI.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1

%build
CPPFLAGS="-I%{_includedir}/glide"; export CPPFLAGS 
./autogen.sh
%configure \
	%{?!debug:--disable-debug} \
	%{?!_with_glide:--disable-glide} \
	%{?!_with_kgicon:--disable-genkgi} \
%ifnarch %{ix86}
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

# demos which are nice, but not installed by make install
install programs/demos/.libs/flying_ggis $RPM_BUILD_ROOT%{_bindir}
install programs/demos/.libs/slimy $RPM_BUILD_ROOT%{_bindir}
install programs/demos/.libs/stars $RPM_BUILD_ROOT%{_bindir}

gzip -9nf README ChangeLog NEWS doc/*.txt

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz NEWS.gz doc/*.txt* 
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

%files aa
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ggi/display/aa.so

%ifarch %{ix86} 
%files svgalib
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ggi/display/svga*.so
%attr(755,root,root) %{_libdir}/ggi/display/vgagl.so
%endif

%files X11
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ggi/display/X*.so
%attr(755,root,root) %{_libdir}/ggi/display/xf86dga.so

%{?!_with_glide:#}%files glide
%{?!_with_glide:#}%attr(755,root,root) %{_libdir}/ggi/display/glide.so

%files programs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man6/*

%files devel
%defattr(644,root,root,755)
%doc ChangeLog.gz
%doc %{_examplesdir}/%{name}-%{version}

%{_includedir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/ggi/*/*.la
%attr(755,root,root) %{_libdir}/ggi/default/fbdev/*/*.la

%{_mandir}/man3/*
