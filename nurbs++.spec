Summary:	NURBS Library
Summary(pl):	Biblioteka NURBS
Name:		nurbs++
Version:	3.0.10
Release:	1
License:	GPL
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(fr):	Librairies
Group(pl):	X11/Biblioteki
Source0:	ftp://download.sourceforge.net/pub/sourceforge/libnurbs/%{name}-%{version}.tar.bz2
Patch0:		%{name}-remove-nurbsGL.patch
URL:		http://yukon.genie.uottawa.ca/~lavoie/software/nurbs/
BuildRequires:	OpenGL-devel
BuildRequires:	XFree86-devel >= 3.3.6
BuildRequires:	ImageMagick-devel >= 4.2.8
BuildRequires:	libstdc++-devel
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Non-Uniform Rational B-Splines (NURBS) curves and surface are
parametric functions which can represent any type of curves or
surfaces. This C++ library hides the basic mathematics of NURBS. This
allows the user to focus on the more challenging parts of their
projects.

%package devel
Summary:	LibNURBS development
Summary(pl):	LibNURBS 
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
LibNURBS++ header files.

%description -l pl devel
Pliki nag³ówkowe dla biblioteki nurbs++.

%package static
Summary:	LibNURBS++ static
Summary(pl):	Statyczna wersja biblioteki nurbs++
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
nurbs++ static version.

%description -l pl static
Statycznie linkowana wersja biblioteki nurbs++.

%prep
%setup -q
%patch0 -p0

%build
aclocal
autoconf
automake -a -c
%configure \
	--enable-shared \
	--enable-static \
	--enable-exception \
	--enable-library \
	--with-x \
	--enable-float \
	--enable-double \
	--without-opengl \
	--without-magick \
	--disable-debug 
    
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%attr(644,root,root) %{_includedir}/nurbs++

%files static
%defattr(644,root,root,755)
%attr(644,root,root) %{_libdir}/lib*.a
