%define upstream_name    Module-Info
%define upstream_version 0.31

Name: 		perl-%{upstream_name}
Version: 	%perl_convert_version %{upstream_version}
Release: 	%mkrel 1
Epoch:		1

Summary: 	Information about Perl modules 
License: 	GPL+ or Artistic
Group: 		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0: 	http://search.cpan.org/CPAN/authors/id/M/MB/MBARBON/%{upstream_name}-%{upstream_version}.tar.bz2

%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildArch: 	noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}

%description
Module::Info gives you information about Perl modules without actually loading
the module.  It actually isn't specific to modules and should work on any perl
code.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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

