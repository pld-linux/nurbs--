Summary:	NURBS++ library
Summary(pl):	Biblioteka NURBS++
Name:		nurbs++
Version:	3.0.10
Release:	3
License:	GPL
Group:		X11/Libraries
Source0:	ftp://download.sourceforge.net/pub/sourceforge/libnurbs/%{name}-%{version}.tar.bz2
Patch0:		%{name}-templates.patch
Patch1:		%{name}-magick.patch
Patch2:		%{name}-link.patch
URL:		http://yukon.genie.uottawa.ca/~lavoie/software/nurbs/
BuildRequires:	OpenGL-devel
BuildRequires:	XFree86-devel >= 3.3.6
BuildRequires:	ImageMagick-devel >= 5.2.9
BuildRequires:	libstdc++-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
Requires:	OpenGL
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1
%define		_prefix		/usr/X11R6

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
Requires:	%{name} = %{version}

%description devel
NURBS++ library header files.

%description devel -l pl
Pliki nag³ówkowe dla biblioteki NURBS++.

%package static
Summary:	NURBS++ static library
Summary(pl):	Statyczna wersja biblioteki NURBS++
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static version of NURBS++ library.

%description static -l pl
Statyczna wersja biblioteki NURBS++.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
libtoolize --copy --force
aclocal
autoconf
automake -a -c -f
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

%{__make} DESTDIR=$RPM_BUILD_ROOT install

# remove unwanted paths from libtool scripts
for f in $RPM_BUILD_ROOT%{_libdir}/lib{matrixN,matrixI,nurbsf,nurbsd}.la ; do
	cat $f | awk '/^dependency_libs/ { gsub("-L[ \t]*[^ \t]*nurbs\+\+-[^ \t]* ","") } //' >$f.tmp
	mv -f $f.tmp $f
done

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/nurbs++

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
