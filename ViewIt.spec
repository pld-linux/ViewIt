Summary:	Previewer for GNUstep
Summary(pl):	Program do podgl±dania plików dla GNUstepa
Name:		ViewIt
Version:	0.5
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://mac.wms-network.de/gnustep/viewit/%{name}-%{version}.tar.gz
# Source0-md5:	217309a8f51a804b18200da03a0f892d
URL:		http://mac.wms-network.de/gnustep/viewit/viewit.html
BuildRequires:	gnustep-gui-devel >= 0.8.7
Requires:	gnustep-gui >= 0.8.7
Requires:	ghotscript
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		libcombo	gnu-gnu-gnu
%define		gsos		linux-gnu
%ifarch %{ix86}
%define		gscpu		ix86
%else
# also s/alpha.*/alpha/, but we use only "alpha" arch for now
%define		gscpu		%{_target_cpu}
%endif
%define		appdir	%{_libdir}/GNUstep/System/Applications/%{name}.app

%description
ViewIt is a simple file previewer application for GNUstep.

%description -l pl
ViewIt jest prost± aplikacj± do podgl±dania plików przeznaczon± dla
GNUstepa.

%prep
%setup -q -n %{name}

%build
. %{_libdir}/GNUstep/System/Library/Makefiles/GNUstep.sh
%{__make} \
	OPTFLAG="%{rpmcflags}" \
	messages=yes

%install
rm -rf $RPM_BUILD_ROOT
. %{_libdir}/GNUstep/System/Library/Makefiles/GNUstep.sh

%{__make} install \
	GNUSTEP_INSTALLATION_DIR=$RPM_BUILD_ROOT%{_libdir}/GNUstep/System

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{appdir}
%attr(755,root,root) %{appdir}/%{name}
%dir %{appdir}/Resources
%{appdir}/Resources/*.desktop
%{appdir}/Resources/*.plist
%{appdir}/Resources/*.tiff
%{appdir}/Resources/*.gorm
#%{appdir}/Resources/Scripts
%dir %{appdir}/%{gscpu}
%dir %{appdir}/%{gscpu}/%{gsos}
%dir %{appdir}/%{gscpu}/%{gsos}/%{libcombo}
%attr(755,root,root) %{appdir}/%{gscpu}/%{gsos}/%{libcombo}/%{name}
%{appdir}/%{gscpu}/%{gsos}/%{libcombo}/*.openapp
%attr(755,root,root) %{_libdir}/GNUstep/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/*
