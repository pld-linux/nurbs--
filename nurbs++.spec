Summary:	NURBS Library
Summary(pl):	Biblioteka NURBS
Name:		libnurbs++
Version:	3.0.10
Release:	1
Copyright:	GPL
Group:		X11/Libraries
Group(pl):	X11/Biblioteki
Source0:	http://download.sourceforge.net/libnurbs/nurbs++-%{version}.tar.bz2
#Patch0:		
BuildRequires:	OpenGL-devel
BuildRequires:	XFree86-devel >= 3.3.6
BuildRequires:	ImageMagick-devel >= 4.2.8
#BuildRequires:	
#Requires:	
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_prefix	/usr/X11R6

%description

%description -l pl

%package devel
Summary:	LibNURBS development
Summary(pl):	LibNURBS 
Group:		X11/Development/Libraries
Group(pl):	X11/Programowanie/Biblioteki

%description devel
LibNURBS++ header files.

%description -l pl devel
Pliki nag³ówkowe dla biblioteki libNURBS++

%package static
Summary:	LibNURBS++ static
Summary(pl):	Statyczna wersja biblioteki libNURBS++
Group:		X11/Development/Libraries
Group(pl):	X11/Programowanie/Biblioteki

%description static
libNURBS++ static version.

%description -l pl static
Statycznie linkowana wersja biblioteki libNURBS++

%prep
%setup -q -n nurbs++-%{version}

#%patch

%build
CXXFLAGS="-O2 -mpentium"
export CXXFLAGS
%configure \
    --enable-shared \
    --enable-static \
    --enable-exception \
    --enable-library \
    --with-x \
    --enable-float \
    --enable-double \
    --with-opengl=/usr/X11R6 \
    --without-magick \
    --disable-debug 
    
%{__make} RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc
%attr(,,)

%files devel
%defattr(644,root,root,755)
%doc
%attr(,,)

%files static
%defattr(644,root,root,755)
%doc
%attr(,,)
