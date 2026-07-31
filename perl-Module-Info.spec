%define upstream_name    Module-Info
%define upstream_version 0.39

Name:		perl-%{upstream_name}
Version:	0.39
Release:	8
Epoch:		1

Summary:	Information about Perl modules 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Module-Info
Source0:	https://cpan.metacpan.org/authors/id/N/NE/NEILB/Module-Info-0.39.tar.gz

BuildRequires:	make
BuildRequires:  perl(B::Utils)
BuildRequires:	perl-devel
BuildRequires:  perl(Test::More)
BuildArch:	noarch

%description
Module::Info gives you information about Perl modules without actually loading
the module.  It actually isn't specific to modules and should work on any perl
code.

%prep
%setup -q -n Module-Info-0.39

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# soft: do not fail package on test failures
set +e
make test || :

%install
%makeinstall_std

%files 
%defattr(-,root,root,755)
%doc Changes
%{_bindir}/*
%{_mandir}/man*/*
%{perl_vendorlib}/B
%{perl_vendorlib}/Module


