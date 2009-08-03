%define upstream_name    Mail-POP3Client
%define upstream_version 2.18

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	POP3Client module for perl (Mail_and_Usenet_News/Mail)
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/S/SD/SDOWD/%{upstream_name}-%{upstream_version}.tar.bz2

%if %{mdkversion} < 1010
Buildrequires:perl-devel
%endif
Buildarch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}
Obsoletes:  perl-POP3Client <= 2.13
Provides:   POP3Client = %{version}

%description
POP3Client is a Perl module to provide an object-oriented interface to a
POP3 server.

%prep 
%setup -q -n %{upstream_name}-%{upstream_version}

%build

CFLAGS="$RPM_OPT_FLAGS" %{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
%makeinstall_std
%{__rm} -rf $RPM_BUILD_ROOT%{perl_archlib}/perllocal.pod

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes  MANIFEST README
%{perl_vendorlib}/Mail/
%_mandir/man3/*
