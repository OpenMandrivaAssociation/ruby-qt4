Name:		ruby-qt4
Summary:	Ruby Qt4 bindings
Version:	4.12.1
Release:	1
Epoch:		1
Group:		Development/KDE and Qt
License:	GPLv2 LGPLv2
URL:		http://www.kde.org
%define is_beta %(if test `echo %version |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	ftp://ftp.kde.org/pub/kde/%{ftpdir}/%{version}/src/qtruby-%{version}.tar.xz
BuildRequires:	cmake
BuildRequires:	kde4-macros
BuildRequires:	kdelibs4-devel
BuildRequires:	smokeqt-devel >= 1:%{version}
BuildRequires:	phonon-devel
BuildRequires:	qscintilla-qt4-devel
BuildRequires:	ruby-devel
BuildRequires:	ruby

%description
A Qt4 bindings for Ruby language.

%files
%doc COPYING COPYING.LIB README TODO AUTHORS ChangeLog
%{_kde_bindir}/rbqtapi
%{ruby_sitearchdir}/qscintilla.so
%{ruby_sitearchdir}/qtdeclarative.so
%{ruby_sitearchdir}/qtruby4.so
%{ruby_sitearchdir}/qtuitools.so
%{ruby_sitearchdir}/qtwebkit.so
%{ruby_sitearchdir}/qtscript.so
%{ruby_sitearchdir}/qttest.so
%{ruby_sitearchdir}/phonon.so
%{ruby_sitelibdir}/Qt.rb
%{ruby_sitelibdir}/Qt3.rb
%{ruby_sitelibdir}/Qt4.rb
%{ruby_sitelibdir}/Qt
%{ruby_sitelibdir}/qscintilla
%{ruby_sitelibdir}/qtdeclarative
%{ruby_sitelibdir}/qtuitools
%{ruby_sitelibdir}/qtwebkit
%{ruby_sitelibdir}/qtscript
%{ruby_sitelibdir}/qttest
%{ruby_sitelibdir}/phonon

#------------------------------------------------------------

%define libqtruby4shared_major 2
%define libqtruby4shared %mklibname qtruby4shared %{libqtruby4shared_major}

%package -n %{libqtruby4shared}
Summary:	Qt generic bindings library
Group:		Development/KDE and Qt

%description -n %{libqtruby4shared}
Qt generic bindings library.

%files -n %{libqtruby4shared}
%{_kde_libdir}/libqtruby4shared.so.%{libqtruby4shared_major}*

#------------------------------------------------------------

%package devel
Summary:	Header files for ruby-qt4
Group:		Development/KDE and Qt
Requires:	ruby-qt4 = %{EVRD}
Requires:	%{libqtruby4shared} = %{EVRD}

%description devel
ruby-qt4 devel files.

%files devel
%{_kde_bindir}/rbrcc
%{_kde_bindir}/rbuic4
%{_kde_libdir}/libqtruby4shared.so
%{_kde_includedir}/qtruby
%{_kde_datadir}/qtruby4/cmake/*.cmake

#------------------------------------------------------------

%prep
%setup -qn qtruby-%{version}

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Tue Jan 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.1-1
- New version 4.12.1

* Wed Dec 04 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.4-1
- New version 4.11.4

* Wed Nov 06 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.3-1
- New version 4.11.3

* Wed Oct 02 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.2-1
- New version 4.11.2

* Tue Sep 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.1-1
- New version 4.11.1

* Wed Aug 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.0-1
- New version 4.11.0

* Wed Jul 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.5-1
- New version 4.10.5

* Wed Jun 05 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.4-1
- New version 4.10.4

* Tue May 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.3-1
- New version 4.10.3

* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.2-1
- New version 4.10.2

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.1-1
- New version 4.10.1

* Thu Feb 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.0-1
- New version 4.10.0

* Wed Dec 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.4-1
- New version 4.9.4

* Wed Nov 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.3-1
- New version 4.9.3

* Thu Oct 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.2-1
- New version 4.9.2

* Sat Sep 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.1-1
- New version 4.9.1

* Tue Aug 14 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.0-1
- New version 4.9.0

* Sun Jul 22 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.8.97-1
- New version 4.8.97

* Sun Jul 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.8.95-1
- New version 4.8.95

* Fri Jun 08 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 1:4.8.4-69.1mib2010.2
- New version 4.8.4
- MIB (Mandriva International Backports)

* Fri May 04 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 1:4.8.3-69.1mib2010.2
- New version 4.8.3
- MIB (Mandriva International Backports)

* Wed Apr 04 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 1:4.8.2-69.1mib2010.2
- New version 4.8.2
- MIB (Mandriva International Backports)

* Wed Mar 07 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 1:4.8.1-69.1mib2010.2
- New version 4.8.1
- MIB (Mandriva International Backports)

* Mon Feb 20 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 1:4.8.0-69.2mib2010.2
+ Revision: 771180
- Backport to 2010.2 for MIB users
- MIB (Mandriva International Backports)

* Sat Feb 04 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.8.0-2
+ Revision: 771180
- Rebuild against new ruby

* Thu Jan 19 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.8.0-1
+ Revision: 762418
- New upstream tarball

* Fri Jan 06 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.97-1
+ Revision: 758119
- New upstream tarball

* Tue Jan 03 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.95-1
+ Revision: 748770
- New version

* Wed Dec 14 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.90-1
+ Revision: 740827
- New version

* Mon Nov 21 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.80-1
+ Revision: 732114
- New version 4.7.80

* Tue Sep 20 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.41-1
+ Revision: 700589
- Add runy as buildrequire
- Import qtruby
- Create current folder

