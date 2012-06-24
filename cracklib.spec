Summary:	Password checking library
Summary(fr):	Biblioth�que de v�rification de mots de passe
Summary(tr):	Parola denetim kitapl���
Summary(pl):	Biblioteka sprawdzania hase�
Name:		cracklib
Version:	2.7
Release:	8
Group:		Libraries
Group(pl):	Biblioteki
Copyright:	artistic
Source:		%{name}_%{version}.tgz
Patch0:		cracklib.patch
Patch1:		cracklib-pld.patch
BuildRequires:	words
URL:		ftp://coast.cs.purdue.edu/pub/tools/unix/cracklib
Buildroot:	/tmp/%{name}-%{version}-root

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

%package	devel
Summary:	Header files and documentation for cracklib
Summary(pl):	Pliki nag��wkowe i dokumentacja dla cracklib
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files and documentation for cracklib.

%description -l pl
Pliki nag��wkowe i dokumentacja dla cracklib.

%package	dicts
Summary:	Standard dictionaries (/usr/share/dict/words)
Summary(de):	Standard-W�rterb�cher (/usr/share/dict/words)
Summary(fr):	Dictionnaires standards (/usr/share/dict/words)
Summary(tr):	Standart s�zl�kler (/usr/share/dict/words)
Summary(pl):	Standardowe s�owniki (/usr/share/dict/words)
Group:		Utilities/System
Group(pl):	Narz�dzia/System

%description dicts
Includes the cracklib dictionaries for the standard /usr/dict/words, as
well as utilities needed to create new dictionaries.

%description -l de dicts
Enth�lt die Cracklib-W�rterb�cher f�r die Standard-/usr/share/dict/W�rter sowie
Utilities zum Erstellen neuer W�rterb�cher"

%description -l fr dicts
Contient les dictionnaires cracklib pour le /usr/share/dict/words standard,
ainsi que les utilitaires n�cessaires � la cr�ation de nouveaux dictionnaires.

%description -l tr dicts
/usr/share/dict/words dosyas� i�in 'cracklib' kitapl�klar�n� ve yeni s�zl�kler
yarat�lmas� i�in gerekli yard�mc� programlar� i�erir.

%description -l pl
Pakiet zawiera s�owniki cracklib'a dla standardowego /usr/share/dict/words oraz
narz�dzia do tworzenia nowych s�ownik�w.

%prep
%setup  -q -n %{name},%{version}
%patch0 -p1
%patch1 -p1

%build
make all

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/{sbin,lib,include,share/dict}

make \
    ROOT=$RPM_BUILD_ROOT \
    install

strip	 $RPM_BUILD_ROOT%{_sbindir}/packer
strip	--strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

gzip -9nf README MANIFEST LICENCE POSTER HISTORY

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc {README,MANIFEST,LICENCE,POSTER}.gz

%attr(755,root,root) %{_libdir}/lib*so.*

%files devel
%defattr(644,root,root,755)
%doc HISTORY.gz
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*

%files dicts
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/*
%{_datadir}/dict/cracklib_dict*
