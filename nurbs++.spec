#
# Conditional build:
%bcond_with	cppunit	# use cppunit; doesn't build with current cppunit
#
Summary:	NURBS++ library
Summary(pl.UTF-8):   Biblioteka NURBS++
Name:		nurbs++
Version:	3.0.11
Release:	8
License:	GPL
Group:		X11/Libraries
Source0:	http://dl.sourceforge.net/libnurbs/%{name}-%{version}.tar.bz2
# Source0-md5:	11aa7f2a1ae2bc3e2671d56f557fbbbf
Patch0:		%{name}-link.patch
Patch1:		%{name}-magick.patch
Patch2:		%{name}-config.patch
Patch3:		%{name}-strict_types.patch
Patch4:		%{name}-gcc4.patch
URL:		http://libnurbs.sourceforge.net/
BuildRequires:	ImageMagick-devel >= 1:6.2.4.0
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake
%if %{with cppunit}
BuildRequires:	cppunit-devel
%endif
BuildRequires:	libstdc++-devel >= 5:3.4
BuildRequires:	libtool >= 2:1.4d-3
BuildRequires:	xorg-lib-libX11-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1

%description
Non-Uniform Rational B-Splines (NURBS) curves and surface are
parametric functions which can represent any type of curves or
surfaces. This C++ library hides the basic mathematics of NURBS. This
allows the user to focus on the more challenging parts of their
projects.

%description -l pl.UTF-8
Wymierne krzywe i powierzchnie sklejane NURBS (Non-Uniform Rational
B-Splines) są funkcjami, które mogą przedstawiać dowolny rodzaj
krzywych lub powierzchni. Ta biblioteka C++ zawiera część matematyczną
tych funkcji. Pozwala programiście skupić się na innych częściach
projektów.

%package devel
Summary:	NURBS++ library development package
Summary(pl.UTF-8):   Pliki nagłówkowe biblioteki NURBS++
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	ImageMagick-devel >= 1:6.2.4.0
Requires:	libstdc++-devel >= 5:3.4

%description devel
NURBS++ library header files.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla biblioteki NURBS++.

%package static
Summary:	NURBS++ static library
Summary(pl.UTF-8):   Statyczna wersja biblioteki NURBS++
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of NURBS++ library.

%description static -l pl.UTF-8
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
%if !%{with cppunit}
export has_cppunit=no
%endif
%configure \
	--disable-debug \
	--enable-double \
	--enable-exception \
	--enable-float \
	--enable-library \
	--enable-shared \
	--enable-static \
	--with-magick \
	--with-opengl \
	--with-x

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
