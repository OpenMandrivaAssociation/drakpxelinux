Summary:	PXE default file configurator
Name:		drakpxelinux
Version:	1.2.1
Release:        %mkrel 8
License:	GPLv2+
Group:		System/Configuration/Other
URL:		http://cvs.mandriva.com/cgi-bin/cvsweb.cgi/soft/drakpxelinux/
Source0:	%{name}-%{version}.tar.bz2
Requires:	perl-Gtk2, perl-MDK-Common, pxe, drakxtools, tftp-server, xinetd, pxelinux
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
Buildarch:	noarch
BuildRoot:	%{_tmppath}/%{name}-buildroot

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

%if %mdkversion < 200900
%post
%update_menus
%update_desktop_database
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%clean_desktop_database
%endif

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



%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-6mdv2011.0
+ Revision: 663860
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-5mdv2011.0
+ Revision: 604824
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-4mdv2010.1
+ Revision: 522511
- rebuilt for 2010.1

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-3mdv2010.0
+ Revision: 413394
- rebuild

* Thu Sep 18 2008 Antoine Ginies <aginies@mandriva.com> 1.2.1-2mdv2009.0
+ Revision: 285598
- add dolly method, update svn info to get the source, remove call to next step in last step's wizard, fix online documentation's url
- new

* Wed Sep 17 2008 Antoine Ginies <aginies@mandriva.com> 1.2.1-1mdv2009.0
+ Revision: 285471
- improve add entry's wizard

* Wed Sep 17 2008 Antoine Ginies <aginies@mandriva.com> 1.2.0-17mdv2009.0
+ Revision: 285456
- fix group
- fix bug 42326

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Thierry Vignaud <tv@mandriva.org>
    - better group

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 1.2.0-15mdv2008.1
+ Revision: 149294
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Sep 19 2007 Antoine Ginies <aginies@mandriva.com> 1.2.0-14mdv2008.0
+ Revision: 90807
- update po files

* Wed Sep 19 2007 Adam Williamson <awilliamson@mandriva.org> 1.2.0-13mdv2008.0
+ Revision: 90128
- rebuild for 2008
- fix XDG menu categories
- drop old menu file
- new license policy

  + Thierry Vignaud <tv@mandriva.org>
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'


* Fri Mar 23 2007 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-12mdv2007.1
+ Revision: 148352
- Import drakpxelinux

* Fri Mar 23 2007 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-12mdv2007.1
- fix the xdg menu stuff

* Thu Sep 21 2006 Antoine Ginies <aginies@mandriva.com> 1.2.0-11mdv2007.0
- use new wizards API (blino)
- add dolly installation method (cs4)

* Fri Sep 16 2005 Antoine Ginies <aginies@n1.mandriva.com> 1.2.0-10mdk
- add deploy_server directly in $o hash, not at end of file (or else it will be ignored) (blino)

* Fri Sep 16 2005 Antoine Ginies <aginies@n1.mandriva.com> 1.2.0-9mdk
- add deploy_get_autoinst deploy_get_autoinst.pl (blino)
- auto_install: test perl script
- catch USR1 signal to update systems tab
- improve auto_install option

* Thu Sep 15 2005 Antoine Ginies <aginies@n1.mandriva.com> 1.2.0-8mdk
- allow to automatically select the network interface #18513 (blino)
- remove PXE entry doesn't remove kernel and initrd
- use auto_install instead of kickstart option
- re-enable local boot in default profil
- fix bug in write/read custom options
- fix ramdisk_size (read/write)
- add quick help on auto-install

* Wed Sep 14 2005 Antoine Ginies <aginies@n1.mandriva.com> 1.2.0-7mdk
- clone/add/remove now refresh default boot menu
- remove old code
- user can't change initrd and kernel path

* Sun Sep 11 2005 Antoine Ginies <aginies@n1.mandriva.com> 1.2.0-6mdk
- set default vga option to 788
- force default boot for a profil

* Wed Sep 07 2005 Antoine Ginies <aginies@n1.mandriva.com> 1.2.0-5mdk
- move drakpxelinux.pl in /usr/sbin directory to be able to use consolehelper
- fix missing directory

* Tue Sep 06 2005 Antoine Ginies <aginies@n1.mandriva.com> 1.2.0-4mdk
- fx default boot for profile

* Tue Sep 06 2005 Antoine Ginies <aginies@n1.mandriva.com> 1.2.0-3mdk
- major bug fix: write_conf, fix local pb, fix duplicate default config
- update all PO files (thx translators)

* Sat Sep 03 2005 Antoine Ginies <aginies@n1.mandriva.com> 1.2.0-2mdk
- fix vga resolution pb
- fix pb of duplicate entry in systems tab (need to update systems avec get all mac addr)
- now we can clone PXE entry
- select default boot in combobox
- fix memdisk/data.img and kernel/initrd test
- fix: add an entry only if a profile is selected

* Fri Sep 02 2005 Antoine Ginies <aginies@n1.mandriva.com> 1.2.0-1mdk
- various imrpovement (from blino's kadeploy)
- add xinetd.d daemon (blino)

* Fri Jul 22 2005 Antoine Ginies <aginies@n1.mandrakesoft.com> 1.1.0-2mdk
- convert vga codes and resolutions when appropriate (blino)
- fix installation method

* Thu Jul 14 2005 Antoine Ginies <aginies@n1.mandrakesoft.com> 1.1.0-1mdk
- improve GUI
- add menu
- remove "instant change", and add an apply button
- use consolehelper
- avoid remove/edit local entry

* Wed Jul 13 2005 Olivier Blin <oblin@mandriva.com> 1.0.2-6mdk
- move configuration code to network::pxe, cleanups
- fix vga resolutions list in Edit window
- add profiles support

* Tue Mar 22 2005 Antoine Ginies <aginies@n1.mandrakesoft.com> 1.0.2-5mdk
- fix wizard
- add ka method

* Tue Feb 15 2005 guibo <guibo@guiboserv.guibland.com> 1.0.2-4mdk
- fix init in PXE server (wizard)

* Fri Feb 11 2005 guibo <guibo@nodewireless.guibland.com> 1.0.2-3mdk
- fix bug (update vmlinuz and initrd files)

* Mon Jan 24 2005 Antoine Ginies <aginies@n1.mandrakesoft.com> 1.0.2-2mdk
- update po files.

* Fri Nov 12 2004 guibo <guibo@node80.guibland.com> 1.0.2-1mdk
- fix custom option, dhcp/ip addr
- add test in add wizard
- now support multiple interfaces
- add a button to reconfigure PXE server
- display resolution instead of vga code

* Sat Oct 02 2004 Antoine Ginies <aginies@n1.mandrakesoft.com> 1.0.1-3mdk
- add missing po files

* Wed Sep 15 2004 Antoine Ginies <aginies@mandrakesoft.com> 1.0.1-2mdk
- fix busy cursor

* Tue Aug 31 2004 guibo <guibo@node80.guibland.com> 1.0.1-1mdk
- typo fix (Joao Ferreira; Arpad Biro)

* Sat Aug 14 2004 Antoine Ginies <aginies@mandrakesoft.com> 1.0.0-1mdk
- add a check of pxe.conf file
- add a check box for DHCP or ip address
- add test on IP address
- display vga resolution in edit box
- perl_checker fix
- rearrange some widgets (thx Mokaddem)
- fix label in column
- thx R1 for help/idea, Chandra/Nicolabs for test

* Thu Aug 12 2004 mdkc Antoine Ginies <aginies@mandrakesoft.com> 0.9.1-1mdk
- add a file dialog box for directory
- some clean in code

* Wed Aug 11 2004 Antoine Ginies <aginies@mandrakesoft.com> 0.9.0-2mdk
- fix pb of same var in code

* Sun Aug 08 2004 Antoine Ginies <aginies@mandrakesoft.com> 0.9.0-1mdk
- add interactive help
- use OptionMenu instead of Combo box

* Sat Aug 07 2004 guibo <guibo@node80.guibland.com> 0.8.0-3mdk
- remove kernel/initrd in remove mode
- default options are blank in add image
- add a test in file selection
- readjust info in wizard
- add a wait message in wizard
- add info in edit box
- add a dialog box (first time launch)

* Sat Aug 07 2004 guibo <guibo@node80.guibland.com> 0.8.0-2mdk
- improve get information
- fix pb of wizard
- block rename of label (to fix pb of same label name)
- typo

* Sat Aug 07 2004 Antoine Ginies <aginies@mandrakesoft.com> 0.8.0-1mdk
- fix button display
- add help.txt support
- fix wizard
- add label
- enable tftp server
- save old config
- add wizard to add an image in pxe
- cell no more editable
- fix get_information in help.txt

* Fri Aug 06 2004 guibo <guibo@node80.guibland.com> 0.7.0-1mdk
- fix display pb
- add entry in menu
- correct requires

* Fri Jul 30 2004 Antoine Ginies <aginies@mandrakesoft.com> 0.6.0-1mdk
- fix edit dialog box
- now support embedded mode (mcc)

* Thu Jul 29 2004 mdkc <mdkc@dhcp114.mandrakesoft.com> 0.5.0-2mdk
- fix cancel button (initrd/kernel choice)

* Fri Jul 23 2004 Antoine Ginies <aginies@mandrakesoft.com> 0.5.0-1mdk
- first release

