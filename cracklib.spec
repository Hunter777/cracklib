Summary:	Password checking library
Summary(fr):	Biblioth�que de v�rification de mots de passe
Summary(pl):	Biblioteka sprawdzania hase�
Summary(tr):	Parola denetim kitapl���
Name:		cracklib
Version:	2.7
Release:	14
License:	Artistic
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	����������
Group(uk):	��̦�����
Source0:	ftp://coast.cs.purdue.edu/pub/tools/unix/cracklib/%{name}_%{version}.tgz
Patch0:		%{name}.patch
Patch1:		%{name}-pld.patch
Patch2:		%{name}-nss.patch
BuildRequires:	words
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Checks passwords for security related characteristics - length,
uniqueness, whether they are in a word database, etc.

%description -l de
�berpr�ft Pa�w�rter auf Sicherheitsmerkmale - L�nge, Eindeutigkeit,
Anwesenheit in einer W�rter-Datenbank usw.

%description -l fr
V�rifie les caract�ristiques li�es � la s�curit� des mots de passe -
longueur, unicit�, s'ils sont dans une base de mots, etc.

%description -l pl
Sprawdza has�a pod k�tem bezpiecze�stwa - d�ugo��, unikalno��, czy
wyst�puj� w s�owniu itp.

%description -l tr
Parolalar�n uzunluklar�, sistemde tek olmalar�, s�zc�k veri taban�nda
bulunmamalar� gibi g�venlikle ilgili �zelliklerini kontrol eder.

%package devel
Summary:	Header files and documentation for cracklib
Summary(pl):	Pliki nag��wkowe i dokumentacja dla cracklib
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	����������/����������
Group(uk):	��������/��̦�����
Requires:	%{name} = %{version}

%description devel
Header files and documentation for cracklib.

%description devel -l pl
Pliki nag��wkowe i dokumentacja dla cracklib.

%package dicts
Summary:	Standard dictionaries (/usr/share/dict/words)
Summary(de):	Standard-W�rterb�cher (/usr/share/dict/words)
Summary(fr):	Dictionnaires standards (/usr/share/dict/words)
Summary(pl):	Standardowe s�owniki (/usr/share/dict/words)
Summary(tr):	Standart s�zl�kler (/usr/share/dict/words)
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System

%description dicts
Includes the cracklib dictionaries for the standard /usr/dict/words,
as well as utilities needed to create new dictionaries.

%description dicts -l de
Enth�lt die Cracklib-W�rterb�cher f�r die
Standard-/usr/share/dict/W�rter sowie Utilities zum Erstellen neuer
W�rterb�cher"

%description dicts -l fr
Contient les dictionnaires cracklib pour le /usr/share/dict/words
standard, ainsi que les utilitaires n�cessaires � la cr�ation de
nouveaux dictionnaires.

%description dicts -l pl
Pakiet zawiera s�owniki cracklib'a dla standardowego
/usr/share/dict/words oraz narz�dzia do tworzenia nowych s�ownik�w.

%description dicts -l tr
/usr/share/dict/words dosyas� i�in 'cracklib' kitapl�klar�n� ve yeni
s�zl�kler yarat�lmas� i�in gerekli yard�mc� programlar� i�erir.

%prep
%setup	-q -n %{name},%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__make} all

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_libdir},%{_includedir},%{_datadir}/dict}

%{__make} install \
	ROOT=$RPM_BUILD_ROOT

gzip -9nf README MANIFEST LICENCE POSTER HISTORY

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
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
