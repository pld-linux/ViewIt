Summary:	Previewer for GNUstep
Name:		ViewIt
Version:	0.5
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://mac.wms-network.de/gnustep/viewit/%{name}-%{version}.tar.gz
URL:		http://mac.wms-network.de/gnustep/viewit/viewit.html
BuildRequires:	gnustep-gui-devel >= 0.8.7
Requires:	gnustep-gui >= 0.8.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		libcombo	gnu-gnu-gnu
%define		gsos		linux-gnu
%ifarch %{ix86}
%define		gscpu		ix86
%else
# also s/alpha.*/alpha/, but we use only "alpha" arch for now
%define		gscpu		%{_target_cpu}
%endif
%define appdir     %{_libdir}/GNUstep/System/Applications/CodeEditor.app
%define supportdir %{_libdir}/GNUstep/System/Library/ApplicationSupport/CodeEditorView

%description
ViewIt, is a simple file previewer application for GNUstep.

%prep
%setup -q -n %{name}

%build
. %{_libdir}/GNUstep/System/Library/Makefiles/GNUstep.sh
%{__make} \
	OPTFLAG="%{rpmcflags}" \
	messages=yes

%install
rm -rf $RPM_BUILD_ROOT
. %{_prefix}/System/Library/Makefiles/GNUstep.sh

%{__make} install \
	GNUSTEP_INSTALLATION_DIR=$RPM_BUILD_ROOT%{_libdir}/GNUstep/System

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%dir %{appdir}
%attr(755,root,root) %{appdir}/%{name}
%dir %{_prefix}/System/Applications/ImageViewer.app/Resources
%dir %{appdir}/Resources
%{appdir}/Resources/*.desktop
%{appdir}/Resources/*.plist
%{appdir}/Resources/*.tiff
%{appdir}/Resources/*.gorm
%{appdir}/Resources/Scripts
%dir %{appdir}/%{gscpu}
%dir %{appdir}/%{gscpu}/%{gsos}
%dir %{appdir}/%{gscpu}/%{gsos}/%{libcombo}
%attr(755,root,root) %{appdir}/%{gscpu}/%{gsos}/%{libcombo}/%{name}
%{appdir}/%{gscpu}/%{gsos}/%{libcombo}/*.openapp
