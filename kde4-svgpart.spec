%define		_state		stable
%define		orgname		svgpart
%define		qtver		4.7.3

Summary:	K Desktop Environment - svgpart
Name:		svgpart
Version:	4.7.0
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.bz2
# Source0-md5:	64e10ccf126668a4fb3af337bd547a13
URL:		http://www.kde.org/
BuildRequires:	kde4-kdelibs-devel
Obsoletes:	kde4-kdegraphics-svgpart
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

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/svgpart.so
%{_datadir}/apps/svgpart
%{_datadir}/kde4/services/svgpart.desktop
