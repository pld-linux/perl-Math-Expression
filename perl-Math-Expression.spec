#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Math
%define	pnam	Expression
Summary:	Math::Expression - evaluate arithmetic/string expressions
Summary(pl):	Math::Expression - obliczanie wyra¿eñ arytmetycznych i na ³añcuchach znaków
Name:		perl-Math-Expression
Version:	1.14
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3efe3b9f1dca35b7fd0ecc79f0fe2b0d
BuildRequires:	perl-devel >= 5.8.0
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

%description -l pl
Ten modu³ rozwi±zuje problem obliczania wyra¿eñ odczytywanych z plików
konfiguracyjnych bez u¿ywania eval. Obs³ugiwane s± operatory
arytmetyczne i na ³añcuchach znaków, a tak¿e: warunki, tablice i
funkcje. Przestrzeñ nazw jest zarz±dzana (ze wzglêdów bezpieczeñstwa),
mog± byc podane funkcje do ustawiania i pobierania warto¶ci zmiennych.
Komunikaty b³êdów mog± byæ przekazywane przez podan± funkcjê. Modu³
nie jest przeznaczony do skomplikowanych obliczeñ.

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
