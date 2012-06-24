Summary:     Password checking library
Summary(fr): Biblioth�que de v�rification de mots de passe
Summary(tr): Parola denetim kitapl���
Summary(pl): Biblioteka sprawdzania hase�
Name:        cracklib
Version:     2.7
Release:     4
Group:       Development/Libraries
Group(pl):   Programowanie/Biblioteki
Source:      ftp://coast.cs.purdue.edu/pub/tools/unix/cracklib/%{name}_%{version}.tgz
Patch:       cracklib-2.7-redhat.patch
URL:         ftp://coast.cs.purdue.edu/pub/tools/unix/cracklib/
Copyright:   artistic
Buildroot:   /tmp/%{name}-%{version}-root

%description
Checks passwords for security related characteristics - length, uniqueness, 
whether they are in a word database, etc.

%description -l de
�berpr�ft Pa�w�rter auf Sicherheitsmerkmale - L�nge, Eindeutigkeit, 
Anwesenheit in einer W�rter-Datenbank usw.

%description -l fr
V�rifie les caract�ristiques li�es � la s�curit� des  mots de passe - longueur,
unicit�, s'ils sont dans une base de mots, etc.

%description -l tr
Parolalar�n uzunluklar�, sistemde tek olmalar�, s�zc�k veri taban�nda
bulunmamalar� gibi g�venlikle ilgili �zelliklerini kontrol eder.

%description -l pl
Sprawdza has�a pod k�tem bezpiecze�stwa - d�ugo��, unikalno��, czy
wyst�puj� w s�owniu itp.

%package devel
Summary:     Header files and documentation for cracklib
Summary(pl): Pliki nag��wkowe i dokumentacja dla cracklib
Group:       Development/Libraries
Group(pl):   Programowanie/Biblioteki
Requires:    %{name} = %{version}

%description devel
Header files and documentation for cracklib.

%description -l pl
Pliki nag��wkowe i dokumentacja dla cracklib.

%package dicts
Summary:     Standard dictionaries (/usr/dict/words)
Summary(de): Standard-W�rterb�cher (/usr/dict/words)
Summary(fr): Dictionnaires standards (/usr/dict/words)
Summary(tr): Standart s�zl�kler
Summary(pl): Standardowe s�owniki (/usr/dict/words)
Group:       Utilities/System
Group(pl):   Narz�dzia/System

%description dicts
Includes the cracklib dictionaries for the standard /usr/dict/words, as
well as utilities needed to create new dictionaries.

%description -l de dicts
Enth�lt die Cracklib-W�rterb�cher f�r die Standard-/usr/dict/W�rter sowie
Utilities zum Erstellen neuer W�rterb�cher"

%description -l fr dicts
Contient les dictionnaires cracklib pour le /usr/dict/words standard, ainsi
que les utilitaires n�cessaires � la cr�ation de nouveaux dictionnaires.

%description -l tr dicts
/usr/dict/words dosyas� i�in 'cracklib' kitapl�klar�n� ve yeni s�zl�kler
yarat�lmas� i�in gerekli yard�mc� programlar� i�erir.

%description -l pl
Pakiet zawiera s�owniki cracklib'a dla standardowego /usr/dict/words oraz
narz�dzia do tworzenia nowych s�ownik�w.

%prep
%setup -q -n %{name},%{version}
%patch -p1

%build
make all

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/{sbin,lib,include}
make install ROOT=$RPM_BUILD_ROOT

strip $RPM_BUILD_ROOT/usr/lib/lib*.so.*.*

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644, root, root, 755)
%doc README MANIFEST LICENCE POSTER
%attr(755, root, root) /usr/lib/lib*so.*.*

%files devel
%defattr(644, root, root, 755)
%doc HISTORY
%attr(755, root, root) /usr/lib/lib*so
/usr/include/*

%files dicts
%defattr(644, root, root, 755)
%attr(755, root, root) /usr/sbin/*
/usr/lib/cracklib_dict*

%changelog
* Tue Jan 26 1999 Micha� Kuratczyk <kurkens@polbox.com>
- added pl translations
- cosmetics changes

* Sat Aug 15 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.7-3]
- added -q %setup parameter,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source and %setup,
- added stripping shared libraries,
- added devel subpackage,
- added %attr and %defattr macros in %files (allows build package from
  non-root account).

* Sat May 09 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Mar 10 1998 Cristian Gafton <gafton@redhat.com>
- updated to 2.7
- build shared libraries

* Mon Nov 03 1997 Donnie Barnes <djb@redhat.com>
- added -fPIC

* Mon Oct 13 1997 Donnie Barnes <djb@redhat.com>
- basic spec file cleanups

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc
