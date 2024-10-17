%define upstream_name    Module-Info
%define upstream_version 0.37

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3
Epoch:		1

Summary:	Information about Perl modules 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/M/MB/MBARBON/Module-Info-%{upstream_version}.tar.gz

BuildRequires:  perl(B::Utils)
BuildRequires:	perl-devel
BuildRequires:  perl(Test::More)
BuildArch:	noarch

%description
Module::Info gives you information about Perl modules without actually loading
the module.  It actually isn't specific to modules and should work on any perl
code.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files 
%defattr(-,root,root,755)
%doc Changes
%{_bindir}/*
%{_mandir}/man*/*
%{perl_vendorlib}/B
%{perl_vendorlib}/Module


%changelog
