Summary:	PXE default file configurator
Name:		drakpxelinux
Version:	1.2.0
Release:        %mkrel 14
License:	GPLv2+
Group:		System/Configuration/Other
URL:		http://cvs.mandriva.com/cgi-bin/cvsweb.cgi/soft/drakpxelinux/
Source0:	%{name}-%{version}.tar.bz2
Requires:	perl-Gtk2, perl-MDK-Common, pxe, drakxtools, tftp-server, xinetd, pxelinux
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
Buildarch:	noarch

%description
Quick configuration of PXE menu parameters. 

%prep

%setup -q

%build

%install
rm -rf %{buildroot}

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

#install lang
%find_lang %{name}

%post
%update_menus
%update_desktop_database

%postun
%clean_menus
%clean_desktop_database

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc default TODO COPYING
%{_sbindir}/%{name}
%{_sbindir}/deployd
%{_sbindir}/deploy_get_autoinst.pl
%{_sysconfdir}/xinetd.d/deployd
%{_sysconfdir}/xinetd.d/deploy_get_autoinst
#%{_datadir}/%{name}*
%{_datadir}/applications/mandriva-%{name}.desktop

