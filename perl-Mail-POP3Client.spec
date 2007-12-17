%define name perl-%{realname}
%define realname Mail-POP3Client
%define version 2.17
%define release %mkrel 1

Name:		%{name}
Summary:	POP3Client module for perl (Mail_and_Usenet_News/Mail)
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{realname}
Source:		http://search.cpan.org/CPAN/authors/id/S/SD/SDOWD/%{realname}-%{version}.tar.bz2
%if %{mdkversion} < 1010
Buildrequires:perl-devel
%endif
Buildarch:	noarch
Obsoletes:  perl-POP3Client <= 2.13
Provides:   POP3Client = %version

%description
POP3Client is a Perl module to provide an object-oriented interface to a
POP3 server.

%prep 

%setup -q -n %{realname}-%{version}

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

