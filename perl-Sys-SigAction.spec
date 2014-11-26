#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define	pdir	Sys
%define	pnam	SigAction
%include	/usr/lib/rpm/macros.perl
Summary:	Sys::SigAction - Perl extension for Consistent Signal Handling
Name:		perl-Sys-SigAction
Version:	0.15
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Sys/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	54789a1893f63c2345b1014fcb7c47a7
URL:		http://search.cpan.org/dist/Sys-SigAction/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl extension for Consistent Signal Handling.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Sys/*.pm
%{_mandir}/man3/*
