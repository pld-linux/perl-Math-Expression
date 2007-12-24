#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Math
%define		pnam	Expression
Summary:	Math::Expression - evaluate arithmetic/string expressions
Summary(pl.UTF-8):	Math::Expression - obliczanie wyrażeń arytmetycznych i na łańcuchach znaków
Name:		perl-Math-Expression
Version:	1.17
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	44a4a5996dec011b5f4e155ae17e426a
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module solves the problem of evaluating expressions read from
config files without the use of eval. String and arithmetic operators
are supported, as are: conditions, arrays and functions. The
name-space is managed (for security), user provided functions may be
specified to set/get variable values. Error messages may be via a user
provided function. This is not designed for high computation use.

%description -l pl.UTF-8
Ten moduł rozwiązuje problem obliczania wyrażeń odczytywanych z plików
konfiguracyjnych bez używania eval. Obsługiwane są operatory
arytmetyczne i na łańcuchach znaków, a także: warunki, tablice i
funkcje. Przestrzeń nazw jest zarządzana (ze względów bezpieczeństwa),
mogą być podane funkcje do ustawiania i pobierania wartości zmiennych.
Komunikaty błędów mogą być przekazywane przez podaną funkcję. Moduł
nie jest przeznaczony do skomplikowanych obliczeń.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes Credits README TODO
%{perl_vendorlib}/Math/Expression.pm
%{_mandir}/man3/*
