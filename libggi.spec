Summary:	GGI - Generic Graphics Interface	
Summary(pl):	GGI - Generic Graphics Interface
Name:		libggi
Version:	2.0b2.1
Release:	3
License:	GPL
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	ftp://ftp.ggi-project.org/pub/ggi/ggi/current/%{name}-%{version}.tar.bz2
URL:		http://www.ggi-project.org/
BuildRequires:	libgii-devel
BuildRequires:	XFree86-devel
BuildRequires:	aalib-devel
BuildRequires:	svgalib-devel
#BuildRequires:	glide-devel
#BuildRequires:	kgicon-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LibGGI, the dynamic GGI (General Graphics Interface) library is a
flexible drawing library.

It provides an opaque interface to the display's acceleration
functions. It was originally intended to allow user programs to
interface with KGI, the GGI Kernel Graphics Interface, but other
display types can be easily used by loading the appropriate "display
target" (e.g. X, memory).

%package aa
Summary:	aalib target for LibGII
Summary(pl):	obs�uga aalib dla LibGII
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	%{name} = %{version}

%description aa
LibGGI target for displaying graphics using ascii-art-library.

%package svgalib
Summary:	SVGALib target for LibGII
Summary(pl):	obs�uga SVGALib dla LibGII
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	%{name} = %{version}

%description svgalib
LibGGI target for displaying via SVGALib.

%package X11
Summary:	X11 targets for LibGII
Summary(pl):	Obs�uga X11 dla LibGII
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	%{name} = %{version}

%description X11
LibGGI targets for displaing in X:
 - x - graphics via X-protocol
 - xlib - graphics via X-library
 - dga - graphics via XFree86 DGA extension

%package glide
Summary:	Glide (3DFX) target for LibGII
Summary(pl):	Obs�uga Glide (3DFX) dla LibGII
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	%{name} = %{version}

%description glide
GGI Glide target.

%package programs
Summary:	Utilities and demos for GGI
Summary(pl):	Programy narz�dziowe i przyk�adowe dla LibGGI
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}
Obsoletes:	libggi-demos

%description programs
Various utilities and demos for GGI.

%package devel
Summary:	Development part of LibGII
Summary(pl):	Cz�� dla programist�w biblioteki LibGII
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Development part of LibGII.

%description devel -l pl
Pliki potrzebne do programowania z wykorzystaniem LibGII.

%prep
%setup -q

%build
CPPFLAGS="-I/usr/include/glide"; export CPPFLAGS 
%configure \
	--disable-debug \
	--disable-glide \
	--disable-genkgi \
	--sysconfdir=%{_sysconfdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/src/examples/%{name}

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT"

install programs/demos/*.c $RPM_BUILD_ROOT%{_prefix}/src/examples/%{name}

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
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ggi/display/aa.so

%files svgalib
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ggi/display/svgalib.so
%attr(755,root,root) %{_libdir}/ggi/display/svgalib-misc.so
%attr(755,root,root) %{_libdir}/ggi/display/vgagl.so

%files X11
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ggi/display/X*.so
%attr(755,root,root) %{_libdir}/ggi/display/xf86dga.so

#%files glide
#%attr(755,root,root) %{_libdir}/ggi/display/glide.so

%files programs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man6/*

%files devel
%defattr(644,root,root,755)
%doc ChangeLog.gz
%doc %{_prefix}/src/examples/%{name}

%{_includedir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/ggi/*/*.la
%attr(755,root,root) %{_libdir}/ggi/default/fbdev/*/*.la

%{_mandir}/man3/*
