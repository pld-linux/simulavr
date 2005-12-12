Summary:	A simulator for Atmel's AVR family of microcontrollers
Summary(pl):	Symulator dla rodziny mikrokontrolerów Atmel's AVR
Name:		simulavr
Version:	0.1.2.1
Release:	2
License:	GPL
Group:		Development/Debuggers
Source0:	http://savannah.nongnu.org/download/simulavr/%{name}-%{version}.tar.bz2
# Source0-md5:	7fbf757f285ac9fd2d22604df6a9ee5f
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	crossavr-gcc
BuildRequires:	doxygen
BuildRequires:	ncurses-devel
BuildRequires:	tetex
BuildRequires:	texinfo-texi2dvi
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simulavr is a simulator for the Atmel AVR family of microcontrollers.
Simulavr can be used either standalone or as a remote target for gdb.
When used as a remote target for gdb, the simulator is used as a
backend to gdb such that gdb can be used as a source level debugger.

%description -l pl
Simulavr jest symulatorem dla rodziny mikrokontrolerów Atmel AVR. Mo¿e
byæ wykorzystywany osobno, lub jako zdalny target dla gdb. Gdy jest
wykorzystywany jako zdalny target dla gdb, symulatorów jest u¿ywany
jak nak³adka na gdb tak, ¿e gdb mo¿e byæ u¿yty jako debugger na
poziomie kodu ¼ród³owego.

%prep
%setup -q

%build
CFLAGS="%{rpmcflags} -I%{_includedir}/ncurses"
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-tests
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING INSTALL ProjSummary
%doc README README.gdb README.opcodes TODO
%doc doc/
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/simulavr*
%{_infodir}/*
