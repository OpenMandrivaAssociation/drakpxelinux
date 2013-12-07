Summary:	PXE default file configurator
Name:		drakpxelinux
Version:	1.2.1
Release:	12
License:	GPLv2+
Group:		System/Configuration/Other
Url:		http://cvs.mandriva.com/cgi-bin/cvsweb.cgi/soft/drakpxelinux/
Source0:	%{name}-%{version}.tar.bz2
Buildarch:	noarch

Requires:	drakxtools
Requires:	perl-Gtk2
Requires:	perl-MDK-Common
Requires:	pxe
Requires:	pxelinux
Requires:	tftp-server
Requires:	xinetd
Requires(post,postun):	desktop-file-utils

%description
Quick configuration of PXE menu parameters. 

%prep
%setup -q

%build

%install

make prefix=%{buildroot} install 

# XDG menu
install -d %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Drakpxelinux
Comment=Mandriva Linux Pxelinux configurator
Exec=%{_sbindir}/%{name}
Icon=configuration_section
Terminal=false
Type=Application
Categories=GTK;Settings;X-Mandriva-CrossDesktop;
EOF

%find_lang %{name}

%files -f %{name}.lang
%doc default TODO COPYING
%{_sbindir}/%{name}
%{_sbindir}/deployd
%{_sbindir}/deploy_get_autoinst.pl
%{_sysconfdir}/xinetd.d/deployd
%{_sysconfdir}/xinetd.d/deploy_get_autoinst
#%{_datadir}/%{name}*
%{_datadir}/applications/mandriva-%{name}.desktop

