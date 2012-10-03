Name:		ruby-qt4
Summary:	Ruby Qt4 bindings
Version: 4.9.2
Release: 1
Epoch:		1
Group:		Development/KDE and Qt
License:	GPLv2 LGPLv2
URL:		http://www.kde.org
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/qtruby-%{version}.tar.xz
BuildRequires:	cmake
BuildRequires:	kde4-macros
Buildrequires:	kdelibs4-devel
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

