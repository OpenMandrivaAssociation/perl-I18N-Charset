%define module	I18N-Charset
%define upstream_version 1.411

Name:		perl-%{module}
Version:	%perl_convert_version %{upstream_version}
Release:	1
Summary:	IANA Character Set Registry names and Unicode::MapUTF8
License:	GPL or Artistic
Group:		Development/Perl
Source:		http://www.cpan.org/authors/id/M/MT/MTHURN/I18N-Charset-%{upstream_version}.tar.gz
URL:		http://search.cpan.org/dist/%{module}
BuildRequires:	perl-devel
BuildRequires:	perl(IO::Capture)
BuildRequires:	perl(App::Info)
BuildRequires:	perl(Unicode::Map)
BuildRequires:	perl(Unicode::Map8)
BuildRequires:	perl(IO::String)
BuildArch:	noarch

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
%setup -q -n %{module}-%{upstream_version} 

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/I18N
%{_mandir}/*/*

%changelog
* Fri Nov 12 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.396-1mdv2011.0
+ Revision: 596558
- update to new version 1.396

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.394-2mdv2011.0
+ Revision: 430467
- rebuild

* Sun Jul 13 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.394-1mdv2009.0
+ Revision: 234278
- update to new version 1.394

* Sun Jul 06 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.392-1mdv2009.0
+ Revision: 232107
- update to new version 1.392

* Mon Jun 30 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.391-1mdv2009.0
+ Revision: 230270
- update to new version 1.391

* Wed May 28 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.389-1mdv2009.0
+ Revision: 212214
- update to new version 1.389

* Fri Feb 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.388-1mdv2008.1
+ Revision: 173947
- update to new version 1.388

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Jul 16 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.385-1mdv2008.0
+ Revision: 52491
- update to new version 1.385

* Tue May 01 2007 Olivier Thauvin <nanardon@mandriva.org> 1.382-1mdv2008.0
+ Revision: 20194
- 1.382


* Tue Dec 20 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.379-1mdk
- New release 1.379
- spec cleanup
- fix directory ownership
- dropped patch (fixed upstream)

* Sun Jul 31 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.375-2mdk
- Fix BuildRequires

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 1.375-1mdk
- initial Mandriva package


