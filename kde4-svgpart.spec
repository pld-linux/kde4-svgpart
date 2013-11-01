%define		_state		stable
%define		orgname		svgpart
%define		qtver		4.8.1

Summary:	K Desktop Environment - svgpart
Name:		kde4-svgpart
Version:	4.11.3
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	8f2f000322b13db839fef9ee71e2962d
URL:		http://www.kde.org/
BuildRequires:	kde4-kdelibs-devel >= %{version}
Obsoletes:	kde4-kdegraphics-svgpart < 4.6.99
Obsoletes:	svgpart <= 4.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
svgpart

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/svgpart.so
%{_datadir}/apps/svgpart
%{_datadir}/kde4/services/svgpart.desktop
