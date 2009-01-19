Summary: Tcsh dot file enhancements, complete package.
Name: tcshrc
Version: 1.6.0
Release: 1
URL: http://tcshrc.sourceforge.net
Source: http://prdownloads.sourceforge.net/tcshrc/%{name}-%{version}.tar.gz
License: GPL
Group: System Environment/Shells
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildArchitectures: noarch
Requires: tcsh

%description
tcshrc is a collection of dot files that enable all the available
features of the tcsh shell such as intelligent completion, aliases
and key bindings. Once install, each user can opt in and enable 
individually the dot files by running 'tcshrc_config'. The administrator
can also enable tcshrc so that new users can have tcshrc available
by default. If you shell is not tcsh (for example it is bash, 
run "echo $SHELL"), use 'chsh' to change to "/bin/tcsh" to use tcsh.

%prep
%setup -q -n %{name}-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/usr/share/tcshrc
install -m 755 tcshrc_config $RPM_BUILD_ROOT/usr/bin/tcshrc_config
install -m 755 src/tcshrc $RPM_BUILD_ROOT/usr/share/tcshrc
install -m 644 src/tcshrc.alias $RPM_BUILD_ROOT/usr/share/tcshrc/tcshrc.alias
install -m 644 src/tcshrc.bindkey $RPM_BUILD_ROOT/usr/share/tcshrc/tcshrc.bindkey
install -m 644 src/tcshrc.complete $RPM_BUILD_ROOT/usr/share/tcshrc/tcshrc.complete
install -m 644 src/tcshrc.hosts $RPM_BUILD_ROOT/usr/share/tcshrc/tcshrc.hosts
install -m 644 src/tcshrc.set $RPM_BUILD_ROOT/usr/share/tcshrc/tcshrc.set
install -m 644 src/tcshrc.local $RPM_BUILD_ROOT/usr/share/tcshrc/tcshrc.local

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING INSTALL FAQ TODO ChangeLog THANKS doc/tcshrc.pdf doc/tcshrc.ps doc/tcshrc.sgml
%attr(755,root,root)/usr/bin/tcshrc_config
%attr(755,root,root)/usr/share/tcshrc
%attr(644,root,root)/usr/share/tcshrc/tcshrc
%attr(644,root,root)/usr/share/tcshrc/tcshrc.alias
%attr(644,root,root)/usr/share/tcshrc/tcshrc.bindkey
%attr(644,root,root)/usr/share/tcshrc/tcshrc.complete
%attr(644,root,root)/usr/share/tcshrc/tcshrc.hosts
%attr(644,root,root)/usr/share/tcshrc/tcshrc.set

%changelog
* Fri Aug 12 2004 Simos Xenitellis <simos.lists@googlemail.com>
- New version including bugfixes (1.5.0).
* Fri Apr  3 2003 Simos Xenitellis <simos.lists@googlemail.com>
- Initial RPM version (1.2.0).
