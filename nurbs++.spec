Summary:	NURBS++ library
Summary(pl):	Biblioteka NURBS++
Name:		nurbs++
Version:	3.0.11
Release:	4
License:	GPL
Group:		X11/Libraries
Source0:	http://dl.sourceforge.net/libnurbs/%{name}-%{version}.tar.bz2
# Source0-md5:	11aa7f2a1ae2bc3e2671d56f557fbbbf
Patch0:		%{name}-templates.patch
Patch1:		%{name}-link.patch
Patch2:		%{name}-magick.patch
Patch3:		%{name}-config.patch
Patch4:		%{name}-gcc33.patch
URL:		http://libnurbs.sourceforge.net/
BuildRequires:	ImageMagick-devel >= 5.2.9
BuildRequires:	OpenGL-devel
BuildRequires:	XFree86-devel >= 3.3.6
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.4d-3
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1

%description
Non-Uniform Rational B-Splines (NURBS) curves and surface are
parametric functions which can represent any type of curves or
surfaces. This C++ library hides the basic mathematics of NURBS. This
allows the user to focus on the more challenging parts of their
projects.

%description -l pl
Wymierne krzywe i powierzchnie sklejane NURBS (Non-Uniform Rational
B-Splines) s± funkcjami, które mog± przedstawiaæ dowolny rodzaj
krzywych lub powierzchni. Ta biblioteka C++ zawiera czê¶æ matematyczn±
tych funkcji. Pozwala programi¶cie skupiæ siê na innych czê¶ciach
projektów.

%package devel
Summary:	NURBS++ library development package
Summary(pl):	Pliki nag³ówkowe biblioteki NURBS++
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	ImageMagick-devel >= 5.2.9
Requires:	libstdc++-devel

%description devel
NURBS++ library header files.

%description devel -l pl
Pliki nag³ówkowe dla biblioteki NURBS++.

%package static
Summary:	NURBS++ static library
Summary(pl):	Statyczna wersja biblioteki NURBS++
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of NURBS++ library.

%description static -l pl
Statyczna wersja biblioteki NURBS++.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%{__libtoolize}
%{__aclocal} -I config
%{__autoconf}
%{__automake}
%configure \
	--enable-shared \
	--enable-static \
	--enable-exception \
	--enable-library \
	--with-x \
	--enable-float \
	--enable-double \
	--with-opengl \
	--with-magick \
	--disable-debug

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/nurbs++-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/nurbs++
%{_mandir}/man1/nurbs++-config.1*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
