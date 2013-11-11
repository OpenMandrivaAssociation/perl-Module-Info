%define upstream_name    Module-Info
%define upstream_version 0.35

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1
Epoch:		1

Summary:	Information about Perl modules 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/M/MB/MBARBON/Module-Info-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
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
* Sun Nov 14 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1:0.320.0-1mdv2011.0
+ Revision: 597616
- update to new version 0.32

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 1:0.310.0-1mdv2011.0
+ Revision: 401630
- rebuild using %%perl_convert_version
- fixed license field

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1:0.31-4mdv2009.0
+ Revision: 257855
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1:0.31-3mdv2009.0
+ Revision: 245940
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1:0.31-1mdv2008.1
+ Revision: 136289
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Jul 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1:0.31-1mdv2008.0
+ Revision: 46653
- update to new version 0.31


* Tue Mar 21 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1:0.30-1mdk
- new version

* Mon Dec 19 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.290-1mdk
- new version
- spec cleanup
- fix directory ownership
- rpmbuilupdate aware
- %%{1}mdk
- better summary

* Fri Apr 22 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.28-1mdk
- 0.28

* Mon Mar 07 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.27-1mdk
- 0.27
- add tests, fix POD in description

* Sat Jul 17 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.26-1mdk
- 0.26

* Tue Feb 17 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.24-1mdk
- 0.24

* Wed Apr 16 2003 Peter Chen <petechen@netilla.com> 0.19-1mdk
- Initial packaging.



