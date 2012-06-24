#
# Conditional build:
%bcond_with	words	# bigger words database
#
Summary:	Password checking library
Summary(es):	Biblioteca de chequeo de contrase�as
Summary(fr):	Biblioth�que de v�rification de mots de passe
Summary(pl):	Biblioteka sprawdzania hase�
Summary(pt_BR):	Biblioteca de checagem de senhas
Summary(ru):	���������� �������� �������
Summary(tr):	Parola denetim kitapl���
Summary(uk):	��̦����� ����צ��� ����̦�
Name:		cracklib
Version:	2.8.3
Release:	0.2
License:	GPL v2
Group:		Libraries
Source0:	http://dl.sourceforge.net/cracklib/%{name}-%{version}.tar.gz
# Source0-md5:	13f82f75b892cbd0ba7cb9069e307006
Source1:	http://dl.sourceforge.net/cracklib/cracklib-words.gz
# Source1-md5:	d18e670e5df560a8745e1b4dede8f84f
URL:		http://sourceforge.net/projects/cracklib/
Patch0:		%{name}-pld.patch
BuildRequires:	words
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CrackLib tests passwords to determine whether they match certain
security-oriented characteristics. You can use CrackLib to stop users
from choosing passwords which would be easy to guess. CrackLib
performs certain tests:

- It tries to generate words from a username and gecos entry and
  checks those words against the password;
- It checks for simplistic patterns in passwords;
- It checks for the password in a dictionary.

CrackLib is actually a library containing a particular C function
which is used to check the password, as well as other C functions.
CrackLib is not a replacement for a passwd program; it must be used in
conjunction with an existing passwd program.

Install the cracklib package if you need a program to check users'
passwords to see if they are at least minimally secure. If you install
CrackLib, you'll also want to install the cracklib-dicts package.

%description -l de
�berpr�ft Pa�w�rter auf Sicherheitsmerkmale - L�nge, Eindeutigkeit,
Anwesenheit in einer W�rter-Datenbank usw.

%description -l fr
V�rifie les caract�ristiques li�es � la s�curit� des mots de passe -
longueur, unicit�, s'ils sont dans une base de mots, etc.

%description -l pl
CrackLib sprawdza has�a pod k�tem bezpiecze�stwa. Mo�na u�y� tej
biblioteki do powstrzymywania u�ytkownik�w przed wybieraniem hase�
�atwych do odgadni�cia. CrackLib przeprowadza nast�puj�ce testy:

- pr�buje wygenerowa� s�owa z nazwy u�ytkownika i wpisu gecos, a
  nast�pnie por�wnuje je z has�em
- szuka prostych wzorc�w w ha�le
- szuka has�a w s�owniku

CrackLib to biblioteka zawieraj�ca funkcj� C s�u��c� do sprawdzania
has�a oraz inne funkcje C. Nie jest to zamiennik programu passwd -
musi by� u�yty w po��czeniu z istniej�cym programem passwd.

%description -l pt_BR
Inclui os dicion�rios cracklib para o padr�o /usr/dict/words, assim
como os utilit�rios necess�rios para criar dicion�rios.

%description -l ru
CrackLib ��������� ������ �� ������� ������������ ��������� ���������
������������. ��� ����� ���� ������������ ��� �������������� ������
�������������� ���������������� �������. CrackLib ���������� �����
�����:

- ���������� ����� �� ����� ������������ � ���� gecos � ���������� ��
  � �������;
- ���� � ������� ������� �������;
- ��������� ������ �� ������� ��� � �������.

CrackLib - ���, ����������, ����������, ���������� �������������
������� C ��� ���������� ������� � ��������� ������ �������. ��� ��
������ ��������� passwd, �� ���� ������������ ��������� � ������������
���������� passwd.

%description -l tr
Parolalar�n uzunluklar�, sistemde tek olmalar�, s�zc�k veri taban�nda
bulunmamalar� gibi g�venlikle ilgili �zelliklerini kontrol eder.

%description -l uk
CrackLib ����צ�Ѥ ����̦ �� צ���צ�Φ��� ������ �����Ҧ�� �������.
���� ���� ���� ����������� ��� ����¦����� ������ �������������
����̦�, �˦ ����� צ�������. ���� �����դ ��˦ �����:

- �����դ ����� � ���Φ ����������� �� ���� gecos � ��Ҧ���� �� �
  �������;
- ����� � ������� ����Ԧ �������;
- ����צ�Ѥ ����̦ �� ����Φ��� �� � ��������.

CrackLib - ��, ������, ¦�̦�����, �� ͦ����� �����Ʀ��� ����æ� C ���
צ���������� ����̦� �� ���˦ ��ۦ ����æ�. �� �� ��ͦ�� ��������
passwd, �� ����� ��������������� �Ц���� � �������� ��������� passwd.

%package devel
Summary:	Header files and documentation for cracklib
Summary(es):	Archivos de inclusi�n y bibliotecas para cracklib
Summary(pl):	Pliki nag��wkowe i dokumentacja dla cracklib
Summary(pt_BR):	Arquivos de inclus�o e bibliotecas para a cracklib
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files and documentation for cracklib.

%description devel -l es
Este paquete contiene los archivos de inclusi�n y bibliotecas que se
necesitan para desarrollar programas que usan cracklib.

%description devel -l pl
Pliki nag��wkowe i dokumentacja dla cracklib.

%description devel -l pt_BR
Este pacote cont�m os arquivos de inclus�o e bibliotecas que s�o
necess�rios para desenvolver programas que usam a cracklib.

%package static
Summary:	Static cracklib library
Summary(pl):	Statyczna biblioteka cracklib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static cracklib library.

%description static -l pl
Statyczna biblioteka cracklib.

%package dicts
Summary:	Standard dictionaries (/usr/share/dict/words)
Summary(de):	Standard-W�rterb�cher (/usr/share/dict/words)
Summary(es):	Diccionarios para chequeo de contrase�as
Summary(fr):	Dictionnaires standards (/usr/share/dict/words)
Summary(pl):	Standardowe s�owniki (/usr/share/dict/words)
Summary(pt_BR):	Dicion�rios para checagem de senhas
Summary(ru):	����������� ������� CrackLib
Summary(tr):	Standart s�zl�kler (/usr/share/dict/words)
Summary(uk):	��������Φ �������� CrackLib
Group:		Applications/System

%description dicts
The cracklib-dicts package includes the CrackLib dictionaries.
CrackLib will need to use the dictionary appropriate to your system,
which is normally put in /usr/share/dict/words. Cracklib-dicts also
contains the utilities necessary for the creation of new dictionaries.

%description dicts -l de
Enth�lt die Cracklib-W�rterb�cher f�r die
Standard-/usr/share/dict/W�rter sowie Utilities zum Erstellen neuer
W�rterb�cher"

%description dicts -l es
Incluye el diccionario cracklib para el padr�n /usr/share/dict/words,
y utilitarios necesarios a creaci�n de nuevos diccionarios.

%description dicts -l fr
Contient les dictionnaires cracklib pour le /usr/share/dict/words
standard, ainsi que les utilitaires n�cessaires � la cr�ation de
nouveaux dictionnaires.

%description dicts -l pl
Pakiet zawiera s�owniki cracklib'a dla standardowego
/usr/share/dict/words oraz narz�dzia do tworzenia nowych s�ownik�w.

%description dicts -l pt_BR
Inclui o dicion�rio cracklib para o padr�o /usr/dict/words, bem como
utilit�rios necess�rios a cria��o de novos dicion�rios.

%description dicts -l ru
����� cracklib-dicts �������� ������� CrackLib. CrackLib ����� �����
�������, ��������������� ����� �������, ������� ������ ��������� �
/usr/share/dict/words. Cracklib-dicts ����� �������� �������,
����������� ��� �������� ����� ��������.

%description dicts -l tr
/usr/share/dict/words dosyas� i�in 'cracklib' kitapl�klar�n� ve yeni
s�zl�kler yarat�lmas� i�in gerekli yard�mc� programlar� i�erir.

%description dicts -l uk
����� cracklib-dicts ͦ����� �������� CrackLib. CrackLib ������
���Ҧ�Φ ��������, �� צ���צ����� ��ۦ� �����ͦ, ���Ҧ ��������
����������� � /usr/share/dict/words. Cracklib-dicts ����� ͦ�����
���̦��, ����Ȧ�Φ ��� ��������� ����� ������˦�.

%prep
%setup	-q
%patch0 -p0
%if %{with words} 
install %{SOURCE1} dicts/
%endif

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_libdir},%{_includedir},%{_datadir}/dict}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

util/cracklib-format dicts/cracklib* | util/cracklib-packer $RPM_BUILD_ROOT%{_datadir}/dict/cracklib_dict

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libcrack.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcrack.so
%{_libdir}/libcrack.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libcrack.a

%files dicts
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/*
%{_datadir}/dict/cracklib_dict*
