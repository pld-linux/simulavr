Summary:	A simulator for Atmel's AVR family of microcontrollers
Summary(pl.UTF-8):	Symulator dla rodziny mikrokontrolerów Atmel's AVR
Name:		simulavr
Version:	0.1.2.2
Release:	1
License:	GPL
Group:		Development/Debuggers
Source0:	http://savannah.nongnu.org/download/simulavr/%{name}-%{version}.tar.gz
# Source0-md5:	7fa27cddaa3397046538bf5b916fdc11
Patch0:		%{name}-doc.patch
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

%description -l pl.UTF-8
Simulavr jest symulatorem dla rodziny mikrokontrolerów Atmel AVR. Może
być wykorzystywany osobno, lub jako zdalny target dla gdb. Gdy jest
wykorzystywany jako zdalny target dla gdb, symulatorów jest używany
jak nakładka na gdb tak, że gdb może być użyty jako debugger na
poziomie kodu źródłowego.

%prep
%setup -q
%patch0 -p1

%build
CFLAGS="%{rpmcflags} -I/usr/include/ncurses"
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

%post	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING INSTALL ProjSummary
%doc README README.gdb README.opcodes TODO
%doc doc/
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/simulavr*
%{_infodir}/*
