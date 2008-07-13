%define module	I18N-Charset
%define name	perl-%{module}
%define version 1.394
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	IANA Character Set Registry names and Unicode::MapUTF8
License:	GPL or Artistic
Group:		Development/Perl
Source:		http://search.cpan.org/CPAN/authors/id/M/MT/MTHURN/%{module}-%{version}.tar.bz2
URL:		http://search.cpan.org/dist/%{module}
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl-IO-Capture >= 0.05-1mdk
BuildRequires:	perl-App-Info
BuildRequires:	perl-Unicode-Map
BuildRequires:	perl-Unicode-Map8
BuildRequires:  perl-IO-String
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This distribution contains a module I18N::Charset which maps Character
Set names to the names officially registered with IANA.  For example,
'Shift_JIS' is the official name of what is often referred to in HTML
headers as 'x-sjis'.

It also maps character set names to Unicode::Map, Unicode::Map8, and
Unicode::MapUTF8 conversion scheme names (if those modules are
installed).  For example, the Unicode::Map8 scheme name for
'windows-1251' is 'cp1251'.

It also maps character set names to their preferred MIME names.  For
example, the preferred MIME name for 'ISO_646.irv:1991' is 'US-ASCII'.

It also maps character set names to conversion scheme names as defined
by the iconv library.  For example, the iconv conversion scheme name
for 'Shift_JIS' is 'MS_KANJI'.

It also maps character set names to encoding names as defined
by the Encode module.  For example, the Encode encoding name
for 'Shift_JIS' is 'shiftjis'.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/I18N
%{_mandir}/*/*

