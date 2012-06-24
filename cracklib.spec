Summary:	Password checking library
Summary(es):	Biblioteca de chequeo de contrase�as
Summary(fr):	Biblioth�que de v�rification de mots de passe
Summary(pl):	Biblioteka sprawdzania hase�
Summary(pt_BR):	Biblioteca de checagem de senhas
Summary(ru):	���������� �������� �������
Summary(tr):	Parola denetim kitapl���
Summary(uk):	��̦����� ����צ��� ����̦�
Name:		cracklib
Version:	2.7
Release:	16
License:	Artistic
Group:		Libraries
Source0:	ftp://coast.cs.purdue.edu/pub/tools/unix/libs/cracklib/%{name}_%{version}.tgz
# Source0-md5: 7f810e310c7f2df33d1eaa2b41ab2435
Patch0:		%{name}.patch
Patch1:		%{name}-pld.patch
Patch2:		%{name}-nss.patch
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

%description -l es
Incluye los diccionarios cracklib para el padr�n /usr/dict/words, as�
como, los utilitarios necesarios para crear diccionarios.

%description -l fr
V�rifie les caract�ristiques li�es � la s�curit� des mots de passe -
longueur, unicit�, s'ils sont dans une base de mots, etc.

%description -l pl
Sprawdza has�a pod k�tem bezpiecze�stwa - d�ugo��, unikalno��, czy
wyst�puj� w s�owniu itp.

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
Requires:	%{name} = %{version}

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
Incluye el diccionario cracklib para el padr�n /usr/dict/words, bien
como utilitarios necesarios a creaci�n de nuevos diccionarios.

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
%setup	-q -n %{name},%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__make} all \
	CC="%{__cc}" \
	OPTFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_libdir},%{_includedir},%{_datadir}/dict}

%{__make} install \
	ROOT=$RPM_BUILD_ROOT

install cracklib/packer.h $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README MANIFEST LICENCE POSTER HISTORY

%attr(755,root,root) %{_libdir}/lib*so.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*

%files dicts
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/*
%{_datadir}/dict/cracklib_dict*
