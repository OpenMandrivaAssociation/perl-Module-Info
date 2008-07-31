%define module  Module-Info
%define	name	perl-%{module}
%define version 0.31
%define release %mkrel 4

Name: 		%{name}
Epoch:		1
Version: 	%{version}
Release: 	%{release}
Summary: 	Information about Perl modules 
License: 	GPL or Artistic
Group: 		Development/Perl
Source: 	http://search.cpan.org/CPAN/authors/id/M/MB/MBARBON/%{module}-%{version}.tar.bz2
Url:            http://search.cpan.org/dist/%{module}
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildArch: 	noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}

%description
Module::Info gives you information about Perl modules without actually loading
the module.  It actually isn't specific to modules and should work on any perl
code.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%{makeinstall_std}

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root,755)
%doc Changes
%{_bindir}/*
%{_mandir}/man*/*
%{perl_vendorlib}/B
%{perl_vendorlib}/Module

