Summary:	Java crypto package
Summary(pl):	Pakiet kryptograficzny Javy
Name:		cryptix
Version:	3.2.0
Release:	1
License:	BSD-like
Group:		Development/Languages/Java
%define 	snapshot	20001002
Source0:	http://www.cryptix.org/dist/%{name}32-%{snapshot}-r%{version}.zip
# Source0-md5:	7a3545ede3fff5c89eba601fea03791a
Source1:	%{name}.build.xml
URL:		http://www.cryptix.org/
BuildRequires:	jakarta-ant >= 1.5
BuildRequires:	unzip
Requires:	jre >= 1.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cryptix 3 is a cleanroom implementation of Sun's Java Cryptography
Extensions (JCE) version 1.1. In addition to that it contains the
Cryptix Provider which delivers a wide range of algorithms and support
for PGP 2.x. Cryptix 3 runs on both JDK 1.1 and JDK 1.2 (Java 2).

%description -l pl
Cryptix 3 to implementacja standardu JCE (Java Cryptography
Extensions) Suna w wersji 1.1. Pakiet dodatkowo zawiera Cryptix
Provider, dostarczaj±cy szeroki zakres algorytmów oraz wsparcie dla
PGP 2.x. Cryptix 3 dzia³a zarówno na JDK 1.1 jak i JDK 1.2 (Java 2).

%prep
%setup -q -c
cp %{SOURCE1} build.xml
find . -name "*.jar" -exec rm -f {} \;

%build
ant jar javadoc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}
cp build/lib/%{name}.jar $RPM_BUILD_ROOT%{_javadir}
ln -sf %{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENCE.TXT README.TXT build/api
%{_javadir}/*.jar
