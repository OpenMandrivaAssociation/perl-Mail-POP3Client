%define upstream_name    Mail-POP3Client
%define upstream_version 2.19

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	POP3Client module for perl (Mail_and_Usenet_News/Mail)
License:	GPL
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/S/SD/SDOWD/Mail-POP3Client-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch
Obsoletes:	perl-POP3Client <= 2.13
Provides:	POP3Client = %{version}

%description
POP3Client is a Perl module to provide an object-oriented interface to a
POP3 server.

%prep 
%setup -q -n %{upstream_name}-%{upstream_version}

%build
CFLAGS="%{optflags}" perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod

%files
%doc Changes  MANIFEST README
%{perl_vendorlib}/Mail/
%{_mandir}/man3/*


%changelog
* Mon Aug 03 2009 Jérôme Quelin <jquelin@mandriva.org> 2.180.0-1mdv2010.0
+ Revision: 407794
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 2.18-4mdv2009.0
+ Revision: 257689
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 2.18-3mdv2009.0
+ Revision: 245775
- rebuild

* Thu Feb 28 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.18-1mdv2008.1
+ Revision: 175983
- update to new version 2.18

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue May 08 2007 Olivier Thauvin <nanardon@mandriva.org> 2.17-1mdv2008.0
+ Revision: 25116
- Import perl-Mail-POP3Client


